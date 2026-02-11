# Hello World Next.js App

シンプルなNext.js（App Router）アプリケーションです。トップページに「Hello World」と説明文が表示されます。

## 📁 ファイル構成

```
.
├── app/                      # App Router のディレクトリ
│   ├── layout.tsx           # ページ全体のレイアウト
│   ├── page.tsx             # トップページ（/）
│   └── globals.css          # グローバルスタイル
├── package.json             # プロジェクトの依存関係
├── tsconfig.json            # TypeScript設定
├── next.config.js           # Next.js設定
├── .eslintrc.json           # ESLint設定
└── .gitignore               # Gitで無視するファイル
```

## 🚀 セットアップと実行方法

### 1. 依存関係をインストール
\`\`\`bash
npm install
\`\`\`

### 2. 開発サーバーを起動
\`\`\`bash
npm run dev
\`\`\`

ブラウザで http://localhost:3000 にアクセスするとアプリが表示されます。

### 3. 本番用にビルド
\`\`\`bash
npm run build
npm start
\`\`\`

## 📝 各ファイルの説明

### package.json
プロジェクトのメタデータと依存パッケージを管理します。
- `dev`: 開発サーバーを起動
- `build`: 本番用にビルド
- `start`: 本番サーバーを起動
- `lint`: コード品質をチェック

### tsconfig.json
TypeScriptのコンパイル設定を定義します。

### next.config.js
Next.jsの動作設定を定義します。

### app/layout.tsx
すべてのページの外側を囲むレイアウト。HTMLタグやメタデータを定義します。

### app/page.tsx
トップページ（/）のコンポーネント。「Hello World」と説明文を表示します。

### app/globals.css
全ページで適用されるグローバルなCSS。

## 🎯 主な特徴

- ✨ **Next.js 15** の最新版
- 🎨 **App Router** 対応（Pages Routerではなく）
- 📘 **TypeScript** で安全なコード
- 🧹 **ESLint** でコード品質を確保
- 📱 シンプルでわかりやすい構成

## 📚 Next.js について

Next.jsはReactベースのフレームワークで、以下の機能を提供します：
- サーバーサイドレンダリング（SSR）
- 静的サイト生成（SSG）
- API ルート
- ファイルベースのルーティング

詳しくは [Next.js公式ドキュメント](https://nextjs.org) を参照してください。
