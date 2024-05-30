# Hollow Triangle Pattern

這是一個簡單的Python程式,用於根據輸入的數字繪製一個空心正三角形圖案。該程式是為Cathay Bank的一個面試問題而設計的。

## 問題描述

設計一個函數,接受一個數字作為輸入,並以 `*` 字符輸出對應邊長的空心正三角形。

例如,輸入為 `3` 時,輸出應為:

## 解決方案

### 邊界條件

- 輸入數字必須在 1 到 10 之間(包括 1 和 10)。

### 異常處理

- 如果輸入的不是一個有效的整數,程式會拋出 `ValueError` 異常。
- 如果輸入的數字超出範圍(小於 1 或大於 10),程式會拋出 `InputOutOfRangeException` 自定義異常。

### 實作細節

1. 定義一個自定義異常 `InputOutOfRangeException`。
2. 實作 `hollow_triangle` 函數,接受一個整數作為輸入:
   - 驗證輸入是否為有效的 1 到 10 之間的整數,如果不是則拋出相應的異常。
   - 使用兩個迴圈,一個用於控制行數,另一個用於控制列數。
   - 對於每一行,根據行號和三角形邊長計算出需要輸出的字串,包括空格和 `*` 字符。
   - 將計算出的字串輸出到控制台。

### 執行環境

- Python 版本: 3.9.6
- 需要安裝的套件: `pytest`(用於單元測試)

### 使用方式

1. 克隆存儲庫: git clone https://github.com/your-username/hollow-triangle.git
2. 導航到專案目錄:cd hollow-triangle
3. 執行程式: python hollow_triangle.py
4. 執行單元測試:pytest test_hollow_triangle.py

該程式的目的是展示Python程式設計和單元測試的基本能力。歡迎查看源代碼並提出任何建議或改進意見。