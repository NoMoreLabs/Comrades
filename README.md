# Call-Data-Comrades

This repository contains artwork, metadata, rarity analysis, and trait statistics for two Ethscriptions collections: **Call Data Comrades** (CDC) and **Comrades of the Dead** (COTD).

## Collections

### Call Data Comrades (CDC)
- **9,959 total comrades** across different tiers:
  - 9,819 generic
  - 52 honorary
  - 49 legends
  - 21 nyan comrades

### Comrades of the Dead (COTD)
- **666 total comrades**

## Repository Structure

- **art/**
  - `comrades_32px/`: 32x32 pixel comrade images with backgrounds (CDC)
    - `generic/` (9,819 images), `honorary/` (52 images), `legends/` (49 images), `nyan/` (21 images)
  - `comrades_32px_noBG/`: 32x32 pixel comrade images without backgrounds (CDC)
  - `comrades_800px/`: 800x800 pixel comrade images with backgrounds (CDC)
  - `comrades_800px_noBG/`: 800x800 pixel comrade images without backgrounds (CDC)
  - `comrades_trait_layers/`: Individual trait layer assets organized by category (CDC)
    - `01_Relics/`, `02_Eyes/`, `03_Mouth/`, `04_Audio Indexer Derivtations/`
    - `05_Head/`, `06_Cloths/`, `07_Skin Stuff/`, `08_Type/`
    - `09_Extras/`, `10_Backgrounds/`, `11_Animated Traits/`

- **metadata/**
  - `call-data-comrades.json`: Metadata for all Call Data Comrades (CDC).
  - `comrades-of-the-dead.json`: Metadata for all Comrades of the Dead (COTD).
  - `cdc-grid.png`: Visual grid of all Call Data Comrades.

- **rarity/**
  - Files prefixed with `cdc-`: Call Data Comrades rarity analysis
    - `cdc-rarity.md`: Documentation on rarity methodology and findings.
    - `cdc-attribute-count-analysis.md`: Lists CDC comrades grouped by their attribute count.
    - `cdc-attribute-synergy.json`: Data on attribute synergies.
    - `cdc-rarity-grid.png`: Visual rarity grid.
    - `cdc-rarity-ranks.csv` / `cdc-rarity-ranks.txt`: Rarity rankings for all CDC comrades.
    - `cdc-traits-stats.md`: Detailed trait rarity statistics.
  - Files prefixed with `cotd-`: Comrades of the Dead rarity analysis
    - `cotd-rarity-rankings.txt`: Rarity rankings for all COTD comrades.
    - `cotd-rarity-statistics.txt`: Detailed trait rarity statistics.

## Contents

- **Artwork**: Complete collection of Call Data Comrades images in multiple formats and sizes (32px and 800px), both with and without backgrounds, plus individual trait layers for custom rendering.
- **Metadata**: Comprehensive data for each comrade in both collections (CDC and COTD), including traits and attributes.
- **Rarity Analysis**: In-depth breakdown of attribute counts, trait frequencies, and rarity scores for both collections.
- **Trait Statistics**: Frequency and rarity scores for all trait values, grouped by trait type.

## Naming Convention

To keep files organized and easily identifiable:
- **`cdc-`** prefix: Call Data Comrades (9,959 items)
- **`cotd-`** prefix: Comrades of the Dead (666 items)

## Usage

- Use the artwork files to integrate Call Data Comrades visually into your application, marketplace, or project.
- Access trait layers to create custom combinations or generate new variations.
- Use the metadata files to integrate comrades from either collection into your application or analysis.
- Reference the rarity and trait stats for rarity-based sorting, filtering, or visualization.

## License

This repository and all its contents are dedicated to the public domain under [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).
