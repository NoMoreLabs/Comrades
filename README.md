# Call-Data-Comrades

This repository contains artwork, metadata, rarity analysis, and trait statistics for the Call Data Comrades collection on Ethscriptions. The collection includes 9,959 total comrades across different tiers: 9,819 generic, 52 honorary, 49 legends, and 21 nyan comrades.

## Repository Structure

- **art/**
  - `comrades_32px/`: 32x32 pixel comrade images with backgrounds
    - `generic/` (9,819 images), `honorary/` (52 images), `legends/` (49 images), `nyan/` (21 images)
  - `comrades_32px_noBG/`: 32x32 pixel comrade images without backgrounds
  - `comrades_800px/`: 800x800 pixel comrade images with backgrounds
  - `comrades_800px_noBG/`: 800x800 pixel comrade images without backgrounds
  - `comrades_trait_layers/`: Individual trait layer assets organized by category
    - `01_Relics/`, `02_Eyes/`, `03_Mouth/`, `04_Audio Indexer Derivtations/`
    - `05_Head/`, `06_Cloths/`, `07_Skin Stuff/`, `08_Type/`
    - `09_Extras/`, `10_Backgrounds/`, `11_Animated Traits/`

- **metadata/**
  - `call-data-comrades.json`: Metadata for all comrades in the collection.
  - `comrades-grid.png`: Visual grid of all comrades.

- **rarity/**
  - `comrade-rarity.md`: Documentation on rarity methodology and findings.
  - `comrades-attribute-count-analysis.md`: Lists comrades grouped by their attribute count.
  - `comrades-attribute-synergy.json`: Data on attribute synergies.
  - `comrades-rarity-grid.png`: Visual rarity grid.
  - `comrades-rarity-ranks.csv` / `comrades-rarity-ranks.txt`: Rarity rankings for all comrades.
  - `comrades-traits-stats.md`: Detailed trait rarity statistics.

## Contents

- **Artwork**: Complete collection of Comrades images in multiple formats and sizes (32px and 800px), both with and without backgrounds, plus individual trait layers for custom rendering.
- **Metadata**: Comprehensive data for each comrade, including traits and attributes.
- **Rarity Analysis**: In-depth breakdown of attribute counts, trait frequencies, and rarity scores.
- **Trait Statistics**: Frequency and rarity scores for all trait values, grouped by trait type.

## Usage

- Use the artwork files to integrate Call Data Comrades visually into your application, marketplace, or project.
- Access trait layers to create custom combinations or generate new variations.
- Use the metadata files to integrate Call Data Comrades into your application or analysis.
- Reference the rarity and trait stats for rarity-based sorting, filtering, or visualization.

## License

This repository and all its contents are dedicated to the public domain under [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).
