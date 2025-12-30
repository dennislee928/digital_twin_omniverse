# Physics Simulation Best Practices

This document outlines best practices for setting up and using physics simulations in digital twin applications.

## Configuration

### Extension Setup

1. **Always disable Fabric Scene Delegate** when using PhysX
   ```toml
   [settings.app.usdrt]
   useFabricSceneDelegate = false
   ```

2. **Add PhysX bundle** to dependencies
   ```toml
   [dependencies]
   "omni.physx.bundle" = {}
   ```

3. **Use automation scripts** to avoid configuration errors
   ```bash
   ./scripts/setup_physics.sh
   ```

## Asset Preparation

### SimReady Assets

- **Use SimReady assets** from NVIDIA Assets library
- SimReady assets are:
  - Built to real-world scale
  - Properly aligned with Z-up pivot
  - Ready for physics simulation

### Asset Scaling

- ✅ **Uniform scaling** is safe for physics
- ❌ **Non-uniform scaling** (one or two axes) may cause unpredictable behavior
- Always test scaled assets in simulation

### Asset Placement

- **Place objects above surfaces** when possible
- Objects embedded in surfaces may not collide properly
- Let gravity bring objects into contact for reliable collision detection

## Physics Setup

### Rigid Bodies

1. **Use Rigid Body with Colliders Preset** for most objects
   - Provides both rigid body and collision properties
   - Ensures proper collision detection

2. **Apply to Mesh assets**, not Xform assets
   - Physics must be on the actual geometry
   - Xform parents won't have collision properties

### Conveyor Belts

1. **Select only the belt mesh**, not the entire conveyor
   - Physics should be on the moving part only
   - Reduces unnecessary computation

2. **Use Kinematic Enabled** for moving belts
   - Allows continuous motion
   - Imparts movement to contacting objects

3. **Use Velocities in Local Space**
   - Uses belt's local coordinate system
   - Easier to configure direction

4. **Use Surface Linear Velocity** instead of Linear Velocity
   - Works on dynamic bodies
   - More reliable for conveyor systems

5. **Check axis direction**
   - Green axis (Y) typically points along belt
   - Use negative values to reverse direction

### Velocity Configuration

- **Test direction** before finalizing values
- **Start with small values** and increase as needed
- **Use negative values** for opposite direction
- Typical values: -20 to -50 units per second

## Simulation Testing

### Initial Testing

1. **Save scene** before first simulation
   - Allows reset to original positions
   - Easier to iterate on settings

2. **Test one object at a time**
   - Start with single box on single belt
   - Add complexity gradually

3. **Check collision detection**
   - Objects should not pass through each other
   - Adjust Colliders Approximation if needed

### Troubleshooting

#### Objects Not Moving

- Check if physics is applied to correct prim (Mesh, not Xform)
- Verify objects are above surface, not embedded
- Check Kinematic Enabled is on for moving parts

#### Wrong Direction

- Verify axis orientation (check pivot point colors)
- Use negative velocity to reverse direction
- Test with small values first

#### Objects Falling Through

- Ensure Colliders are properly configured
- Check Colliders Approximation settings
- Verify physics is on Mesh assets

#### Unpredictable Behavior

- Check for non-uniform scaling
- Verify real-world scale is maintained
- Test with SimReady assets first

## Performance Optimization

### Efficient Setup

1. **Apply physics only where needed**
   - Don't apply to static objects unnecessarily
   - Use kinematic for moving parts

2. **Optimize collision geometry**
   - Use appropriate Colliders Approximation
   - Simpler shapes = better performance

3. **Limit active objects**
   - Too many physics objects can slow simulation
   - Use instancing for repeated objects

### Stage Settings

Access via **Window > Physics Stage Settings**:

- **Gravity**: Adjust for different environments
- **Solver iterations**: Balance accuracy vs performance
- **Fixed time step**: Control simulation speed
- **Max sub-steps**: Handle fast-moving objects

## Use Case Patterns

### Conveyor Belt Systems

1. Setup belts with kinematic + surface velocity
2. Place boxes above belt surface
3. Test single belt first, then add connections
4. Add containers with appropriate collision settings

### Falling Objects

1. Place objects in air above ground
2. Apply rigid body physics
3. Let gravity handle motion
4. Adjust restitution for bounce behavior

### Robotics Simulation

1. Setup robot with appropriate physics
2. Configure collision for robot parts
3. Test pick-and-place scenarios
4. Validate collision avoidance

### Container Catching

1. Apply physics to container
2. Adjust Colliders Approximation
3. Test box entry angles
4. Fine-tune container position

## Common Patterns

### Pattern 1: Simple Conveyor

```python
# Setup belt
ConveyorBeltSetup.setup_conveyor_belt(
    belt_path="/World/Belt/Mesh",
    velocity_y=-20.0
)

# Setup boxes
BoxPhysicsSetup.setup_multiple_boxes([
    "/World/Box1",
    "/World/Box2",
    "/World/Box3"
])
```

### Pattern 2: Multi-Belt System

```python
# Setup all belts
belt_paths = [
    "/World/Belt1/Mesh",
    "/World/Belt2/Mesh",
    "/World/Belt3/Mesh"
]
ConveyorBeltSetup.setup_multiple_belts(belt_paths, velocity_y=-20.0)
```

## Integration with Other Features

### With Markup Extension

- Mark physics simulation areas
- Add comments about simulation settings
- Document expected behavior

### With Waypoint Extension

- Save views of simulation states
- Create waypoints at key simulation moments
- Document simulation progression

### With Measure Extension

- Measure distances for physics setup
- Verify object spacing
- Validate simulation scale

## Documentation

### Scene Documentation

- Document physics settings in scene
- Note velocity values and directions
- Record any custom configurations

### Testing Documentation

- Record test results
- Note any issues and solutions
- Document performance characteristics

## Related Resources

- [Physics Simulation Guide](PHYSICS_SIMULATION_GUIDE.md)
- [Physics Setup Example](examples/physics_setup_example.py)
- [Physics Config Example](examples/physics_config_example.kit)
- [Simulation Documentation](https://docs.omniverse.nvidia.com/)
