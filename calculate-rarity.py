import os
import re
import json
import sys
from collections import defaultdict

# Helper function to parse index input (supports comma, space, and range formats)
def parse_index_input(input_str):
    """
    Parse index input supporting formats like:
    - "1,5,10,15" (comma-separated)
    - "1 5 10 15" (space-separated)
    - "1-5,10,15" (ranges with commas)
    - "1-5 10 15" (ranges with spaces)
    - Any combination of the above
    Returns a set of unique index numbers
    """
    if not input_str.strip():
        return set()
    
    indices = set()
    # Replace commas with spaces for uniform parsing
    input_str = input_str.replace(',', ' ')
    
    # Split by whitespace
    parts = input_str.split()
    
    for part in parts:
        part = part.strip()
        if not part:
            continue
            
        # Check if it's a range (e.g., "1-5")
        if '-' in part:
            try:
                start, end = part.split('-', 1)
                start_num = int(start.strip())
                end_num = int(end.strip())
                # Add all numbers in range (inclusive)
                for i in range(start_num, end_num + 1):
                    indices.add(i)
            except (ValueError, AttributeError):
                print(f"Warning: Could not parse range '{part}', skipping...")
                continue
        else:
            # Single number
            try:
                indices.add(int(part))
            except ValueError:
                print(f"Warning: Could not parse number '{part}', skipping...")
                continue
    
    return indices

# Interactive file input with smart path resolution
raw_input_path = input("Enter path to metadata JSON file: ").strip()
expanded_path = os.path.expanduser(raw_input_path)
abs_path = os.path.abspath(expanded_path)

base_dir = os.path.dirname(os.path.realpath(__file__))

# Smart path resolution - try multiple locations
if not os.path.isfile(abs_path):
    project_root = os.path.normpath(os.path.join(base_dir, '..'))
    candidate = os.path.normpath(os.path.join(project_root, raw_input_path))
    if os.path.isfile(candidate):
        input_meta = candidate
    else:
        print(f"Error: File not found: {abs_path}")
        sys.exit(1)
else:
    input_meta = abs_path

# File management setup
input_meta = os.path.normpath(input_meta)
metadata_dir = os.path.dirname(input_meta)
base_name = os.path.splitext(os.path.basename(input_meta))[0]

# Find the repo root by looking for the rarity directory
# Start from the script directory and search upwards
repo_root = base_dir
while repo_root != os.path.dirname(repo_root):  # Stop at filesystem root
    potential_rarity_dir = os.path.join(repo_root, 'rarity')
    if os.path.isdir(potential_rarity_dir):
        rarity_dir = potential_rarity_dir
        break
    repo_root = os.path.dirname(repo_root)
else:
    # If not found, create it in the current directory
    rarity_dir = os.path.join(base_dir, 'rarity')

rarity_dir = os.path.normpath(rarity_dir)

# Ensure directories exist
os.makedirs(metadata_dir, exist_ok=True)
os.makedirs(rarity_dir, exist_ok=True)

# Versioning system function
def next_version(dir_path, pattern):
    max_ver = 0
    for fname in os.listdir(dir_path):
        match = re.match(pattern, fname)
        if match:
            try:
                ver = int(match.group(1))
                if ver > max_ver:
                    max_ver = ver
            except ValueError:
                continue
    return max_ver + 1

# File patterns and paths
json_pattern = rf"^{re.escape(base_name)}-new(\d+)\.json$"
rank_static = os.path.join(rarity_dir, f"{base_name}-rarity-rankings.txt")
stats_static = os.path.join(rarity_dir, f"{base_name}-rarity-statistics.txt")

new_json_ver = next_version(metadata_dir, json_pattern)
new_rank_ver = next_version(rarity_dir, rf"^{re.escape(base_name)}-rarity-rankings-new(\d+)\.txt$") if os.path.exists(rank_static) else None
new_stats_ver = next_version(rarity_dir, rf"^{re.escape(base_name)}-rarity-statistics-new(\d+)\.txt$") if os.path.exists(stats_static) else None

# Define output file paths
output_meta = os.path.join(metadata_dir, f"{base_name}-new{new_json_ver}.json")
output_rank = os.path.join(rarity_dir, f"{base_name}-rarity-rankings-new{new_rank_ver}.txt") if new_rank_ver else rank_static
output_stats = os.path.join(rarity_dir, f"{base_name}-rarity-statistics-new{new_stats_ver}.txt") if new_stats_ver else stats_static

# Debug output
print(f"\nOutput files will be created at:")
print(f"  Metadata:   {output_meta}")
print(f"  Rankings:   {output_rank}")
print(f"  Statistics: {output_stats}")

# Load and validate data
with open(input_meta, 'r', encoding='utf-8') as f:
    nft_data = json.load(f)

# Flexible data extraction
if isinstance(nft_data, list):
    items = nft_data
elif 'collection_items' in nft_data:
    items = nft_data['collection_items']
elif 'items' in nft_data:
    items = nft_data['items']
else:
    items = []

if not items:
    print("No items found in metadata.")
    sys.exit(1)

total_retrieved = len(items)

# Detect which attribute key is used in the JSON
attr_key = None
if items:
    if 'item_attributes' in items[0]:
        attr_key = 'item_attributes'
    elif 'attributes' in items[0]:
        attr_key = 'attributes'
    else:
        print("Error: Could not detect attribute key in items. Expected 'attributes' or 'item_attributes'.")
        sys.exit(1)
    print(f"Detected attribute key: '{attr_key}'")

# Collection size validation
if total_retrieved > 0:
    print(f"Retrieved {total_retrieved} items. Version: new{new_json_ver}")

# Interactive rank override input
print("\n" + "="*60)
print("RANK OVERRIDE OPTIONS")
print("="*60)
print("You can specify items to receive hardcoded ranks (by index number).")
print("Formats supported: comma-separated (1,5,10), space-separated (1 5 10),")
print("or ranges (1-5, 10-15). You can combine formats (e.g., '1-5,10,15').")
print("Press Enter to skip if no overrides are needed.\n")

rank_0_input = input("Enter index numbers for items to assign RANK 0 (press Enter to skip): ").strip()
rank_0_indices = parse_index_input(rank_0_input)

rank_1_input = input("Enter index numbers for items to assign RANK 1 (press Enter to skip): ").strip()
rank_1_indices = parse_index_input(rank_1_input)

# Validate indices exist in the collection
valid_indices = {item.get('index') for item in items if 'index' in item}
invalid_rank_0 = rank_0_indices - valid_indices
invalid_rank_1 = rank_1_indices - valid_indices

if invalid_rank_0:
    print(f"Warning: The following rank 0 indices don't exist in the collection: {sorted(invalid_rank_0)}")
    rank_0_indices = rank_0_indices & valid_indices

if invalid_rank_1:
    print(f"Warning: The following rank 1 indices don't exist in the collection: {sorted(invalid_rank_1)}")
    rank_1_indices = rank_1_indices & valid_indices

# Check for overlaps
overlap = rank_0_indices & rank_1_indices
if overlap:
    print(f"Warning: The following indices were specified for both rank 0 and rank 1: {sorted(overlap)}")
    print("They will be assigned to rank 0 (rank 0 takes priority).")
    rank_1_indices = rank_1_indices - overlap

# Determine starting rank for regular items
if rank_0_indices and rank_1_indices:
    regular_items_start_rank = 2
    print(f"\n{len(rank_0_indices)} items will be assigned rank 0.")
    print(f"{len(rank_1_indices)} items will be assigned rank 1.")
elif rank_0_indices:
    regular_items_start_rank = 1
    print(f"\n{len(rank_0_indices)} items will be assigned rank 0.")
elif rank_1_indices:
    regular_items_start_rank = 2
    print(f"\n{len(rank_1_indices)} items will be assigned rank 1.")
else:
    regular_items_start_rank = 1
    print("\nNo rank overrides specified. Using standard rarity calculation.")

if rank_0_indices:
    print(f"Rank 0 indices: {sorted(rank_0_indices)}")
if rank_1_indices:
    print(f"Rank 1 indices: {sorted(rank_1_indices)}")
if rank_0_indices or rank_1_indices:
    print(f"Regular items will start at rank {regular_items_start_rank}.")

# Build index to ID mapping for rank overrides
index_to_id = {}
for item in items:
    idx = item.get('index')
    item_id = item.get('ethscription_id', item.get('id', ''))
    if idx and item_id:
        index_to_id[idx] = item_id

print(f"\nCalculating rarity...")

# Build set of hardcoded rank item IDs for exclusion from trait frequency calculations
hardcoded_rank_ids = set()
for idx in rank_0_indices | rank_1_indices:
    if idx in index_to_id:
        hardcoded_rank_ids.add(index_to_id[idx])

if hardcoded_rank_ids:
    print(f"Excluding {len(hardcoded_rank_ids)} hardcoded rank items from trait frequency calculations.")

# Step 3: Calculate Trait Value Frequencies (excluding Featured Artist traits and hardcoded rank items)
trait_value_counts = defaultdict(int)
# Adjust total_items to exclude hardcoded rank items from rarity calculations
total_items = len(items) - len(hardcoded_rank_ids)

# Traits to filter out from the rarity calculations
traits_to_exclude = {"Wisdom/Magic", "Power/Strength", "Speed/Agility"}

for item in items:
    item_id = item.get('ethscription_id', item.get('id', ''))
    
    # Skip items with hardcoded ranks
    if item_id in hardcoded_rank_ids:
        continue
    
    for attr in item.get(attr_key, []):
        trait_type = attr.get('trait_type')  # Ensure 'trait_type' exists
        trait_value = attr.get('value')      # Ensure 'value' exists
        # Skip Featured Artist trait type and metadata traits to avoid inflating rarity scores
        if (trait_type and trait_value and 
            trait_type not in traits_to_exclude and 
            trait_type.lower() not in ['rarity', 'rank'] and 
            trait_type != 'Featured Artist'):
            trait_value_counts[(trait_type, trait_value)] += 1

# Step 4: Calculate Rarity Score for Each Trait
def calculate_rarity_score(trait_type, trait_value):
    frequency = trait_value_counts[(trait_type, trait_value)]
    if frequency == 0:
        # Trait only exists in hardcoded rank items, return 0 (won't affect scoring)
        return 0
    return total_items / frequency  # Rarity Score formula

# Step 5: Calculate Total Rarity Scores and Rankings
# Dynamically identify Featured Artists by their trait
def is_featured_artist(item):
    """Check if an item is a Featured Artist based on its traits"""
    for attr in item.get(attr_key, []):
        if attr.get('trait_type') == 'Featured Artist':
            return True
    return False

nft_rankings = []

for nft in items:
    nft_id = nft.get('ethscription_id', nft.get('id', ''))
    
    # Skip rarity calculation for hardcoded rank items
    if nft_id in hardcoded_rank_ids:
        # Add to rankings with a placeholder score (will use hardcoded rank later)
        # Use first trait as placeholder for "rarest trait"
        nft_traits = nft.get(attr_key, [])
        placeholder_trait = ('Hardcoded Rank', 'N/A', 0)
        if nft_traits:
            first_trait = nft_traits[0]
            placeholder_trait = (first_trait.get('trait_type', 'N/A'), first_trait.get('value', 'N/A'), 0)
        nft_rankings.append((nft.get('name', ''), 0, placeholder_trait, nft))
        continue
    
    nft_traits = nft.get(attr_key, [])
    total_rarity_score = 0  # Initialize total rarity score for the NFT
    rarity_scores = []  # Store rarity scores for each trait for later retrieval

    for trait in nft_traits:
        trait_type = trait.get('trait_type')  # Ensure 'trait_type' exists
        trait_value = trait.get('value')      # Ensure 'value' exists
        # Skip excluded traits, metadata traits and Featured Artist traits in scoring
        if (trait_type in traits_to_exclude or 
            trait_type.lower() in ['rarity', 'rank'] or 
            trait_type == 'Featured Artist'):  
            continue
        
        rarity_score = calculate_rarity_score(trait_type, trait_value)
        total_rarity_score += rarity_score  # Sum all trait rarity scores for the NFT
        rarity_scores.append((trait_type, trait_value, rarity_score))  # Store for later

    if rarity_scores:
        # Find the rarest trait based on the highest rarity score
        rarest_trait = max(rarity_scores, key=lambda x: x[2])
        nft_rankings.append((nft.get('name', ''), total_rarity_score, rarest_trait, nft))
    elif is_featured_artist(nft):
        # Featured Artists get added with special handling (they have no calculated rarity scores)
        # Find their Featured Artist trait to display as "rarest"
        featured_trait = None
        for trait in nft.get(attr_key, []):
            if trait.get('trait_type') == 'Featured Artist':
                featured_trait = ('Featured Artist', trait.get('value'), 999999)  # High dummy score for sorting
                break
        if featured_trait:
            nft_rankings.append((nft.get('name', ''), 999999, featured_trait, nft))  # High score to rank at top

# Step 6: Order NFTs by Total Rarity Score (Descending)
nft_rankings.sort(key=lambda x: x[1], reverse=True)

# Step 7: Save Rarity Rankings to a File

# Initialize ranks dictionary with hardcoded overrides
ranked_nfts = []
ranks = {}

# Assign rank 0 to specified items
rank_0_ids = {index_to_id[idx] for idx in rank_0_indices if idx in index_to_id}
for item_id in rank_0_ids:
    ranks[item_id] = 0

# Assign rank 1 to specified items (if no rank 0 items, or additional rank 1 items)
rank_1_ids = {index_to_id[idx] for idx in rank_1_indices if idx in index_to_id}
for item_id in rank_1_ids:
    ranks[item_id] = 1

# Determine the starting rank for regular items
regular_rank_counter = regular_items_start_rank

for rank, (nft_name, total_rarity_score, rarest_trait, nft_item) in enumerate(nft_rankings, start=1):
    # Calculate the number of digits needed based on collection size
    num_digits = len(str(total_items))
    
    ethscription_id = nft_item.get('ethscription_id', nft_item.get('id', ''))
    
    # Check if this item already has a hardcoded rank (0 or 1)
    if ethscription_id in ranks:
        # Use the hardcoded rank
        formatted_rank = ranks[ethscription_id]
        rank_str = str(formatted_rank).zfill(num_digits)
    else:
        # Assign next available rank for regular items
        formatted_rank = regular_rank_counter
        rank_str = str(regular_rank_counter).zfill(num_digits)
        ranks[ethscription_id] = formatted_rank
        regular_rank_counter += 1

    # Calculate the number of digits needed based on collection size
    num_digits = len(str(total_items))
    
    # Extract the base name and number from the NFT name
    name_parts = nft_name.split("#")
    if len(name_parts) == 2:
        base_name = name_parts[0].strip()
        try:
            number = int(name_parts[1])
            formatted_nft_name = f"{base_name} #{number:0{num_digits}d}"
        except ValueError:
            # If we can't parse the number, use the original name
            formatted_nft_name = nft_name
    else:
        # If the name doesn't follow the "#" format, use it as is
        formatted_nft_name = nft_name

    link = f"https://ethscriptions.com/ethscriptions/{ethscription_id}"

    # Extract the rarest trait and its value
    rarest_trait_type, rarest_trait_value, _ = rarest_trait

    # Output the rarest trait (as requested)
    ranked_nfts.append((rank_str, formatted_nft_name, rarest_trait_type, rarest_trait_value, link))

# Sort NFTs by rank to ensure "00001" is at the top
ranked_nfts.sort(key=lambda x: x[0])

# Update metadata with rarity values
for item in items:
    eid = item.get('ethscription_id', item.get('id'))
    
    # Get rank from our ranks dictionary
    rank_val = ranks.get(eid)
    
    if rank_val is None:
        continue
    
    # Remove any existing rank trait
    item[attr_key] = [attr for attr in item.get(attr_key, []) 
                             if attr.get('trait_type', '').lower() != 'rank']
    
    # Update or add rarity trait
    updated = False
    for attr in item.get(attr_key, []):
        if attr.get('trait_type', '').lower() == 'rarity':
            attr['value'] = rank_val
            updated = True
            break
    
    if not updated:
        item.setdefault(attr_key, []).append({'trait_type': 'Rarity', 'value': rank_val})

# Write updated metadata
with open(output_meta, 'w', encoding='utf-8') as f:
    json.dump(nft_data, f, ensure_ascii=False, indent=4)
print(f"Wrote updated metadata to {output_meta}")

# Write the rankings to file
with open(output_rank, 'w', encoding='utf-8') as txt_file:
    for formatted_rank, formatted_nft_name, rarest_trait_type, rarest_trait_value, link in ranked_nfts:
        text = f"Rank {formatted_rank} - {formatted_nft_name} | Rarest trait = {rarest_trait_type} - {rarest_trait_value} | Link: {link}\n"
        txt_file.write(text)
print(f"Wrote rankings to {output_rank}")

# Step 8: Calculate and Print Rarity Scores for Traits
# Collect Featured Artist traits separately (for display purposes only)
featured_artist_traits = defaultdict(int)

for item in items:
    for attr in item.get(attr_key, []):
        trait_type = attr.get('trait_type')
        trait_value = attr.get('value')
        
        if trait_type == 'Featured Artist':
            # Count Featured Artist traits for display only
            featured_artist_traits[(trait_type, trait_value)] += 1

# Prepare regular trait entries
regular_trait_entries = []
for (trait_type, trait_value), count in trait_value_counts.items():
    entry = ((trait_type, trait_value), count)
    regular_trait_entries.append(entry)

# Sort regular traits by rarity score descending
regular_trait_entries.sort(key=lambda x: (total_items / x[1] if x[1] else 0), reverse=True)

# Prepare Featured Artist entries for display
featured_entries = []
for (trait_type, trait_value), count in featured_artist_traits.items():
    entry = ((trait_type, trait_value), count)
    featured_entries.append(entry)

# Sort Featured Artist entries by rarity score descending
featured_entries.sort(key=lambda x: (total_items / x[1] if x[1] else 0), reverse=True)

with open(output_stats, 'w', encoding='utf-8') as f:
    if featured_entries:
        f.write("-------------------------------------------------------------\n")
        f.write("Rarity Scores for Traits (Featured Artist traits shown separately):\n")
        f.write("-------------------------------------------------------------\n")
        f.write("NOTE: Featured Artist traits are excluded from rarity calculations\n")
        f.write("to prevent inflation of common trait rarity scores.\n\n")
        f.write("FEATURED ARTIST TRAITS (not included in rarity calculations):\n")
        for (trait_type, trait_value), count in featured_entries:
            f.write(f"{trait_type} - {trait_value} | frequency = {count} / {total_items} (excluded from scoring)\n")
        f.write("\nREGULAR TRAITS (used in rarity calculations):\n")
    else:
        f.write("-------------------------------------------------------------\n")
        f.write("Rarity Scores for Traits:\n")
        f.write("-------------------------------------------------------------\n")
    
    # Then regular traits (these are actually used in calculations)
    for (trait_type, trait_value), count in regular_trait_entries:
        rarity_score = calculate_rarity_score(trait_type, trait_value)
        f.write(f"{trait_type} - {trait_value} | rarity score = {rarity_score:.2f} | frequency = {count} / {total_items}\n")

print(f"Wrote statistics to {output_stats}")

print("\n-------------------------------------------------------------\nRarity Scores for Traits (sorted by most rare to least rare):\n-------------------------------------------------------------")
if featured_entries:
    print("NOTE: Featured Artist traits are excluded from calculations")
for trait, count in sorted(trait_value_counts.items(), key=lambda x: (x[1] / total_items)):
    trait_type, trait_value = trait
    
    rarity_score = calculate_rarity_score(trait_type, trait_value)
    frequency = count
    
    print(f"{trait_type} - {trait_value} | rarity score = {rarity_score:.2f} | frequency = {frequency} / {total_items}")
    
print("\nThe terminal output of this script is tracked as a text file here: https://github.com/alperaym/darknezz-ethscription/blob/main/rarity/darknezz-rarity-statistics.txt")
print("\nThe full rankings text file that this script produces is tracked here: https://github.com/alperaym/darknezz-ethscription/blob/main/rarity/darknezz-rarity-rankings.txt")
print("\ns/o to Snepsid: https://github.com/Snepsid and Nakamingos: https://x.com/Nakamingos as well as VirtualAlaska: https://github.com/VirtualAlaska and mfpurrs: https://x.com/mfpurrs")