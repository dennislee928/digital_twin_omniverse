# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# 自訂擴展範例
# Custom Extension Example
#
# 此範例展示如何創建一個自訂擴展
# This example demonstrates how to create a custom extension

import omni.ext
import omni.kit.commands
import omni.usd
from pxr import Usd, UsdGeom


class CustomDigitalTwinExtension(omni.ext.IExt):
    """
    自訂數位孿生擴展範例
    Custom Digital Twin Extension Example
    
    此擴展展示如何：
    This extension demonstrates how to:
    1. 整合多個擴展功能
       Integrate multiple extension features
    2. 創建自訂工具
       Create custom tools
    3. 與 USD 場景互動
       Interact with USD scenes
    """

    def on_startup(self, ext_id: str):
        """
        擴展啟動時調用
        Called when extension is activated
        """
        print("[CustomDigitalTwinExtension] Extension startup")
        
        self._ext_id = ext_id
        self._setup_ui()
        self._register_commands()
        
    def on_shutdown(self):
        """
        擴展關閉時調用
        Called when extension is deactivated
        """
        print("[CustomDigitalTwinExtension] Extension shutdown")
        self._cleanup()
    
    def _setup_ui(self):
        """設置 UI 元素"""
        # 這裡可以添加自訂 UI
        # Add custom UI here
        pass
    
    def _register_commands(self):
        """註冊自訂命令"""
        # 註冊自訂命令供其他擴展或腳本使用
        # Register custom commands for use by other extensions or scripts
        pass
    
    def _cleanup(self):
        """清理資源"""
        # 清理擴展使用的資源
        # Clean up resources used by extension
        pass


# 輔助函數範例
# Helper Function Examples

def get_stage():
    """
    獲取當前 USD 場景
    Get current USD stage
    
    Returns:
        Usd.Stage: 當前場景物件
    """
    usd_context = omni.usd.get_context()
    return usd_context.get_stage()


def create_prim_at_position(prim_path: str, position: tuple):
    """
    在指定位置創建 Prim
    Create Prim at specified position
    
    Args:
        prim_path: Prim 路徑
        position: 位置座標 (x, y, z)
    """
    stage = get_stage()
    if not stage:
        print("Error: No stage available")
        return
    
    prim = stage.DefinePrim(prim_path, "Xform")
    if prim:
        xform = UsdGeom.Xformable(prim)
        translate_op = xform.AddTranslateOp()
        translate_op.Set(position)
        print(f"Created prim at {prim_path} with position {position}")


def duplicate_prim(source_path: str, target_path: str):
    """
    複製 Prim
    Duplicate Prim
    
    Args:
        source_path: 源 Prim 路徑
        target_path: 目標 Prim 路徑
    """
    stage = get_stage()
    if not stage:
        print("Error: No stage available")
        return
    
    source_prim = stage.GetPrimAtPath(source_path)
    if not source_prim:
        print(f"Error: Source prim not found at {source_path}")
        return
    
    # 使用 USD 命令複製
    # Use USD command to duplicate
    omni.kit.commands.execute(
        "CopyPrimsCommand",
        paths_from=[source_path],
        paths_to=[target_path]
    )
    print(f"Duplicated {source_path} to {target_path}")


# 擴展命令範例
# Extension Command Examples

class CustomMeasureCommand(omni.kit.commands.Command):
    """
    自訂測量命令範例
    Custom Measure Command Example
    """
    
    def __init__(self, point1: tuple, point2: tuple):
        self.point1 = point1
        self.point2 = point2
        self.distance = None
    
    def do(self):
        """執行命令"""
        import math
        dx = self.point2[0] - self.point1[0]
        dy = self.point2[1] - self.point1[1]
        dz = self.point2[2] - self.point1[2]
        self.distance = math.sqrt(dx*dx + dy*dy + dz*dz)
        print(f"Distance: {self.distance:.2f}")
        return self.distance
    
    def undo(self):
        """撤銷命令"""
        pass


# 使用範例
# Usage Example

if __name__ == "__main__":
    # 這些函數可以在擴展中使用
    # These functions can be used in extensions
    pass
