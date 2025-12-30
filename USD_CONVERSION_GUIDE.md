# USD 轉換指南

本指南說明如何將二進位 USD 檔案（`.usd`）轉換為可讀的 ASCII 格式（`.usda`）。

## 為什麼需要轉換？

- **可讀性**：USDA 格式是人類可讀的，方便在文字編輯器中檢視和編輯
- **學習**：可以查看 USD 檔案的內部結構，學習 OpenUSD 語法
- **除錯**：更容易識別和修復問題
- **版本控制**：ASCII 格式更適合版本控制系統

## 方法 1: 使用 USD Explorer 應用程式（推薦）

這是最簡單、最可靠的方法，不需要額外的環境設定。

### 步驟

1. **啟動 USD Explorer 應用程式**
   - 從 Omniverse Launcher 啟動您的自訂應用程式

2. **開啟 USD 檔案**
   - 選擇 **File > Open**
   - 瀏覽並選擇 `Factory_Lite.usd`

3. **儲存為 USDA 格式**
   - 選擇 **File > Save As**
   - 在檔案類型中選擇 **USDA (ASCII)**
   - 選擇儲存位置並儲存

### 優點

- ✅ 不需要額外設定
- ✅ 適用於所有使用者
- ✅ 最可靠的方法
- ✅ 可以預覽檔案內容

## 方法 2: 使用 Python 腳本

此方法需要在 Omniverse 環境中運行，或已安裝 USD Python 綁定。

### 步驟 1: 檢查環境

首先檢查您的系統是否具備運行腳本的環境：

```bash
python check_usd_environment.py
```

此腳本會檢查：
- Python 版本
- USD Python API (pxr) 是否可用
- Omniverse 環境變數

### 步驟 2: 執行轉換

如果環境檢查通過，執行轉換：

```bash
python convert_usd_to_usda.py Factory_Lite/Factory_Lite.usd
```

### 如果環境檢查失敗

如果 `check_usd_environment.py` 顯示無法運行，請：

1. **使用 USD Explorer 應用程式**（方法 1）- 最簡單
2. **在 Omniverse Kit 環境中運行**
   - 啟動 Omniverse 應用程式
   - 使用應用程式內建的 Python 控制台
3. **安裝 USD Python 綁定**
   - 從 [USD GitHub](https://github.com/PixarAnimationStudios/USD) 編譯安裝
   - 或使用預編譯的 USD 發行版

## 方法 3: 使用 USD 命令列工具

如果您有安裝 USD 工具，可以使用命令列：

```bash
# 使用 usdcat（如果已安裝）
usdcat --format usda input.usd > output.usda

# 或使用 usdview
usdview --export input.usd output.usda
```

## 常見問題

### Q: 為什麼 Python 腳本無法運行？

**A**: Python 腳本需要 USD Python API (pxr 模組)，這通常只在以下環境中可用：
- Omniverse 應用程式環境
- 已安裝 USD Python 綁定的系統

**解決方案**：使用 USD Explorer 應用程式轉換檔案（方法 1）

### Q: 轉換後的檔案很大？

**A**: 這是正常的。ASCII 格式比二進位格式大很多，因為：
- 所有資料都以文字形式儲存
- 包含完整的結構資訊
- 沒有壓縮

### Q: 可以在文字編輯器中編輯 USDA 檔案嗎？

**A**: 可以，但需要小心：
- 確保語法正確
- 建議使用支援 USD 語法的編輯器
- 編輯前先備份原始檔案

### Q: 如何將 USDA 轉換回 USD？

**A**: 在 USD Explorer 中：
1. 開啟 USDA 檔案
2. File > Save As
3. 選擇 USD (Binary) 格式

## 相關工具

- `check_usd_environment.py` - 檢查 USD 環境
- `convert_usd_to_usda.py` - 轉換 USD 為 USDA
- USD Explorer 應用程式 - 圖形化轉換工具

## 相關文件

- [Variant Presenter 設定指南](VARIANT_PRESENTER_GUIDE.md)
- [USD 探索指南](docs/USD_EXPLORATION_GUIDE.md)
- [OpenUSD 官方文件](https://openusd.org/)
