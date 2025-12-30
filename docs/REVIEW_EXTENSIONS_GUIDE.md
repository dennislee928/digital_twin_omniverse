# Review 模式擴展綜合指南

本指南綜合介紹 USD Explorer 模板中專為數位孿生工作流程設計的 Review 模式擴展。

## 概述

USD Explorer 模板包含多個範例擴展，專為數位孿生應用程式設計。這些擴展可以根據您的使用案例進行選擇、修改或擴展。

## Review 模式擴展

### 1. Markup 擴展

**功能**：在審查會話期間添加註解和標記

**主要特性**：
- 繪製視覺標記（圓圈、箭頭等）
- 添加文字註解
- 顏色自訂
- 導出為 PDF 或 CSV

**詳細指南**：[Markup 擴展指南](MARKUP_EXTENSION_GUIDE.md)

### 2. Waypoint 擴展

**功能**：保存場景視圖並稍後返回

**主要特性**：
- 保存視圖位置
- 快速導航到保存的視圖
- 播放列表控制
- 自動導覽功能

**詳細指南**：[Waypoint 擴展指南](WAYPOINT_EXTENSION_GUIDE.md)

### 3. Section 擴展

**功能**：創建截面視圖以查看場景內部

**主要特性**：
- 無限大的截面平面
- 可移動和旋轉
- 查看多層建築
- 分析內部結構

**詳細指南**：[Section 擴展指南](SECTION_EXTENSION_GUIDE.md)

### 4. Measure 擴展

**功能**：測量場景中的距離和角度

**主要特性**：
- 頂點測量
- 表面測量
- 邊緣測量
- 角度測量

**詳細指南**：[Measure 擴展指南](MEASURE_EXTENSION_GUIDE.md)

## 工作流程整合

### 典型審查工作流程

```
1. 載入場景 (Factory.usd)
   ↓
2. 進入 Review 模式
   ↓
3. 使用 Measure 測量距離
   ↓
4. 使用 Markup 添加註解
   ↓
5. 使用 Waypoint 保存重要視圖
   ↓
6. 使用 Section 查看內部結構
   ↓
7. 導出標記和報告
```

### 擴展組合使用

#### 測量 + 標記

1. 使用 Measure 測量距離
2. 使用 Markup 在測量位置添加註解
3. 標記需要檢查的區域

#### 視圖 + 標記

1. 使用 Waypoint 保存重要視圖
2. 在每個視圖使用 Markup 添加註解
3. 創建完整的審查路徑

#### 截面 + 測量

1. 使用 Section 創建截面視圖
2. 使用 Measure 測量截面中的尺寸
3. 分析結構和布局

## 自訂擴展

### 選擇擴展

根據您的使用案例：

- **建築審查**：Markup + Section + Measure
- **導覽演示**：Waypoint + Markup
- **結構分析**：Section + Measure
- **完整審查**：所有擴展

### 修改擴展

所有範例擴展都可以：

1. **修改 UI**
   - 調整按鈕位置和樣式
   - 自訂顏色和圖標
   - 改變布局

2. **擴展功能**
   - 添加新功能
   - 整合其他工具
   - 實現自訂工作流程

3. **整合服務**
   - 連接數據庫
   - 整合 API
   - 添加雲端功能

### 開發新擴展

可以：

1. **創建新擴展**
   - 使用 USD Explorer 模板
   - 參考現有擴展代碼
   - 實現新功能

2. **整合第三方擴展**
   - 使用 Omniverse 擴展市場
   - 整合開源擴展
   - 連接外部工具

## 擴展配置

### 啟用/禁用擴展

在應用程式的 `.kit` 文件中：

```toml
[settings.app.extensions]
excluded = [
    # "omni.kit.tool.markup",  # 禁用 Markup
    # "omni.kit.tool.waypoint",  # 禁用 Waypoint
]
```

### 擴展順序

```toml
[dependencies]
"omni.kit.tool.markup" = { order = 1000 }
"omni.kit.tool.waypoint" = { order = 2000 }
"omni.kit.tool.section" = { order = 3000 }
```

## 最佳實踐

### 1. 組織審查會話

- 使用 Waypoint 標記重要位置
- 使用 Markup 記錄問題和觀察
- 使用 Section 查看不同視角

### 2. 協作審查

- 導出 Markup 為 PDF 分享
- 保存 Waypoint 路徑供團隊使用
- 使用 Measure 數據進行報告

### 3. 效能考量

- 禁用不需要的擴展
- 優化大型場景的標記數量
- 定期清理不需要的 Waypoints

## 常見問題

### Q: 如何知道哪些擴展可用？

**A**: 
- 查看應用程式的導航欄
- 檢查 Tools 選單
- 查看 Window 選單中的擴展視窗

### Q: 可以同時使用多個擴展嗎？

**A**: 
- 是的，所有擴展可以同時使用
- 它們設計為協同工作
- 可以組合使用創建完整工作流程

### Q: 如何學習開發擴展？

**A**: 
- 查看範例擴展的源代碼
- 參考 Omniverse 擴展開發文檔
- 使用 USD Explorer 模板作為起點

## 下一步

在下一模組中，您將學習：
- 如何添加擴展到應用程式
- 擴展開發基礎
- 自訂和擴展現有功能

## 相關資源

- [Markup 擴展指南](MARKUP_EXTENSION_GUIDE.md)
- [Waypoint 擴展指南](WAYPOINT_EXTENSION_GUIDE.md)
- [Section 擴展指南](SECTION_EXTENSION_GUIDE.md)
- [Measure 擴展指南](MEASURE_EXTENSION_GUIDE.md)
- [Omniverse 擴展開發](https://docs.omniverse.nvidia.com/)
