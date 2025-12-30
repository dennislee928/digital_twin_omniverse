# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# 擴展整合範例
# Extension Integration Example
#
# 此範例展示如何整合多個擴展功能
# This example demonstrates how to integrate multiple extension features

import omni.ext
import omni.kit.commands
import omni.usd
from pxr import Usd


class ExtensionIntegrationExample(omni.ext.IExt):
    """
    擴展整合範例
    Extension Integration Example
    
    展示如何整合：
    Demonstrates how to integrate:
    - Markup 擴展
    - Waypoint 擴展
    - Measure 擴展
    - Section 擴展
    """
    
    def on_startup(self, ext_id: str):
        """擴展啟動"""
        print("[ExtensionIntegrationExample] Starting integration")
        self._ext_id = ext_id
        self._setup_integrations()
    
    def on_shutdown(self):
        """擴展關閉"""
        print("[ExtensionIntegrationExample] Shutting down integration")
        self._cleanup_integrations()
    
    def _setup_integrations(self):
        """設置整合"""
        # 檢查擴展是否可用
        # Check if extensions are available
        self._check_extension_availability()
        
        # 設置事件監聽
        # Setup event listeners
        self._setup_event_listeners()
    
    def _check_extension_availability(self):
        """檢查擴展可用性"""
        import omni.kit.app
        
        app = omni.kit.app.get_app()
        ext_manager = app.get_extension_manager()
        
        extensions_to_check = [
            "omni.kit.tool.markup",
            "omni.kit.waypoint.core",
            "omni.kit.tool.measure",
            "omni.kit.tool.section"
        ]
        
        available_extensions = []
        for ext_name in extensions_to_check:
            if ext_manager.is_extension_enabled(ext_name):
                available_extensions.append(ext_name)
                print(f"✓ {ext_name} is available")
            else:
                print(f"✗ {ext_name} is not available")
        
        return available_extensions
    
    def _setup_event_listeners(self):
        """設置事件監聽器"""
        # 監聽場景變更事件
        # Listen to stage change events
        usd_context = omni.usd.get_context()
        
        # 監聽場景開啟事件
        # Listen to stage opened event
        self._stage_event_sub = usd_context.get_stage_event_stream().create_subscription_to_pop(
            self._on_stage_event,
            name="ExtensionIntegrationExample"
        )
    
    def _on_stage_event(self, event):
        """場景事件處理"""
        # 當場景變更時執行操作
        # Perform actions when stage changes
        if event.type == int(omni.usd.StageEventType.OPENED):
            print("Stage opened, initializing integrations")
            self._initialize_on_stage_open()
    
    def _initialize_on_stage_open(self):
        """場景開啟時初始化"""
        # 在這裡可以自動創建 Waypoint、添加 Markup 等
        # Here you can automatically create waypoints, add markups, etc.
        pass
    
    def _cleanup_integrations(self):
        """清理整合"""
        if hasattr(self, '_stage_event_sub'):
            self._stage_event_sub = None


# 擴展間通訊範例
# Inter-Extension Communication Example

class ExtensionCommunication:
    """
    擴展間通訊範例
    Inter-Extension Communication Example
    """
    
    @staticmethod
    def call_markup_extension():
        """調用 Markup 擴展功能"""
        try:
            # 嘗試獲取 Markup 擴展實例
            # Try to get Markup extension instance
            import omni.kit.app
            app = omni.kit.app.get_app()
            ext_manager = app.get_extension_manager()
            
            # 這裡可以調用 Markup 擴展的 API
            # Here you can call Markup extension's API
            print("Calling Markup extension")
        except Exception as e:
            print(f"Error calling Markup extension: {e}")
    
    @staticmethod
    def create_waypoint_programmatically(position: tuple, name: str):
        """程式化創建 Waypoint"""
        try:
            # 使用 Waypoint API 創建 Waypoint
            # Use Waypoint API to create waypoint
            print(f"Creating waypoint '{name}' at {position}")
            # 實際實現會使用 Waypoint 擴展的 API
            # Actual implementation would use Waypoint extension's API
        except Exception as e:
            print(f"Error creating waypoint: {e}")


# 自訂工具整合範例
# Custom Tool Integration Example

class CustomToolIntegration:
    """
    自訂工具整合範例
    Custom Tool Integration Example
    """
    
    def __init__(self):
        self.tools = {}
    
    def register_tool(self, name: str, tool_func):
        """註冊工具"""
        self.tools[name] = tool_func
        print(f"Registered tool: {name}")
    
    def execute_tool(self, name: str, *args, **kwargs):
        """執行工具"""
        if name in self.tools:
            return self.tools[name](*args, **kwargs)
        else:
            print(f"Tool '{name}' not found")
            return None
    
    def list_tools(self):
        """列出所有工具"""
        return list(self.tools.keys())


# 使用範例
# Usage Example

def example_workflow():
    """
    整合工作流程範例
    Integrated Workflow Example
    """
    # 1. 檢查擴展可用性
    # Check extension availability
    integration = ExtensionIntegrationExample(None)
    available = integration._check_extension_availability()
    
    # 2. 執行整合操作
    # Perform integrated operations
    if "omni.kit.tool.measure" in available:
        print("Measure extension available, can perform measurements")
    
    if "omni.kit.waypoint.core" in available:
        print("Waypoint extension available, can create waypoints")
    
    # 3. 使用工具整合
    # Use tool integration
    tool_integration = CustomToolIntegration()
    tool_integration.register_tool("custom_measure", lambda: "measure_result")
    result = tool_integration.execute_tool("custom_measure")
    print(f"Tool result: {result}")
