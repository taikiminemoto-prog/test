# 会社用 Claude Code 設定（たたき台）

SaaSのCS・セールス業務向け。**社内のIT・情報セキュリティ担当の確認を経てから展開すること。**

| ファイル | 置き場所 | 役割 |
|---|---|---|
| `settings.json` | 全社に強制するなら managed settings（macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`、Linux: `/etc/claude-code/managed-settings.json`、Windows: `C:\Program Files\ClaudeCode\managed-settings.json`）。チーム単位ならリポジトリの `.claude/settings.json` | 権限で禁止・確認・許可を**仕組みとして**強制する |
| `CLAUDE.md` | 作業リポジトリ／フォルダの直下 | 業務ルール（顧客データ・送信・回答方針）。文章の指示なので強制力はない |

## 設定の意図
- **deny**: 秘密情報・顧客データの読み取り、削除、sudo、外部への通信（curl/wget/ssh）、force push を禁止。
- **ask**: push、Webアクセス、MCP（外部サービス連携）は毎回確認。
- **allow**: 読み取りと閲覧系コマンドだけを自動で許可。
- `disableBypassPermissionsMode`: 確認をすべて飛ばすモードを使えなくする。

## 展開前に調整すること
- `customer-data/` など、実際のフォルダ名に合わせる。
- 使うMCP（CRM・ヘルプデスク連携など）が決まったら、`ask` の `mcp__*` を個別のツール単位の allow/ask に分ける。
- マーケ用スキル（軍配など）を載せる場合は、ライセンスで法人利用が認められているか先に確認する。
- 権限ルールの最新の書式は公式ドキュメント（https://code.claude.com/docs/en/settings）で確認する。
