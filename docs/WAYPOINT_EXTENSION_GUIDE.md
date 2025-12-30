# Waypoint 擴展指南

本指南說明如何使用 USD Explorer 模板中的 Waypoint 擴展來保存場景視圖並稍後返回。

## 概述

Waypoint 擴展允許審查者保存場景的視圖，並在之後返回這些視圖。這對於導航大型場景、保存重要視角或創建導覽路徑非常有用。

## 步驟 1: 準備場景

### 開啟 Factory.usd

1. **開啟應用程式**
   - 啟動您的 USD Explorer 應用程式

2. **載入場景**
   - 如果尚未開啟，開啟 `Factory.usd` 檔案
   - 可以在 Examples 標籤中找到此檔案

### 進入 Review 模式

1. **切換到 Review 模式**
   - 點擊應用程式頂部的 **Review** 標籤
   - 這會進入 Review 模式

2. **確認導航欄**
   - Review 模式包含底部中央的**導航欄（Navigation Bar）**
   - 如果未顯示，使用右下角的切換按鈕開啟

## 步驟 2: 開啟 Waypoint 功能

1. **開啟 Waypoint 視圖**
   - 點擊導航欄上的 **Waypoint** 按鈕
   - 這會顯示為此場景設置的 Waypoints

2. **查看 Waypoint 顯示**
   - Waypoints 會顯示為場景中的**藍色位置標記**
   - 同時在視窗**右上角**顯示為列表

## 步驟 3: 導航到 Waypoint

### 方法 1: 從場景中點擊

1. **找到 Waypoint 標記**
   - 在場景中找到藍色的 Waypoint 位置標記

2. **點擊 Waypoint**
   - **點擊**場景中的 Waypoint 標記
   - 視窗會自動跳轉到該 Waypoint 位置

### 方法 2: 從列表選擇

1. **查看 Waypoint 列表**
   - 在視窗右上角找到 Waypoint 列表
   - 每個 Waypoint 會顯示為縮圖或圖標

2. **點擊 Waypoint 圖像**
   - **點擊**列表中的 Waypoint 圖像
   - 視窗會自動跳轉到該 Waypoint

## 步驟 4: 創建新的 Waypoint

1. **導航到新視圖**
   - 使用視窗導航工具移動到場景的另一個視圖
   - 調整視角、縮放和位置到您想要保存的視圖

2. **添加 Waypoint**
   - 點擊 **Add Waypoint** 按鈕
   - 新的 Waypoint 會創建在當前視圖位置
   - 會顯示為藍色標記並添加到列表中

## 步驟 5: 使用播放列表控制

### 播放列表功能

Waypoint 擴展包含播放列表控制功能：

1. **逐步瀏覽**
   - 使用**上一個/下一個**按鈕逐步瀏覽 Waypoints
   - 這會按順序跳轉到每個 Waypoint

2. **播放 Waypoints**
   - 使用**播放**按鈕自動播放所有 Waypoints
   - 視窗會自動在 Waypoints 之間移動
   - 可以設定播放速度和過渡效果

3. **暫停和停止**
   - 使用**暫停**按鈕暫停播放
   - 使用**停止**按鈕停止播放並返回當前視圖

### 實驗建議

- 嘗試不同的 Waypoint 順序
- 調整播放速度
- 測試過渡效果
- 創建導覽路徑

## Waypoint 功能特性

### 視覺標記

- **藍色標記**：在場景中顯示 Waypoint 位置
- **列表顯示**：在右上角顯示所有 Waypoints
- **縮圖預覽**：每個 Waypoint 有視覺預覽

### 導航功能

- **快速跳轉**：點擊即可跳轉到 Waypoint
- **順序瀏覽**：按順序瀏覽所有 Waypoints
- **自動播放**：自動播放 Waypoint 序列

### 管理功能

- **添加 Waypoint**：輕鬆創建新視圖
- **刪除 Waypoint**：移除不需要的視圖
- **重新排序**：調整 Waypoint 順序
- **重命名**：為 Waypoint 添加描述性名稱

## 工作流程提示

### 1. 創建導覽路徑

- 為重要區域創建 Waypoints
- 按照邏輯順序組織 Waypoints
- 使用播放功能創建自動導覽

### 2. 保存重要視圖

- 為關鍵檢查點創建 Waypoints
- 為不同審查階段保存視圖
- 為團隊成員標記重要位置

### 3. 組織 Waypoints

- 使用有意義的名稱
- 按功能或區域分組
- 定期清理不需要的 Waypoints

## 自訂 Waypoint 擴展

### 擴展性

像所有範例擴展一樣，Waypoint 擴展可以根據使用者需求進行自訂：

1. **UI 自訂**
   - 修改 Waypoint 標記的外觀
   - 自訂列表顯示方式
   - 調整控制按鈕布局

2. **功能擴展**
   - 添加 Waypoint 分類
   - 實現 Waypoint 分享功能
   - 添加導出/導入功能

3. **整合其他功能**
   - 與 Markup 擴展整合
   - 與 Measure 擴展整合
   - 添加註解功能

## 常見問題

### Q: Waypoint 按鈕沒有出現？

**A**: 
- 確認已進入 Review 模式
- 檢查導航欄是否已開啟
- 確認 Waypoint 擴展已啟用

### Q: 無法創建 Waypoint？

**A**: 
- 確保場景已載入
- 檢查是否有寫入權限
- 確認 Waypoint 功能已正確啟用

### Q: 如何刪除 Waypoint？

**A**: 
- 在 Waypoint 列表中選擇 Waypoint
- 使用刪除按鈕或右鍵選單
- 或使用 Delete 鍵

### Q: 可以分享 Waypoints 嗎？

**A**: 
- Waypoints 保存在場景文件中
- 保存場景即可分享 Waypoints
- 可以導出為獨立文件（如果支援）

## 下一步

在下一節中，您將學習：
- 使用 Section 擴展創建截面視圖
- 如何自訂和擴展應用程式

## 相關資源

- [Markup 擴展指南](MARKUP_EXTENSION_GUIDE.md)
- [Section 擴展指南](SECTION_EXTENSION_GUIDE.md)
- [USD Explorer 擴展文件](https://docs.omniverse.nvidia.com/)
