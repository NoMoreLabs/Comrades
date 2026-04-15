# Art

Artwork for all three Comrades collections, provided in multiple resolutions with and without backgrounds.

## Directory Structure

### `call-data-comrades/` — Call Data Comrades (CDC)

9,959 comrades across four tiers: generic (9,819), honorary (54), legends (50), and nyan (21).

| Directory | Resolution | Backgrounds | Subdirectories |
|-----------|-----------|-------------|----------------|
| `cdc_32px/` | 32×32 | Yes | `generic/`, `honorary/`, `legends/`, `nyan/` |
| `cdc_32px_noBG/` | 32×32 | No | `generic/`, `honorary/`, `legends/`, `nyan/` |
| `cdc_800px/` | 800×800 | Yes | `generics/`, `honorary/`, `legends/`, `nyan/` |
| `cdc_800px_noBG/` | 800×800 | No | `generics/`, `honorary/`, `legends/` |

#### Trait Layers (`cdc_trait_layers/`)

Individual PNG trait layer assets for compositing CDC comrades. Organized by category in render order:

| Directory | Category |
|-----------|----------|
| `01_Relics/` | Relics |
| `02_Eyes/` | Eyes |
| `03_Mouth/` | Mouth |
| `04_Audio Indexer Derivations/` | Audio Indexer Derivations |
| `05_Head/` | Head |
| `06_Cloths/` | Cloths |
| `07_Skin Stuff/` | Skin Stuff |
| `08_Type/` | Type |
| `09_Extras/` | Extras |
| `10_Backgrounds/` | Backgrounds |
| `11_Animated Traits/` | Animated Traits |

### `comrades-of-the-dead/` — Comrades of the Dead (COTD)

666 comrades. All files are PNG.

| Directory | Resolution | Backgrounds |
|-----------|-----------|-------------|
| `cotd_32px/` | 32×32 | Yes |
| `cotd_32px_noBG/` | 32×32 | No |
| `cotd_800px/` | 800×800 | Yes |
| `cotd_800px_noBG/` | 800×800 | No |

### `pizza-comrades/` — Pizza Comrades (PC)

2,222 comrades. Primarily PNG with some special comrades in SVG, AVIF, and HTML formats.

| Directory | Resolution | Backgrounds |
|-----------|-----------|-------------|
| `pc_64px/` | 64×64 | Yes |
| `pc_64px_noBG/` | 64×64 | No |
| `pc_768px/` | 768×768 | Yes |
| `pc_768px_noBG/` | 768×768 | No |

## File Naming

Files follow the pattern `Name#ID.ext`:

- **Numbered comrades**: `Comrade#1.png`, `Pizza Comrade#42.png`
- **Named comrades**: `Lord Hexley#15.png`, `General Snepsid#10.png`

## File Formats

| Format | Usage |
|--------|-------|
| PNG | Standard raster images (vast majority) |
| SVG | Vector graphics (select Pizza Comrades) |
| AVIF | Modern compressed format (select Pizza Comrades) |
| HTML | Web-based art (select Pizza Comrades) |
