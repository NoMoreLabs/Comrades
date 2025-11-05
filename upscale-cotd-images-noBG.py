import os
from PIL import Image

# Define paths
script_dir = os.path.dirname(os.path.abspath(__file__))
art_dir = os.path.join(script_dir, 'art')
input_dir = os.path.join(art_dir, 'cotd_32px_noBG')
output_dir = os.path.join(art_dir, 'cotd_800px_noBG')

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get all PNG files from input directory
png_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.png')]
png_files.sort(key=lambda x: int(x.split('.')[0]))  # Sort numerically

total_files = len(png_files)
print(f"Found {total_files} images to upscale from 32px to 800px (no background)")
print(f"Input directory: {input_dir}")
print(f"Output directory: {output_dir}")
print("-" * 60)

# Process each image
for i, filename in enumerate(png_files, 1):
    input_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, filename)
    
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Upscale using NEAREST neighbor to maintain pixel art style
        # This preserves the sharp, pixelated look
        upscaled_img = img.resize((800, 800), Image.NEAREST)
        
        # Save the upscaled image
        upscaled_img.save(output_path, 'PNG')
        
        # Progress indicator
        if i % 50 == 0 or i == total_files:
            print(f"Processed {i}/{total_files} images ({i*100//total_files}%)")
    
    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("-" * 60)
print(f"✓ Successfully upscaled {total_files} images to 800x800px")
print(f"✓ Output saved to: {output_dir}")
