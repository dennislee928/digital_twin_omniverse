# 擴展開發指南

本指南說明如何開發、配置和整合自訂擴展到 USD Explorer 應用程式中。

## 目錄

1. [擴展基礎](#擴展基礎)
2. [創建新擴展](#創建新擴展)
3. [擴展配置](#擴展配置)
4. [擴展整合](#擴展整合)
5. [範例代碼](#範例代碼)

## 擴展基礎

### 擴展結構

一個基本的 Python 擴展包含：

```
extension_name/
├── config/
│   └── extension.toml      # 擴展配置
├── {{python_module_path}}/
│   ├── __init__.py
│   ├── extension.py        # 主擴展代碼
│   └── tests/              # 測試文件
├── data/                   # 資源文件（圖標等）
└── docs/                   # 文檔
```

### 基本擴展代碼

```python
import omni.ext

class MyExtension(omni.ext.IExt):
    def on_startup(self, ext_id: str):
        """擴展啟動時調用"""
        print("Extension startup")
        self._ext_id = ext_id
    
    def on_shutdown(self):
        """擴展關閉時調用"""
        print("Extension shutdown")
```

## 創建新擴展

### 方法 1: 使用創建腳本

```bash
# 運行創建腳本
./scripts/create_extension.sh

# 按照提示輸入：
# - 擴展名稱
# - Python 模組路徑
```

### 方法 2: 手動創建

1. **複製模板**
   ```bash
   cp -r templates/extensions/basic_python/template extensions/my_extension
   ```

2. **替換模板變數**
   - 將 `{{extension_name}}` 替換為實際名稱
   - 將 `{{python_module_path}}` 替換為模組路徑

3. **編輯代碼**
   - 編輯 `extension.py` 實現功能
   - 更新 `extension.toml` 配置

## 擴展配置

### extension.toml 配置

```toml
[package]
title = "My Extension"
version = "1.0.0"
description = "Extension description"

[dependencies]
# 擴展依賴的其他擴展
"omni.kit.tool.measure" = {}

[python]
modules = ["my_module.extension"]
```

### .kit 文件配置

在應用程式的 `.kit` 文件中添加擴展：

```toml
[dependencies]
"my_extension" = {}

# 或指定順序
"my_extension" = { order = 1000 }
```

### 禁用擴展

```toml
[settings.app.extensions]
excluded = [
    "my_extension",  # 禁用此擴展
]
```

## 擴展整合

### 檢查擴展可用性

```python
import omni.kit.app

app = omni.kit.app.get_app()
ext_manager = app.get_extension_manager()

if ext_manager.is_extension_enabled("omni.kit.tool.markup"):
    print("Markup extension is available")
```

### 整合多個擴展

參考 `examples/extension_integration_example.py` 了解如何：
- 檢查擴展可用性
- 設置事件監聽
- 整合多個擴展功能

## 範例代碼

### 範例 1: 基本擴展

見 `examples/custom_extension_example.py`：
- 基本擴展結構
- USD 場景操作
- 自訂命令

### 範例 2: 擴展整合

見 `examples/extension_integration_example.py`：
- 多擴展整合
- 事件監聽
- 擴展間通訊

### 範例 3: 配置範例

見 `examples/extension_config_example.kit`：
- 擴展依賴配置
- 擴展順序控制
- 擴展設定

## 常用 API

### USD 場景操作

```python
import omni.usd
from pxr import Usd

# 獲取當前場景
usd_context = omni.usd.get_context()
stage = usd_context.get_stage()

# 創建 Prim
prim = stage.DefinePrim("/MyPrim", "Xform")

# 獲取 Prim
prim = stage.GetPrimAtPath("/MyPrim")
```

### 命令執行

```python
import omni.kit.commands

# 執行命令
omni.kit.commands.execute("CopyPrimsCommand", 
    paths_from=["/Source"],
    paths_to=["/Target"]
)
```

### UI 創建

```python
import omni.kit.ui

# 創建視窗
window = omni.kit.ui.Window("My Window")
```

## 開發工作流程

### 1. 創建擴展

```bash
./scripts/create_extension.sh
```

### 2. 開發代碼

- 編輯 `extension.py`
- 實現 `on_startup` 和 `on_shutdown`
- 添加功能代碼

### 3. 測試擴展

- 在應用程式中啟用擴展
- 測試功能
- 檢查日誌輸出

### 4. 配置擴展

- 更新 `extension.toml`
- 在 `.kit` 文件中添加依賴
- 配置擴展設定

### 5. 部署擴展

- 將擴展複製到應用程式擴展目錄
- 或打包為擴展包

## 最佳實踐

### 1. 錯誤處理

```python
def on_startup(self, ext_id: str):
    try:
        # 擴展邏輯
        pass
    except Exception as e:
        print(f"Error in extension: {e}")
```

### 2. 資源清理

```python
def on_shutdown(self):
    # 清理訂閱
    if hasattr(self, '_subscription'):
        self._subscription = None
    
    # 清理資源
    self._cleanup()
```

### 3. 日誌記錄

```python
import carb

carb.log_info("Extension started")
carb.log_warn("Warning message")
carb.log_error("Error message")
```

## 調試技巧

### 1. 使用 Console 視窗

- 開啟 Window > Console
- 查看擴展輸出
- 執行 Python 代碼

### 2. 使用斷點

- 在 VS Code 中設置斷點
- 使用 Python 調試器
- 檢查變數值

### 3. 日誌輸出

```python
import carb

carb.log_info(f"Variable value: {variable}")
```

## 相關資源

- [擴展配置範例](examples/extension_config_example.kit)
- [自訂擴展範例](examples/custom_extension_example.py)
- [擴展整合範例](examples/extension_integration_example.py)
- [Omniverse 擴展開發文檔](https://docs.omniverse.nvidia.com/)

## 下一步

- 查看現有擴展模板了解更多範例
- 參考 USD Explorer 擴展源代碼
- 閱讀 Omniverse 擴展開發文檔
