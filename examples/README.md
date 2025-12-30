# 範例代碼目錄

此目錄包含擴展開發和配置的範例代碼。

## 文件說明

### 配置範例

- **extension_config_example.kit** - 擴展配置範例
  - 展示如何在 .kit 文件中配置擴展
  - 包含 Review 模式擴展的配置
  - 展示擴展順序控制和禁用方法

### 代碼範例

- **custom_extension_example.py** - 自訂擴展範例
  - 基本擴展結構
  - USD 場景操作函數
  - 自訂命令範例
  - 輔助函數範例

- **extension_integration_example.py** - 擴展整合範例
  - 多擴展整合方法
  - 擴展可用性檢查
  - 事件監聽設置
  - 擴展間通訊範例

## 使用方式

### 1. 查看配置範例

```bash
# 查看擴展配置範例
cat examples/extension_config_example.kit
```

### 2. 使用代碼範例

```python
# 在您的擴展中導入和使用
from examples.custom_extension_example import (
    get_stage,
    create_prim_at_position,
    duplicate_prim
)
```

### 3. 參考整合範例

```python
# 學習如何整合多個擴展
from examples.extension_integration_example import (
    ExtensionIntegrationExample,
    ExtensionCommunication
)
```

## 相關文檔

- [擴展開發指南](../EXTENSION_DEVELOPMENT_GUIDE.md)
- [Review 模式擴展綜合指南](../REVIEW_EXTENSIONS_GUIDE.md)
