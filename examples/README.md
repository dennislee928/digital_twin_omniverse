# Examples Directory

This directory contains example code for extension development, configuration, and physics simulation.

## Configuration Examples

- **extension_config_example.kit** - Extension configuration example
  - Shows how to configure extensions in .kit file
  - Includes Review mode extensions configuration
  - Demonstrates extension order control and disabling

- **physics_config_example.kit** - Physics configuration example
  - PhysX extension setup
  - Fabric Scene Delegate configuration
  - Physics stage settings

## Code Examples

### Extension Development

- **custom_extension_example.py** - Custom extension example
  - Basic extension structure
  - USD scene operations
  - Custom command examples
  - Helper functions

- **extension_integration_example.py** - Extension integration example
  - Multi-extension integration methods
  - Extension availability checking
  - Event listener setup
  - Inter-extension communication

### Physics Simulation

- **physics_setup_example.py** - Physics setup example
  - Rigid body configuration
  - Conveyor belt setup
  - Box physics setup
  - Surface velocity configuration
  - Helper classes for physics operations

## Usage

### 1. View Configuration Examples

```bash
# View extension configuration
cat examples/extension_config_example.kit

# View physics configuration
cat examples/physics_config_example.kit
```

### 2. Use Code Examples

```python
# Import and use extension helpers
from examples.custom_extension_example import (
    get_stage,
    create_prim_at_position,
    duplicate_prim
)

# Import and use physics helpers
from examples.physics_setup_example import (
    PhysicsSetupHelper,
    ConveyorBeltSetup,
    BoxPhysicsSetup
)
```

### 3. Reference Integration Examples

```python
# Learn how to integrate multiple extensions
from examples.extension_integration_example import (
    ExtensionIntegrationExample,
    ExtensionCommunication
)
```

## Related Documentation

- [Extension Development Guide](../EXTENSION_DEVELOPMENT_GUIDE.md)
- [Review Extensions Guide](../REVIEW_EXTENSIONS_GUIDE.md)
- [Physics Simulation Guide](../PHYSICS_SIMULATION_GUIDE.md)
- [Physics Best Practices](../PHYSICS_BEST_PRACTICES.md)
