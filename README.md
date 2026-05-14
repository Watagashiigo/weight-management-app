# Weight Management App

## 概要

Weight Management Appは、日々の体重記録を継続的に管理して、
他のユーザと成果を共有できるWebアプリケーションです。
主にアメフトなど増量が必要なスポーツで体重を増やすための
コミュニティです。

ユーザは以下の情報を記録できます。

-記録日時（自動的に記録される）
-ユーザ名（自動的に記録される）
-体重（必須）
-画像（任意。体重計の画像や食事の画像など）
-コメント（任意）

また他のユーザの記録や達成したアチーブメントを確認して、
モチベーションを維持しなが継続的に体重管理を行うことを目的としています。

-----

## 主な機能 （今後変更の可能性大）

### ユーザー管理機能

- ユーザー登録
- ログイン / ログアウト
- パスワード変更
- プロフィール編集
- 自己紹介
- スポーツ・趣味の登録
- アイコン画像設定

### 体重記録機能

- 日時の自動記録
- 体重入力
- 体重計画像のアップロード
- コメント追加

### 記録一覧機能

- 表形式での一覧表示
- 日付順ソート
- 検索・フィルタ

### グラフ表示機能

- 体重推移の折れ線グラフ
- 1週間 / 1か月 / 1年表示

### 他ユーザー閲覧機能

- プロフィール閲覧
- 体重記録閲覧
- 継続日数確認
- 投稿数確認

### アチーブメント機能

例:

- 初投稿
- 7日連続記録
- 30日連続記録
- 50kg達成
- 60kg達成
- 5kg減量達成
- 100回投稿

---

## 使用技術（予定）

### バックエンド

- Python
- Django

### フロントエンド

- HTML
- CSS
- JavaScript

### データベース

- SQLite（開発）
- PostgreSQL（本番候補）

### 可視化

- Chart.js

### 画像処理

- Pillow

### バージョン管理

- Git
- GitHub

---

## 画面一覧（予定）

- トップページ
- 新規登録ページ
- ログインページ
- マイページ
- 体重記録投稿ページ
- 記録一覧ページ
- グラフページ
- 他ユーザープロフィールページ
- アチーブメント一覧ページ
- 設定ページ

---

## データモデル（概要）

### User

- username
- email
- password

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

---

## セットアップ方法（予定）

```bash
git clone https://github.com/yourname/weight-management-app.git
cd weight-management-app
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver

### 変更試し

gitの使い方を学習中。

gitの使い方を再学習。
