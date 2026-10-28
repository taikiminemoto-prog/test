#!/usr/bin/env python3
"""価格アンケート（PSM分析 / Van Westendorp 法）を集計する。

4つの価格を聞いたアンケートのCSVから、受け入れられる価格の範囲と、
理想価格・妥協価格を出す。標準ライブラリだけで動く。

使い方:
    python3 psm.py answers.csv
    python3 psm.py answers.csv --json

CSV の列（1行目は見出し。英語・日本語どちらでもよい）:
    too_cheap     / 安すぎる : 安すぎて品質が不安になる価格
    cheap         / 安い     : 安い（お得だ）と感じる価格
    expensive     / 高い     : 高いと感じ始める価格
    too_expensive / 高すぎる : 高すぎて買わない価格

4本の線の交点（日本でよく使われる定義）:
    下限（最低品質保証価格）: 「安すぎる」と「高い」が交わる価格
    理想価格                : 「安すぎる」と「高すぎる」が交わる価格
    妥協価格                : 「安い」と「高い」が交わる価格
    上限（最高価格）         : 「安い」と「高すぎる」が交わる価格
"""

import argparse
import csv
import json
import sys

COLUMNS = (
    ("too_cheap", "安すぎる"),
    ("cheap", "安い"),
    ("expensive", "高い"),
    ("too_expensive", "高すぎる"),
)
POINTS = (
    ("lower", "下限（最低品質保証価格）"),
    ("optimal", "理想価格"),
    ("indifference", "妥協価格"),
    ("upper", "上限（最高価格）"),
)
SMALL_SAMPLE = 30


def parse_price(text):
    cleaned = (text or "").strip()
    for mark in (",", "，", "円", "¥", "￥", "$"):
        cleaned = cleaned.replace(mark, "")
    return float(cleaned) if cleaned else None


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        picked = []
        for names in COLUMNS:
            match = next((h for h in headers if h.strip() in names), None)
            if match is None:
                sys.exit(f"列が見つかりません: {' / '.join(names)}（今の見出し: {', '.join(headers)}）")
            picked.append(match)

        rows, dropped = [], 0
        for record in reader:
            try:
                prices = [parse_price(record[h]) for h in picked]
            except ValueError:
                dropped += 1
                continue
            # 空欄がある回答や、4つの価格の大小が逆になっている回答は使わない
            if None in prices or not (prices[0] <= prices[1] <= prices[2] <= prices[3]) or prices[0] == prices[3]:
                dropped += 1
                continue
            rows.append(prices)
    return rows, dropped


def crossing(grid, falling, rising):
    """価格が上がると減る人数（falling）と、増える人数（rising）が交わる価格を返す。

    2本の線が同じ値のまま続く区間（どちらも0人の区間など）で交わるときは、
    その区間の真ん中を返す。区間の端を返すと、別の交点と同じ値になりやすいため。
    """
    gaps = [falling(price) - rising(price) for price in grid]
    for i, gap in enumerate(gaps):
        if gap > 0:
            continue
        if gap < 0:
            if i == 0:
                return grid[0]
            return grid[i - 1] + (grid[i] - grid[i - 1]) * gaps[i - 1] / (gaps[i - 1] - gap)
        end = i
        while end + 1 < len(gaps) and gaps[end + 1] == 0:
            end += 1
        return (grid[i] + grid[end]) / 2
    return None


def analyze(rows):
    too_cheap, cheap, expensive, too_expensive = zip(*rows)

    def count_at_or_above(values):
        return lambda price: sum(v >= price for v in values)

    def count_at_or_below(values):
        return lambda price: sum(v <= price for v in values)

    grid = sorted({v for row in rows for v in row})
    return {
        "lower": crossing(grid, count_at_or_above(too_cheap), count_at_or_below(expensive)),
        "optimal": crossing(grid, count_at_or_above(too_cheap), count_at_or_below(too_expensive)),
        "indifference": crossing(grid, count_at_or_above(cheap), count_at_or_below(expensive)),
        "upper": crossing(grid, count_at_or_above(cheap), count_at_or_below(too_expensive)),
    }


def fmt(value):
    if value is None:
        return "交点なし"
    return f"{value:,.0f}" if abs(value) >= 100 else f"{value:,.2f}"


def main():
    parser = argparse.ArgumentParser(description="価格アンケート（PSM分析）を集計する")
    parser.add_argument("csv", help="回答のCSVファイル")
    parser.add_argument("--json", action="store_true", help="結果をJSONで出す")
    args = parser.parse_args()

    rows, dropped = load(args.csv)
    if not rows:
        sys.exit(f"使える回答がありません（除外: {dropped} 件）")
    points = analyze(rows)

    if args.json:
        print(json.dumps({"responses": len(rows), "dropped": dropped, **points}, ensure_ascii=False, indent=2))
        return

    print(f"使った回答: {len(rows)} 件（除外: {dropped} 件。空欄や、4つの価格の大小が逆の回答）")
    for key, label in POINTS:
        print(f"{label}: {fmt(points[key])}")
    print(f"受け入れられる範囲: {fmt(points['lower'])} 〜 {fmt(points['upper'])}")
    if len(rows) < SMALL_SAMPLE:
        print(f"※ 回答が {SMALL_SAMPLE} 件未満なので、傾向として扱ってください。")


if __name__ == "__main__":
    main()
