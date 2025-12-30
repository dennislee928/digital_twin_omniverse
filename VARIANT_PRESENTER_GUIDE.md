# Variant Presenter 設定指南

本指南說明如何在您的 USD Explorer 應用程式中添加 Variant Presenter 擴展，並探索 OpenUSD 中的變體（Variants）功能。

## 什麼是 Variants（變體）？

OpenUSD 可以儲存多個資產變體，稱為 **variants**。**VariantSets** 由兩個或多個意見（opinions）組成。變體讓利害關係人可以在單一 USD 檔案中檢視不同的資產、材質和資產放置方式。

## 步驟 1: 轉換 Factory_Lite.usd 為 USDA 格式

首先，我們需要將 USD 檔案轉換為可讀的 ASCII 格式，以便在 VS Code 中檢視變體定義。

### 方法 A: 使用 USD Explorer 應用程式

1. 啟動您的 USD Explorer 應用程式
2. 開啟 `Factory_Lite.usd` 檔案
3. 選擇 **File > Save As**
4. 選擇格式為 **USDA (ASCII)**
5. 儲存為 `Factory_Lite.usda`

### 方法 B: 使用 Python 腳本

**注意**：此腳本需要在 Omniverse 環境中運行，或已安裝 USD Python 綁定。

首先檢查環境：

```bash
# 檢查 USD 環境
python check_usd_environment.py
```

如果環境正確，執行轉換：

```bash
# 在專案根目錄執行
python convert_usd_to_usda.py Factory_Lite/Factory_Lite.usd
```

**如果無法運行腳本**：請使用方法 A（USD Explorer 應用程式），這是最簡單可靠的方法。

## 步驟 2: 在 VS Code 中檢視 Variant 定義

1. 在 VS Code 中開啟 `Factory_Lite.usda` 檔案
2. 使用搜尋功能（`Cmd+F` 或 `Ctrl+F`）搜尋 **"variant"**
3. 您會看到類似這樣的變體定義：

```usda
def "SomePrim" (
    variants = {
        string variantSetName = "variantValue"
    }
    prepend variantSets = "variantSetName"
)
{
    variantSet "variantSetName" = {
        "variantValue" {
            # 變體特定的內容
        }
        "anotherVariantValue" {
            # 另一個變體的內容
        }
    }
}
```

## 步驟 3: 添加 Variant Presenter 擴展到應用程式

Variant Presenter 是一個範例擴展，用於呈現和選擇變體，可以根據應用程式的特定 UI 和邏輯進行自訂。

### 3.1 找到您的應用程式 .kit 檔案

您的自訂應用程式應該有一個 `.kit` 檔案。根據您使用的模板，可能位於：

-   如果您使用 USD Explorer 模板：`<your_app_directory>/omni.usd_explorer.kit`
-   或類似的位置

**注意**：如果您還沒有建立自訂應用程式，請先使用 USD Explorer 模板建立一個。

### 3.2 編輯 .kit 檔案

1. **關閉您的應用程式**（如果正在運行）
2. 在 VS Code 中開啟您的應用程式 `.kit` 檔案
3. 找到 `[dependencies]` 區段
4. 在 `[dependencies]` 區段中添加以下行：

```toml
[dependencies]
# ... 其他依賴 ...
"omni.kit.variant.presenter" = {}
```

### 3.3 儲存檔案

儲存 `.kit` 檔案後，重新啟動您的應用程式。

## 步驟 4: 使用 Variant Presenter

1. **啟動您的應用程式**
2. **開啟 Factory_Lite.usd** 檔案
3. 在應用程式中，選擇 **Tools > Variants > Variant Presenter** 來存取 Variant Presenter 面板

## 步驟 5: 比較 .usda 程式碼與應用程式顯示

在 Variant Presenter 面板中，您可以：

1. **檢視所有可用的變體集**（VariantSets）
2. **檢視每個變體集中的變體選項**
3. **切換不同的變體**並即時查看場景變化
4. **比較 .usda 檔案中的變體定義**與應用程式中顯示的變體

### 變體定義範例

在 `.usda` 檔案中，您可能會看到類似這樣的結構：

```usda
def "Factory_Equipment" (
    prepend variantSets = "equipmentType"
)
{
    variantSet "equipmentType" = {
        "TypeA" {
            def "Equipment" (
                prepend payload = @./SubUSDs/Equipment_TypeA.usd@
            )
        }
        "TypeB" {
            def "Equipment" (
                prepend payload = @./SubUSDs/Equipment_TypeB.usd@
            )
        }
    }
}
```

這表示：

-   有一個名為 `equipmentType` 的變體集
-   包含兩個變體：`TypeA` 和 `TypeB`
-   每個變體引用不同的 USD 檔案

## 變體的優勢

1. **單一檔案管理多個版本**：不需要為每個版本建立單獨的檔案
2. **快速切換**：可以在不同變體之間快速切換進行比較
3. **協作友好**：團隊成員可以檢視和選擇不同的變體
4. **減少檔案數量**：所有變體都在同一個 USD 檔案中

## 學習更多

-   **Create a Variant Set** 主題：了解如何使用 OpenUSD 編寫變體集
-   [OpenUSD 官方文件](https://openusd.org/)
-   [Omniverse 文件](https://docs.omniverse.nvidia.com/)

## 疑難排解

### 問題：找不到 .kit 檔案

**解決方案**：

-   確認您已經從模板建立了自訂應用程式
-   檢查應用程式安裝目錄
-   查看 Omniverse Launcher 中的應用程式設定

### 問題：Variant Presenter 選單未出現

**解決方案**：

-   確認已正確添加 `"omni.kit.variant.presenter" = {}` 到 `.kit` 檔案
-   確認已重新啟動應用程式
-   檢查擴展是否已正確載入（Window > Extensions）

### 問題：看不到變體選項

**解決方案**：

-   確認 `Factory_Lite.usd` 檔案包含變體定義
-   在 VS Code 中搜尋 "variant" 確認檔案中有變體
-   嘗試選擇場景中的不同 prim 來查看其變體
