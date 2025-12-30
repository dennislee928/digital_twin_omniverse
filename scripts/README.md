# Scripts Directory

This directory contains utility scripts for setting up and configuring the digital twin application.

## Available Scripts

### Extension Management

- **create_extension.sh** - Create a new extension from template
  ```bash
  ./scripts/create_extension.sh
  ```
  - Interactive script to create new extensions
  - Automatically replaces template variables
  - Creates proper directory structure

### Physics Setup

- **setup_physics.sh** - Configure physics simulation
  ```bash
  ./scripts/setup_physics.sh
  ```
  - Adds PhysX extension to .kit file
  - Disables Fabric Scene Delegate
  - Creates backup of original file
  - Interactive .kit file selection

### Security Scanning

- **scan_extensions.sh** (in project root) - Security scan for Python extensions
  ```bash
  ./scan_extensions.sh
  ```
  - Scans templates/extensions directory
  - Uses Bandit for code security analysis
  - Generates JSON and TXT reports

## Usage Examples

### Create New Extension

```bash
cd /path/to/digital_twin_omniverse
./scripts/create_extension.sh

# Follow prompts:
# - Enter extension name
# - Enter Python module path
```

### Setup Physics

```bash
./scripts/setup_physics.sh

# Script will:
# - Find .kit files
# - Add PhysX extension
# - Disable Fabric Scene Delegate
# - Create backup
```

## Script Requirements

- Bash shell
- Standard Unix utilities (find, grep, sed)
- Python 3.6+ (for Python scripts)

## Related Documentation

- [Extension Development Guide](../EXTENSION_DEVELOPMENT_GUIDE.md)
- [Physics Simulation Guide](../PHYSICS_SIMULATION_GUIDE.md)
