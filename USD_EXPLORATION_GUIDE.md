# USD 探索指南

本指南協助您了解 OpenUSD 檔案結構與數位孿生開發概念。

## 步驟 1: 在 USD Explorer 中開啟檔案

1. **啟動您的自訂應用程式**（USD Explorer 模板）
2. 在開啟畫面點擊 **New**，這會在 Layout 模式中開啟新檔案
3. 在 **Layout 模式**中，開啟 `Factory_Lite.usd` 檔案

### 模式說明

-   **Review 模式**: 供終端使用者導航、檢視和新增註解
-   **Layout 模式**: 供進階使用者組裝大型場景並執行變更

## 步驟 2: 轉換為 USDA 格式

### 方法 A: 使用 USD Explorer 應用程式（推薦）

1. 在應用程式中開啟 `Factory_Lite.usd`
2. 選擇 **File > Save As** 或 **Export**
3. 選擇格式為 **USDA (ASCII)**
4. 儲存為 `Factory_Lite.usda`

### 方法 B: 使用 Python 腳本

```bash
python convert_usd_to_usda.py Factory_Lite/Factory_Lite.usd
```

## 步驟 3: 檢視 Factory_Lite.usda 結構

在 VS Code 或文字編輯器中開啟 `.usda` 檔案，搜尋 `.usd` 字串。

### 關鍵概念：Payload 引用

您會看到類似這樣的結構：

```usda
def "Vehicle_Hanger_Adjust" (
    prepend payload = @./SubUSDs/Vehicle_Hanger_Adjust.usd@
)
```

這表示：

-   `Factory_Lite.usd` 是一個**組合檔案**（composition file）
-   它使用 **payload** 機制引用其他 USD 檔案
-   每個資產（如 `Vehicle_Hanger_Adjust`）都儲存在獨立的 USD 檔案中
-   這些檔案位於 `SubUSDs/` 資料夾中

### 為什麼這樣設計？

1. **輕量級主檔案**: `Factory_Lite.usd` 本身很小，只包含引用
2. **模組化**: 每個資產可以獨立更新，不需要處理整個場景
3. **團隊協作**: 不同團隊可以同時編輯不同資產
4. **效能**: 可以延遲載入（lazy loading）不需要的資產

## 步驟 4: 檢視個別資產

1. 在應用程式中導航到 `SubUSDs/` 資料夾
2. 找到 `Vehicle_Hanger_Adjust.usd`
3. 雙擊開啟該資產

### 轉換個別資產為 USDA

同樣地，將 `Vehicle_Hanger_Adjust.usd` 儲存為 `.usda` 格式。

### 檢視資產內容

在 `.usda` 檔案中，您會看到：

-   **頂點位置**（vertex positions）: 定義 3D 空間中的形狀
-   **面（faces）**: 定義幾何形狀
-   **材質與屬性**: 視覺外觀相關的資料

## OpenUSD 的優勢

### 1. 資料聚合（Data Aggregation）

-   可以從多個來源組合不同類型的資料
-   支援複雜場景的組裝

### 2. 引用機制（References & Payloads）

-   **Reference**: 直接引用，立即載入
-   **Payload**: 延遲載入，需要時才載入（更高效能）

### 3. 變體（Variants）

-   同一個資產可以有多個版本
-   可以動態切換不同變體

### 4. 圖層（Layers）

-   支援多層編輯
-   可以覆蓋（override）特定屬性而不修改原始檔案

## 下一步

在下一階段，您將學習：

-   **變體（Variants）** 在 OpenUSD 中的表示方式
-   如何使用變體來管理資產的不同版本

## 相關資源

-   [Learn OpenUSD Learning Path](https://www.nvidia.com/en-us/omniverse/learn/openusd/)
-   [Data Aggregation and Navigation Guide](https://docs.omniverse.nvidia.com/)
-   [USD 官方文件](https://openusd.org/)
