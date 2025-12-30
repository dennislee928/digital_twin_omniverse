# Digital Twin Omniverse Documentation Index

Complete guide index for developing digital twin applications with USD Explorer and Omniverse.

## Getting Started

### Quick Start Guides

- **[Quick Start: Variants](QUICK_START_VARIANTS.md)** - Quick reference for variant exploration
- **[Quick Start: Physics](QUICK_START_PHYSICS.md)** - Quick reference for physics simulation setup

### Core Concepts

- **[USD Exploration Guide](USD_EXPLORATION_GUIDE.md)** - Understanding OpenUSD file structure
- **[USD Exploration Guide (EN)](USD_EXPLORATION_GUIDE_EN.md)** - English version
- **[USD Conversion Guide](USD_CONVERSION_GUIDE.md)** - Converting USD to USDA format
- **[Conversion Methods](CONVERSION_METHODS.md)** - All methods for converting USD files
- **[Kit Environment Conversion](KIT_ENVIRONMENT_CONVERSION.md)** - Converting in Omniverse Kit environment

## Asset Management

### Importing Assets

- **[Import Assets Guide](IMPORT_ASSETS_GUIDE.md)** - Importing assets from NVIDIA Assets library
- **[Import Assets Guide (EN)](IMPORT_ASSETS_GUIDE_EN.md)** - English version

### Working with Assets

- **[Duplicate Assets Guide](DUPLICATE_ASSETS_GUIDE.md)** - Methods for duplicating assets
- **[Edit USD Files Guide](EDIT_USD_FILES_GUIDE.md)** - Editing USD files directly

## Variants

- **[Variant Presenter Guide](VARIANT_PRESENTER_GUIDE.md)** - Setting up and using Variant Presenter
- **[Variant Presenter Guide (EN)](VARIANT_PRESENTER_GUIDE_EN.md)** - English version
- **[Duplicate Assets Preview](DUPLICATE_ASSETS_PREVIEW.md)** - Preview of variant concepts

## Review Mode Extensions

### Individual Extension Guides

- **[Measure Extension Guide](MEASURE_EXTENSION_GUIDE.md)** - Measuring distances and angles
- **[Markup Extension Guide](MARKUP_EXTENSION_GUIDE.md)** - Adding annotations and comments
- **[Waypoint Extension Guide](WAYPOINT_EXTENSION_GUIDE.md)** - Saving and navigating views
- **[Section Extension Guide](SECTION_EXTENSION_GUIDE.md)** - Creating section views

### Comprehensive Guide

- **[Review Extensions Guide](REVIEW_EXTENSIONS_GUIDE.md)** - Complete guide to all Review mode extensions

## Physics Simulation

- **[Physics Simulation Guide](PHYSICS_SIMULATION_GUIDE.md)** - Complete physics setup guide
- **[Physics Best Practices](PHYSICS_BEST_PRACTICES.md)** - Best practices for physics simulations

## Extension Development

- **[Extension Development Guide](EXTENSION_DEVELOPMENT_GUIDE.md)** - Developing custom extensions

## Security

- **[Snyk Notes](SNYK_NOTES.md)** - Snyk configuration and Omniverse-specific scanning tools
- **[Snyk Notes (EN)](SNYK_NOTES_EN.md)** - English version
- **[Security Fixes](SECURITY_FIXES.md)** - Security vulnerability fixes summary

## Documentation Structure

```
docs/
├── INDEX.md (this file)
├── Getting Started/
│   ├── QUICK_START_VARIANTS.md
│   ├── QUICK_START_PHYSICS.md
│   ├── USD_EXPLORATION_GUIDE.md
│   └── USD_CONVERSION_GUIDE.md
├── Asset Management/
│   ├── IMPORT_ASSETS_GUIDE.md
│   ├── DUPLICATE_ASSETS_GUIDE.md
│   └── EDIT_USD_FILES_GUIDE.md
├── Variants/
│   └── VARIANT_PRESENTER_GUIDE.md
├── Review Extensions/
│   ├── MEASURE_EXTENSION_GUIDE.md
│   ├── MARKUP_EXTENSION_GUIDE.md
│   ├── WAYPOINT_EXTENSION_GUIDE.md
│   ├── SECTION_EXTENSION_GUIDE.md
│   └── REVIEW_EXTENSIONS_GUIDE.md
├── Physics/
│   ├── PHYSICS_SIMULATION_GUIDE.md
│   └── PHYSICS_BEST_PRACTICES.md
├── Development/
│   └── EXTENSION_DEVELOPMENT_GUIDE.md
└── Security/
    ├── SNYK_NOTES.md
    └── SECURITY_FIXES.md
```

## Code Examples

See the [examples/](../examples/) directory for code examples:

- `custom_extension_example.py` - Custom extension development
- `extension_integration_example.py` - Extension integration
- `physics_setup_example.py` - Physics simulation setup
- `extension_config_example.kit` - Extension configuration
- `physics_config_example.kit` - Physics configuration

## Scripts

See the [scripts/](../scripts/) directory for utility scripts:

- `create_extension.sh` - Create new extensions
- `setup_physics.sh` - Configure physics simulation
- `scan_extensions.sh` - Security scanning (in project root)

## Learning Path

### Beginner

1. Start with [USD Exploration Guide](USD_EXPLORATION_GUIDE.md)
2. Learn to [Import Assets](IMPORT_ASSETS_GUIDE.md)
3. Explore [Variants](VARIANT_PRESENTER_GUIDE.md)

### Intermediate

1. Use [Review Mode Extensions](REVIEW_EXTENSIONS_GUIDE.md)
2. Learn [Physics Simulation](PHYSICS_SIMULATION_GUIDE.md)
3. [Edit USD Files](EDIT_USD_FILES_GUIDE.md) directly

### Advanced

1. [Develop Custom Extensions](EXTENSION_DEVELOPMENT_GUIDE.md)
2. Integrate multiple extensions
3. Optimize physics simulations

## Related Resources

- [Omniverse Documentation](https://docs.omniverse.nvidia.com/)
- [OpenUSD Documentation](https://openusd.org/)
- [NVIDIA Omniverse](https://www.nvidia.com/en-us/omniverse/)
