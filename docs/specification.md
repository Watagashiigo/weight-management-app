# Weight Management App 仕様書

## 1. 概要

体重を記録し、グラフで可視化し、他ユーザーと成果を共有できる Web アプリケーション。

## 2. 主な機能

### ユーザー管理
- 新規登録
- ログイン / ログアウト
- プロフィール編集

### 体重記録
- 体重入力
- 記録日時保存
- 体重計画像アップロード
- コメント追加

### 可視化
- 体重推移グラフ

### ソーシャル機能
- 他ユーザーの記録閲覧
- アチーブメント表示

## 3. データモデル

### Profile
- user
- bio
- favorite_sport
- icon

### WeightRecord
- user
- recorded_at
- weight
- scale_image
- comment

### Achievement
- name
- description
- icon

### UserAchievement
- user
- achievement
- achieved_at

## 4. 使用技術

- Python
- Django
- SQLite
- PostgreSQL（将来）
- Chart.js
- Pillow

## 5. 開発フェーズ

1. 設計
2. Django 基盤構築
3. 体重記録機能
4. グラフ表示
5. アチーブメント
6. UI改善
7. デプロイ