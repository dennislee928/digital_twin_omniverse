# Variant Presenter 快速開始指南

## 快速步驟

### 1. 轉換 USD 為 USDA（如果尚未轉換）

**推薦方法**：使用 USD Explorer 應用程式

1. 開啟 USD Explorer
2. 開啟 `Factory_Lite.usd`
3. File > Save As > 選擇 USDA (ASCII) 格式

**替代方法**：使用 Python 腳本（需要在 Omniverse 環境中）

```bash
# 先檢查環境
python check_usd_environment.py

# 如果環境正確，執行轉換
python convert_usd_to_usda.py Factory_Lite/Factory_Lite.usd
```

### 2. 在 VS Code 中搜尋變體

1. 開啟 `Factory_Lite.usda`
2. 搜尋 `"variant"`（使用 Cmd+F 或 Ctrl+F）

### 3. 添加 Variant Presenter 擴展

1. **關閉應用程式**
2. 開啟應用程式的 `.kit` 檔案
3. 在 `[dependencies]` 區段添加：
    ```toml
    "omni.kit.variant.presenter" = {}
    ```
4. 儲存檔案
5. **重新啟動應用程式**

### 4. 使用 Variant Presenter

1. 開啟 `Factory_Lite.usd`
2. 選擇 **Tools > Variants > Variant Presenter**
3. 在面板中檢視和切換變體

## 詳細說明

請參閱完整指南：

-   [Variant Presenter 設定指南](VARIANT_PRESENTER_GUIDE.md)（繁體中文）
-   [Variant Presenter Setup Guide](VARIANT_PRESENTER_GUIDE_EN.md)（English）
