# Physics Simulation Guide

This guide explains how to enable and configure physics simulation in your USD Explorer application for digital twin environments.

## Overview

Digital twins can simulate real-world behaviors based on physics, allowing you to:
- Optimize equipment layout
- Anticipate maintenance needs
- Train robots for tasks (pick-and-place, collision avoidance)
- Simulate product movement
- Test robotics scenarios
- Simulate sensor behavior
- Model breakage scenarios
- Perform fluid simulations

## Step 1: Enable Physics Extension

### Add PhysX Extension

1. **Close your application** if it's still open

2. **Open your .kit file** in VS Code

3. **Add PhysX extension** to the `[dependencies]` section:
   ```toml
   [dependencies]
   # ... other dependencies ...
   "omni.physx.bundle" = {}
   ```

   The PhysX extension adds a bundled set of physics extensions to your application.

### Disable Fabric Scene Delegate

**Important**: Fabric is incompatible with PhysX due to different transform handling methods. You must disable Fabric Scene Delegate before using PhysX.

1. **In your .kit file**, search for `useFabricSceneDelegate`

2. **Change the value** from `true` to `false`:
   ```toml
   useFabricSceneDelegate = false
   ```

3. **Save the .kit file**

4. **Build and launch** your application from VS Code

## Step 2: Prepare Scene for Physics Simulation

### Load Factory_Lite.usd

1. **Open your application**

2. **Load Factory_Lite.usd** scene
   - This is a lightweight version of the factory
   - Suitable for building conveyor belt systems

3. **Switch to Layout mode** if necessary
   - Click **Layout** at the top of the screen

### Add Conveyor Belt Assets

1. **Navigate to NVIDIA Assets**
   - Click the **NVIDIA Assets** tab at the lower left
   - Enter search term **"conveyor"** to display available conveyor belts

2. **Add conveyor belts**
   - Add two or more belt-based conveyor belts
   - Example assets:
     - `ConveyorBelt_A29_PR_NVD_01`
     - `ConveyorBelt_A25_PR_NVD_01`

3. **Optional: Add container**
   - Search for "bin" or "container"
   - Add a container to catch boxes at the end of the belt

### About SimReady Assets

NVIDIA Assets are **SimReady assets**, meaning:
- Built to **real-world scale**
- **Z-up pivot point** properly placed and aligned
- Assets "sit" properly on the ground plane
- Real-world scale is crucial for accurate physics simulation

### Add Boxes

1. **Search for boxes**
   - Enter search term **"cardbox"** to display cardboard box assets

2. **Place boxes**
   - Drag and place **three boxes** on the topmost part of the conveyor belt
   - Example asset: `Cardbox_C3`

**Note**: In Factory_Lite.usd, physics is already enabled for the floor, so boxes won't fall through even without explicit floor physics setup.

## Step 3: Configure Physics for Objects

### Assign Physics to Boxes

1. **Select all three boxes**
   - Use Ctrl+Click (Windows/Linux) or Cmd+Click (Mac) to select multiple objects

2. **Open Property panel**
   - If not visible, open Window > Property

3. **Add Physics preset**
   - Click the **+Add** button
   - Choose **Physics > Rigid Body with Colliders Preset**

**What this does**:
- Designates assets as **rigid bodies** that respond to collisions
- A rigid body can move and collide but keeps its shape (doesn't bend or squash)
- Colliders Preset defines collision behavior

### Assign Physics to Conveyor Belt

1. **Select the conveyor mechanism**
   - Select the entire conveyor in the viewport

2. **Select belt mesh only**
   - In the Stage window, expand the conveyor object
   - Select only the **Mesh** type asset representing the belt
   - Example name: `SM_ConveyorBelt_A29_Belt01_01`

3. **Add Physics preset**
   - With belt mesh selected, click **+Add** in Property panel
   - Choose **Physics > Rigid Body with Colliders Preset**

## Step 4: Configure Belt Movement

### Set Kinematic Properties

1. **Select the belt mesh** (not the entire conveyor)

2. **Navigate to Physics section** in Property panel

3. **Configure settings**:
   - **Kinematic Enabled**: `On`
   - **Velocities in Local Space**: `On`

**What these do**:
- **Kinematic Enabled**: Simulation acts like the body is continuously moving and imparts movement to contacting objects (boxes)
- **Velocities in Local Space**: Use the belt's pivot point axis to determine movement direction

### Set Surface Velocity

1. **With belt mesh selected**, click **+Add** in Property panel

2. **Choose Physics > Surface Velocity**

3. **Configure Surface Velocity**:
   - A new **Surface Velocity** panel appears in Physics section
   - Set **Surface Linear Velocity Y** to `-20` (negative 20)

**Important Notes**:
- Check the belt's pivot point axis in the viewport
- Green axis (Y-axis) points along the conveyor belt
- Use **negative value** to move in the direction opposite the arrow
- **Surface Linear Velocity** works on dynamic bodies, making it better than Linear Velocity

### Save Scene

**Save the scene** before testing so you can reset objects to original positions after simulation.

## Step 5: Test Physics Simulation

### Run Simulation

1. **Click Timeline button** at lower right of viewport
   - This displays the timeline

2. **Click Play button** on Timeline
   - The simulation runs

### Expected Behavior

- Boxes should move along the conveyor belt
- Boxes fall off at the end of the first belt
- Boxes hit the floor (physics enabled for floor)

### Fix Direction

If the belt moves backward:
1. **Reload the scene** to reset positions
2. **Select belt mesh**
3. **Change Surface Linear Velocity Y** to `-20` (negative)
4. **Save and test again**

## Step 6: Configure Multiple Belts

### Setup Additional Belts

1. **Reload the file** to reset positions

2. **For each additional belt**:
   - Select only the **belt mesh** (not entire conveyor)
   - Apply **Rigid Body with Colliders Preset**
   - Set **Kinematic Enabled**: `On`
   - Set **Velocities in Local Space**: `On`
   - Add **Surface Velocity**
   - Set **Surface Linear Velocity** along appropriate axis

3. **Save the scene**

4. **Play simulation** to test

## Troubleshooting

### Box Not Moving on Belt

**Problem**: Box isn't moving along the belt

**Solution**:
- Box may be placed **below the belt surface**
- Physics engine can't detect collision if objects are embedded
- **Move box well above the belt**
- Box will fall onto belt due to gravity and then roll with belt

### Scaling Issues

**Problem**: Unpredictable behavior with scaled assets

**Solution**:
- **Uniform scaling** is safe for physics simulation
- **Non-uniform scaling** (one or two axes) may cause unpredictable behavior
- Avoid non-uniform scaling for physics-enabled objects

### Boxes Bouncing Off Container

**Problem**: Boxes bounce off container instead of falling inside

**Solution**:
- Try different **Approximation** settings in Colliders section
- Ensure physics is applied to **Mesh asset**, not Xform asset
- Check Colliders section is visible after applying preset

### Colliders Section Missing

**Problem**: No Colliders section after applying preset

**Solution**:
- Ensure physics was applied to a **Mesh asset**, not Xform asset
- Select the mesh component, not the parent Xform

## Advanced Configuration

### Physics Stage Settings

1. **Open Physics Settings**
   - Choose **Window > Physics Stage Settings**

2. **Experiment with settings**:
   - **Gravity**: Increase or decrease gravity
   - **Friction**: Adjust friction values
   - **Restitution**: Control bounce behavior
   - **Solver iterations**: Adjust simulation accuracy

### Additional Experiments

#### Catch Container Physics

1. **Apply physics to container** at end of belt
2. **Use Rigid Body with Colliders Preset**
3. **Adjust Colliders Approximation** if boxes bounce off

#### Falling Boxes Test

1. **Place boxes in air** above the floor
2. **Apply physics** to boxes
3. **Play simulation** to see boxes fall and bounce

## Use Cases

### Digital Twin Applications

Physics simulations enable various use cases:

1. **Product Movement**
   - Simulate product flow through systems
   - Test conveyor systems
   - Model material handling

2. **Robotics Simulations**
   - Train robots for pick-and-place tasks
   - Test collision avoidance
   - Simulate robot interactions

3. **Sensor Simulation**
   - Test sensor placement
   - Simulate sensor behavior
   - Validate sensor data

4. **Breakage Scenarios**
   - Model failure scenarios
   - Test safety systems
   - Analyze impact scenarios

5. **Fluid Simulations**
   - Model fluid flow
   - Test fluid systems
   - Simulate liquid behavior

## Benefits

### Automation

- **Automatic animation** with real-world physics values
- **Gravity and friction** handled automatically
- **Saves development time**
- **Frees developers** for other tasks

### Accuracy

- **Real-world scale** ensures accurate simulation
- **Physical accuracy** means realistic behavior
- **Predictable results** based on physics laws

## Related Resources

- [Simulation Documentation](https://docs.omniverse.nvidia.com/)
- [Rigid-Body Simulation](https://docs.omniverse.nvidia.com/)
- [SimReady 3D Art Asset Creation](https://docs.omniverse.nvidia.com/)
- [Physics Settings](https://docs.omniverse.nvidia.com/)

## Next Steps

- Experiment with different physics settings
- Try more complex simulations
- Integrate physics with other extensions
- Explore advanced physics features
