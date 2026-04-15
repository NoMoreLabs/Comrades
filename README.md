# Comrades

This repository contains artwork, metadata, rarity analysis, and trait statistics for collections in the Comrades universe: **Call Data Comrades** (CDC), **Comrades of the Dead** (COTD), and **Pizza Comrades** (PC). CDC and COTD are Ethscriptions collections; PC is an Ordinals collection.

## Collections

### Call Data Comrades (CDC)
- **9,959 total comrades** across different tiers:
  - 9,819 generic
  - 54 honorary
  - 50 legends
  - 21 nyan comrades

### Comrades of the Dead (COTD)
- **666 total comrades**

### Pizza Comrades (PC)
- **2,222 total comrades**
- Art merger collaboration between Boozy's Pizza Ninjas and McHexley's Call Data Comrades, baked into the NoMoreLabs universe.

## Repository Structure

- **art/**
  - **`call-data-comrades/`** — Call Data Comrades (CDC):
    - `cdc_32px/`: 32x32 pixel comrade images with backgrounds
      - `generic/` (9,819 images), `honorary/` (54 images), `legends/` (50 images), `nyan/` (21 images)
    - `cdc_32px_noBG/`: 32x32 pixel comrade images without backgrounds
    - `cdc_800px/`: 800x800 pixel comrade images with backgrounds
    - `cdc_800px_noBG/`: 800x800 pixel comrade images without backgrounds
    - `cdc_trait_layers/`: Individual trait layer assets organized by category
      - `01_Relics/`, `02_Eyes/`, `03_Mouth/`, `04_Audio Indexer Derivations/`
      - `05_Head/`, `06_Cloths/`, `07_Skin Stuff/`, `08_Type/`
      - `09_Extras/`, `10_Backgrounds/`, `11_Animated Traits/`
  - **`comrades-of-the-dead/`** — Comrades of the Dead (COTD):
    - `cotd_32px/`: 32x32 pixel comrade images (666 images)
    - `cotd_32px_noBG/`: 32x32 pixel comrade images without backgrounds (666 images)
    - `cotd_800px/`: 800x800 pixel comrade images (666 images)
    - `cotd_800px_noBG/`: 800x800 pixel comrade images without backgrounds (666 images)
  - **`pizza-comrades/`** — Pizza Comrades (PC):
    - `pc_64px/`: 64x64 pixel comrade images (2,222 images)
    - `pc_64px_noBG/`: 64x64 pixel comrade images without backgrounds (2,222 images)
    - `pc_768px/`: 768x768 pixel comrade images (2,222 images)
    - `pc_768px_noBG/`: 768x768 pixel comrade images without backgrounds (2,222 images)

- **metadata/**
  - `call-data-comrades.json`: Metadata for all Call Data Comrades (CDC).
  - `comrades-of-the-dead.json`: Metadata for all Comrades of the Dead (COTD).
  - `pizza-comrades.json`: Metadata for all Pizza Comrades (PC).
  - `pizza-comrades-collection-info.json`: Collection-level metadata for Pizza Comrades.
  - `pizza-comrades-gallery.yaml`: Pizza Comrades gallery inscription metadata.
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

- **Artwork**: 
  - Complete collection of Call Data Comrades images in multiple formats and sizes (32px and 800px), both with and without backgrounds, plus individual trait layers for custom rendering.
  - Comrades of the Dead images in 32px and 800px formats, both with and without backgrounds.
  - Pizza Comrades images in 64px and 768px formats, both with and without backgrounds.
- **Metadata**: Comprehensive data for each comrade across CDC, COTD, and PC, including traits and attributes.
- **Rarity Analysis**: In-depth breakdown of attribute counts, trait frequencies, and rarity scores for supported collections.
- **Trait Statistics**: Frequency and rarity scores for trait values, grouped by trait type.

## Naming Convention

To keep files organized and easily identifiable:
- **`cdc-`** prefix: Call Data Comrades (9,962 items)
- **`cotd-`** prefix: Comrades of the Dead (666 items)
- **`pc-`** prefix: Pizza Comrades (2,222 items)

## Usage

- Use the artwork files to integrate Call Data Comrades visually into your application, marketplace, or project.
- Access trait layers to create custom combinations or generate new variations.
- Use the metadata files to integrate comrades from any collection into your application or analysis.
- Reference the rarity and trait stats where available for rarity-based sorting, filtering, or visualization.

## License

This repository and all its contents are dedicated to the public domain under [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/).
