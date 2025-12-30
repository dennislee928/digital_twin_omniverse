# 編輯 USD 文件指南

本指南說明如何通過直接編輯 .usda 文件來添加和修改場景中的資產。

## 概述

OpenUSD 的優勢之一是 USD 文件是人類可讀的（當保存為 USDA 格式時）。這允許開發者直接編輯文件來添加、修改或移除資產。

## 步驟 1: 保存為 USDA 格式

### 在應用程式中保存

1. **開啟場景**
   - 在應用程式中開啟包含資產的場景

2. **保存為 USDA**
   - 選擇 **File > Save As**
   - 選擇格式為 **USDA (ASCII)**
   - 保存檔案

### 使用轉換腳本

```bash
# 檢查環境
python check_usd_environment.py

# 轉換檔案（如果環境正確）
python convert_usd_to_usda.py input.usd output.usda
```

## 步驟 2: 在 VS Code 中開啟文件

1. **開啟 VS Code**
   - 啟動 Visual Studio Code

2. **開啟 USDA 文件**
   - File > Open
   - 選擇剛才保存的 .usda 文件

## 步驟 3: 搜尋資產引用

### 搜尋資產名稱

1. **使用搜尋功能**
   - 按 `Ctrl+F` (Windows/Linux) 或 `Cmd+F` (Mac)
   - 輸入資產名稱的一部分，例如 **"container_f15"**

2. **查看搜尋結果**
   - 會找到所有包含該名稱的引用
   - 每個資產由一個 `def` 語句定義

### 理解資產結構

在 .usda 文件中，資產通常這樣定義：

```usda
def "AssetName" (
    prepend references = @./path/to/asset.usd@
)
{
    double3 xformOp:translate = (100, 0, 50)
    uniform token[] xformOpOrder = ["xformOp:translate"]
}
```

**關鍵元素**：
- `def "AssetName"`：資產名稱
- `references = @./path/to/asset.usd@`：引用的 USD 文件路徑
- `xformOp:translate`：位置座標 (X, Y, Z)

## 步驟 4: 複製和修改資產定義

### 複製 def 語句

1. **選擇完整的 def 語句**
   - 從 `def "AssetName"` 開始
   - 到對應的結束大括號 `}`
   - 確保選擇完整的語句

2. **複製語句**
   - 使用 `Ctrl+C` (Windows/Linux) 或 `Cmd+C` (Mac)

3. **貼上語句**
   - 將複製的語句貼在原始語句下方
   - 現在應該有兩個（或更多）相同的資產定義

### 修改新資產

1. **更改資產名稱**
   - 修改 `def "AssetName"` 中的名稱
   - 例如：`def "AssetName_Copy"` 或 `def "AssetName_02"`

2. **更改位置座標**
   - 找到 `xformOp:translate` 行
   - 修改 X 座標值（第一個數字）
   - 例如：將 `(100, 0, 50)` 改為 `(280, 0, 50)`
   - 這會將新資產放置在 X=280 的位置

### 範例修改

**原始資產**：
```usda
def "container_f15" (
    prepend references = @./assets/container_f15.usd@
)
{
    double3 xformOp:translate = (100, 0, 50)
    uniform token[] xformOpOrder = ["xformOp:translate"]
}
```

**修改後的資產**：
```usda
def "container_f15" (
    prepend references = @./assets/container_f15.usd@
)
{
    double3 xformOp:translate = (100, 0, 50)
    uniform token[] xformOpOrder = ["xformOp:translate"]
}

def "container_f15_copy" (
    prepend references = @./assets/container_f15.usd@
)
{
    double3 xformOp:translate = (280, 0, 50)
    uniform token[] xformOpOrder = ["xformOp:translate"]
}
```

## 步驟 5: 保存文件

1. **保存文件**
   - 在 VS Code 中按 `Ctrl+S` (Windows/Linux) 或 `Cmd+S` (Mac)
   - 或選擇 File > Save

2. **應用程式檢測變更**
   - 返回應用程式
   - 應用程式會檢測到 .usda 文件已更改
   - 會顯示提示詢問是否要 **Fetch**（獲取）更新

3. **獲取更新**
   - 點擊 **Fetch** 按鈕
   - 應用程式會重新載入文件
   - 新資產會出現在場景中

## 工作流程優勢

### 精確控制

- ✅ **精確座標**：可以精確設定資產位置
- ✅ **批量操作**：可以快速添加多個資產
- ✅ **版本控制**：ASCII 格式適合版本控制

### 程式化方法

這個工作流程展示了：
- 如何通過編輯文件添加資產
- OpenUSD 的靈活性和可讀性
- 替代 UI 操作的程式化方法

## 進階技巧

### 1. 批量添加資產

可以複製多個 def 語句並修改每個的位置：

```usda
def "container_f15_01" (
    prepend references = @./assets/container_f15.usd@
)
{
    double3 xformOp:translate = (100, 0, 50)
    uniform token[] xformOpOrder = ["xformOp:translate"]
}

def "container_f15_02" (
    prepend references = @./assets/container_f15.usd@
)
{
    double3 xformOp:translate = (200, 0, 50)
    uniform token[] xformOpOrder = ["xformOp:translate"]
}

def "container_f15_03" (
    prepend references = @./assets/container_f15.usd@
)
{
    double3 xformOp:translate = (300, 0, 50)
    uniform token[] xformOpOrder = ["xformOp:translate"]
}
```

### 2. 修改旋轉和縮放

除了位置，還可以修改：
- **旋轉**：`xformOp:rotateXYZ`
- **縮放**：`xformOp:scale`

### 3. 使用變體

可以在 def 語句中添加變體：

```usda
def "AssetName" (
    prepend references = @./assets/asset.usd@
    variants = {
        string variantSet = "variantValue"
    }
)
```

## 注意事項

### 語法正確性

- 確保語法正確
- 檢查括號和大括號是否匹配
- 確保座標格式正確：`(X, Y, Z)`

### 文件路徑

- 確保引用的 USD 文件路徑正確
- 相對路徑相對於 .usda 文件的位置
- 絕對路徑也可以使用

### 備份

- 編輯前先備份原始文件
- 使用版本控制系統追蹤變更

## 常見問題

### Q: 應用程式沒有檢測到變更？

**A**: 
- 確認文件已保存
- 嘗試手動重新載入場景
- 檢查文件是否在應用程式外部被修改

### Q: 新資產沒有出現？

**A**: 
- 檢查語法是否正確
- 確認座標值是否合理
- 查看應用程式的錯誤訊息

### Q: 可以編輯二進位 .usd 文件嗎？

**A**: 
- 不建議直接編輯二進位文件
- 先轉換為 .usda 格式
- 編輯後可以轉換回 .usd 格式

## 下一步

在下一模組中，您將探索：
- 更多範例擴展
- 為數位孿生應用程式添加互動功能
- 自訂和擴展應用程式功能

## 相關資源

- [複製資產指南](DUPLICATE_ASSETS_GUIDE.md)
- [Measure 擴展指南](MEASURE_EXTENSION_GUIDE.md)
- [USD 探索指南](docs/USD_EXPLORATION_GUIDE.md)
- [OpenUSD 官方文件](https://openusd.org/)
