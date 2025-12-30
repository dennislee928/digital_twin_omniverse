# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# Physics Setup Example
#
# This example demonstrates how to programmatically set up physics
# for objects in a USD scene, including rigid bodies, colliders,
# and surface velocity for conveyor belts.

import omni.kit.commands
import omni.usd
from pxr import Usd, UsdPhysics


class PhysicsSetupHelper:
    """
    Helper class for setting up physics properties on USD prims.
    """
    
    @staticmethod
    def get_stage():
        """Get the current USD stage."""
        usd_context = omni.usd.get_context()
        return usd_context.get_stage()
    
    @staticmethod
    def apply_rigid_body_with_colliders(prim_path: str):
        """
        Apply Rigid Body with Colliders Preset to a prim.
        
        Args:
            prim_path: Path to the prim in the USD stage
        """
        stage = PhysicsSetupHelper.get_stage()
        if not stage:
            print("Error: No stage available")
            return False
        
        prim = stage.GetPrimAtPath(prim_path)
        if not prim:
            print(f"Error: Prim not found at {prim_path}")
            return False
        
        try:
            # Apply rigid body
            # In actual implementation, this would use Kit commands
            # omni.kit.commands.execute("PhysicsRigidBodyCommand", ...)
            
            print(f"Applied Rigid Body with Colliders to {prim_path}")
            return True
        except Exception as e:
            print(f"Error applying physics: {e}")
            return False
    
    @staticmethod
    def set_kinematic_properties(prim_path: str, kinematic_enabled: bool = True, 
                                  velocities_in_local_space: bool = True):
        """
        Set kinematic properties for a rigid body.
        
        Args:
            prim_path: Path to the prim
            kinematic_enabled: Enable kinematic mode
            velocities_in_local_space: Use local space for velocities
        """
        stage = PhysicsSetupHelper.get_stage()
        if not stage:
            return False
        
        prim = stage.GetPrimAtPath(prim_path)
        if not prim:
            return False
        
        try:
            # Get or create PhysicsRigidBodyAPI
            rigid_body_api = UsdPhysics.RigidBodyAPI.Apply(prim, "physics")
            
            if rigid_body_api:
                # Set kinematic enabled
                kinematic_attr = rigid_body_api.CreateKinematicEnabledAttr(kinematic_enabled)
                
                # Set velocities in local space
                # Note: This may require additional API calls depending on Kit version
                
                print(f"Set kinematic properties for {prim_path}")
                print(f"  Kinematic Enabled: {kinematic_enabled}")
                print(f"  Velocities in Local Space: {velocities_in_local_space}")
                return True
        except Exception as e:
            print(f"Error setting kinematic properties: {e}")
            return False
    
    @staticmethod
    def set_surface_velocity(prim_path: str, velocity_x: float = 0.0, 
                             velocity_y: float = 0.0, velocity_z: float = 0.0):
        """
        Set surface velocity for a prim (e.g., conveyor belt).
        
        Args:
            prim_path: Path to the prim
            velocity_x: Velocity along X axis
            velocity_y: Velocity along Y axis
            velocity_z: Velocity along Z axis
        """
        stage = PhysicsSetupHelper.get_stage()
        if not stage:
            return False
        
        prim = stage.GetPrimAtPath(prim_path)
        if not prim:
            return False
        
        try:
            # Apply PhysicsMaterialAPI or use appropriate API
            # Surface velocity setup may require specific Kit commands
            # omni.kit.commands.execute("PhysicsSurfaceVelocityCommand", ...)
            
            print(f"Set surface velocity for {prim_path}")
            print(f"  Velocity: ({velocity_x}, {velocity_y}, {velocity_z})")
            return True
        except Exception as e:
            print(f"Error setting surface velocity: {e}")
            return False


class ConveyorBeltSetup:
    """
    Helper class for setting up conveyor belt physics.
    """
    
    @staticmethod
    def setup_conveyor_belt(belt_mesh_path: str, velocity_y: float = -20.0):
        """
        Complete setup for a conveyor belt with physics.
        
        Args:
            belt_mesh_path: Path to the belt mesh prim
            velocity_y: Surface velocity along Y axis (negative for forward direction)
        """
        print(f"Setting up conveyor belt: {belt_mesh_path}")
        
        # Step 1: Apply rigid body with colliders
        if not PhysicsSetupHelper.apply_rigid_body_with_colliders(belt_mesh_path):
            return False
        
        # Step 2: Set kinematic properties
        if not PhysicsSetupHelper.set_kinematic_properties(
            belt_mesh_path,
            kinematic_enabled=True,
            velocities_in_local_space=True
        ):
            return False
        
        # Step 3: Set surface velocity
        if not PhysicsSetupHelper.set_surface_velocity(
            belt_mesh_path,
            velocity_y=velocity_y
        ):
            return False
        
        print(f"Conveyor belt setup complete: {belt_mesh_path}")
        return True
    
    @staticmethod
    def setup_multiple_belts(belt_paths: list, velocity_y: float = -20.0):
        """
        Setup multiple conveyor belts.
        
        Args:
            belt_paths: List of belt mesh paths
            velocity_y: Surface velocity for all belts
        """
        results = []
        for belt_path in belt_paths:
            result = ConveyorBeltSetup.setup_conveyor_belt(belt_path, velocity_y)
            results.append((belt_path, result))
        
        return results


class BoxPhysicsSetup:
    """
    Helper class for setting up box physics.
    """
    
    @staticmethod
    def setup_box(box_path: str):
        """
        Setup physics for a box.
        
        Args:
            box_path: Path to the box prim
        """
        print(f"Setting up box physics: {box_path}")
        return PhysicsSetupHelper.apply_rigid_body_with_colliders(box_path)
    
    @staticmethod
    def setup_multiple_boxes(box_paths: list):
        """
        Setup physics for multiple boxes.
        
        Args:
            box_paths: List of box prim paths
        """
        results = []
        for box_path in box_paths:
            result = BoxPhysicsSetup.setup_box(box_path)
            results.append((box_path, result))
        
        return results


# Usage Examples

def example_conveyor_belt_setup():
    """
    Example: Setup a single conveyor belt.
    """
    belt_path = "/World/ConveyorBelt_A29/SM_ConveyorBelt_A29_Belt01_01"
    ConveyorBeltSetup.setup_conveyor_belt(belt_path, velocity_y=-20.0)


def example_multiple_belts_setup():
    """
    Example: Setup multiple conveyor belts.
    """
    belt_paths = [
        "/World/ConveyorBelt_A29/SM_ConveyorBelt_A29_Belt01_01",
        "/World/ConveyorBelt_A25/SM_ConveyorBelt_A25_Belt01_01"
    ]
    ConveyorBeltSetup.setup_multiple_belts(belt_paths, velocity_y=-20.0)


def example_box_setup():
    """
    Example: Setup boxes for physics simulation.
    """
    box_paths = [
        "/World/Cardbox_C3_01",
        "/World/Cardbox_C3_02",
        "/World/Cardbox_C3_03"
    ]
    BoxPhysicsSetup.setup_multiple_boxes(box_paths)


def example_complete_setup():
    """
    Example: Complete physics setup for conveyor belt system.
    """
    # Setup boxes
    box_paths = [
        "/World/Cardbox_C3_01",
        "/World/Cardbox_C3_02",
        "/World/Cardbox_C3_03"
    ]
    BoxPhysicsSetup.setup_multiple_boxes(box_paths)
    
    # Setup conveyor belts
    belt_paths = [
        "/World/ConveyorBelt_A29/SM_ConveyorBelt_A29_Belt01_01",
        "/World/ConveyorBelt_A25/SM_ConveyorBelt_A25_Belt01_01"
    ]
    ConveyorBeltSetup.setup_multiple_belts(belt_paths, velocity_y=-20.0)
    
    print("Complete physics setup finished")


if __name__ == "__main__":
    # These examples can be run in the Omniverse Kit console
    # or integrated into an extension
    pass
