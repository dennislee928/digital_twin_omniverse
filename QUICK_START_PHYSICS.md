# Physics Simulation Quick Start

## Enable Physics Extension

### Method 1: Using Setup Script (Recommended)

```bash
./scripts/setup_physics.sh
```

### Method 2: Manual Configuration

1. **Open .kit file** in VS Code
2. **Add PhysX extension**:
   ```toml
   [dependencies]
   "omni.physx.bundle" = {}
   ```
3. **Disable Fabric Scene Delegate**:
   ```toml
   [settings.app.usdrt]
   useFabricSceneDelegate = false
   ```
4. **Save and rebuild** application

## Setup Conveyor Belt Physics

### 1. Add Assets

- Load **Factory_Lite.usd**
- Add **conveyor belts** (search "conveyor" in NVIDIA Assets)
- Add **boxes** (search "cardbox")
- Place 3 boxes on topmost belt

### 2. Setup Boxes

1. **Select all 3 boxes**
2. Property panel > **+Add** > **Physics > Rigid Body with Colliders Preset**

### 3. Setup Conveyor Belt

1. **Select belt mesh only** (not entire conveyor)
   - In Stage window, expand conveyor
   - Select Mesh asset (e.g., `SM_ConveyorBelt_A29_Belt01_01`)

2. **Add Physics preset**:
   - Property panel > **+Add** > **Physics > Rigid Body with Colliders Preset**

3. **Configure Physics section**:
   - **Kinematic Enabled**: `On`
   - **Velocities in Local Space**: `On`

4. **Add Surface Velocity**:
   - Property panel > **+Add** > **Physics > Surface Velocity**
   - Set **Surface Linear Velocity Y**: `-20`

### 4. Test Simulation

1. **Save scene**
2. **Click Timeline** button (lower right)
3. **Click Play** button
4. Boxes should move along belt

### 5. Fix Direction (if needed)

If belt moves backward:
- Change **Surface Linear Velocity Y** to `-20` (negative)
- Save and test again

## Quick Reference

### Physics Settings

- **Rigid Body with Colliders Preset**: For boxes and belt mesh
- **Kinematic Enabled**: For moving belts
- **Velocities in Local Space**: Use belt's local axis
- **Surface Linear Velocity Y**: `-20` for forward motion

### Common Issues

- **Box not moving**: Place box above belt surface
- **Wrong direction**: Use negative velocity value
- **No collision**: Ensure physics on Mesh, not Xform

## Detailed Guides

- [Physics Simulation Guide](PHYSICS_SIMULATION_GUIDE.md)
- [Physics Best Practices](PHYSICS_BEST_PRACTICES.md)
- [Physics Setup Example](examples/physics_setup_example.py)
