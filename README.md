# Hollow Triangle Pattern

這是一個Python程式,用於根據輸入的數字繪製一個空心正三角形圖案。是Cathay Bank的第一題 programming question。

## 問題描述

設計一個函數,接受一個數字作為輸入,並以 `\*` 字符輸出對應邊長的空心正三角形。

例如,底下:

input(1)
\*

input(2)
  \*
 \* \*

input(3)
   \*
  \* \*
 \* \* \*

input(4)
   \*
  \* \* 
 \* \* \*
\* \* \* \*

## 解決方案
底下針對問題，思考脈絡如下

### 相關考慮條件1: 定義邊界條件（若要不設限邊界，則可以修改限制變數）

- 輸入數字必須在 1 到 10 之間(包括 1 和 10)。

### 相關考慮條件2: 異常處理

- 如果輸入的不是一個有效的整數,程式會拋出 `ValueError` 異常。
- 如果輸入的數字超出範圍(小於 1 或大於 10),程式會拋出 `InputOutOfRangeException` 自定義異常。

### 實作細節

1. 定義一個自定義異常 `InputOutOfRangeException`。
2. 實作 `hollow_triangle` 函數,接受一個整數作為輸入:
   - 驗證輸入是否為有效的 1 到 10 之間的整數,如果不是則拋出相應的異常。
   - 使用兩個迴圈,一個用於控制行數,另一個用於控制列數。
   - 對於每一行,根據行號和三角形邊長計算出需要輸出的字串,包括空格和 `\*` 字符。
   - 將計算出的字串輸出到控制台。

### 執行環境

- Python 版本: 3.9.6
- 需要安裝的套件: `pytest`(用於單元測試) （教學：https://docs.pytest.org/en/latest/getting-started.html）

### 使用方式

1. clone git repo: git clone https://github.com/ch806290/cathaybk_assignment01.git
2. 到專案目錄: cd cathaybk_assignment01
3. 執行程式: python3 cathaybk_001.py

### pytest 單元測試

1. 到專案目錄: cd cathaybk_assignment01
2. 執行單元測試:python3 -m pytest test_cathaybk_001.py