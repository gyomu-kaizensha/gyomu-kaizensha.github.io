#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 5 tax-accountant demo pages from a shared template."""
import os, json

COMPANIES = [
    {
        "slug": "miraic-demo",
        "company": "みらいコンサルティンググループ",
        "subtitle": "顧問先・コンサル案件 業務管理",
        "address": "東京都千代田区（デモ用住所）",
        "tel": "03-XXXX-XXXX",
        "icon": "💼",
        "primary": "#0277bd",
        "primary_dark": "#01579b",
        "accent": "#00bfa5",
        "secondary": "#e1f5fe",
        "yellow": "#00bfa5",
        "kpis": [
            ("4", "urgent", "🔴 進行中コンサル案件（要対応）"),
            ("3", "soon", "🟠 申告期限 30日以内"),
            ("8/12", "normal", "📊 月次レポート進捗"),
            ("2", "accent", "✨ 今月の新規顧問先"),
        ],
        "section1_title": "🔴 進行中コンサル案件（要対応）",
        "section2_title": "🟠 申告期限が近い顧問先",
        "core_feature": "コンサル案件の進捗管理・顧問先別収支管理",
        "clients": [
            {"name":"株式会社ミライ製作所","addr":"東京都千代田区","work":"事業承継コンサル","date":"2026-04-01","next":"2026-05-15","status":"urgent"},
            {"name":"合同会社ヴィジョン","addr":"東京都港区","work":"組織再編支援","date":"2026-03-20","next":"2026-05-12","status":"urgent"},
            {"name":"イノベート株式会社","addr":"神奈川県横浜市","work":"M&Aアドバイザリー","date":"2026-02-10","next":"2026-05-20","status":"soon"},
            {"name":"スカイラボ株式会社","addr":"東京都新宿区","work":"法人税申告（3月決算）","date":"2026-04-30","next":"2026-05-31","status":"soon"},
            {"name":"グリーンテック合同会社","addr":"埼玉県さいたま市","work":"月次顧問・記帳代行","date":"2026-04-15","next":"2026-06-15","status":"ok"},
            {"name":"フロンティア株式会社","addr":"東京都品川区","work":"創業支援・補助金申請","date":"2026-03-05","next":"2026-07-01","status":"ok"},
        ],
    },
    {
        "slug": "mirai-partners-demo",
        "company": "税理士法人みらいパートナーズ",
        "subtitle": "顧客フォロー・伴走支援 管理",
        "address": "東京都中央区（デモ用住所）",
        "tel": "03-XXXX-XXXX",
        "icon": "🤝",
        "primary": "#1a3a8e",
        "primary_dark": "#102566",
        "accent": "#ff6b35",
        "secondary": "#e8eef9",
        "yellow": "#ff6b35",
        "kpis": [
            ("32", "normal", "👥 顧問契約数"),
            ("5", "soon", "🟠 申告期限 30日以内"),
            ("3", "accent", "✨ 今月の新規ご相談"),
            ("9", "urgent", "📅 月次面談予定"),
        ],
        "section1_title": "🌱 きっかけ別 新規ご相談（要フォロー）",
        "section2_title": "🟠 申告期限が近い顧問先",
        "core_feature": "お客様のきっかけ別管理・伴走型支援の進捗管理",
        "clients": [
            {"name":"田村 和也 様","addr":"きっかけ：相続のご相談","work":"相続税申告・遺産分割","date":"2026-04-25","next":"2026-05-20","status":"urgent"},
            {"name":"株式会社ハーモニー","addr":"きっかけ：開業相談","work":"創業支援・記帳指導","date":"2026-04-10","next":"2026-05-15","status":"urgent"},
            {"name":"佐々木 美和 様","addr":"きっかけ：確定申告","work":"個人事業主 月次顧問","date":"2026-03-15","next":"2026-05-25","status":"soon"},
            {"name":"株式会社ブルーム","addr":"きっかけ：法人設立","work":"法人税申告（4月決算）","date":"2026-05-31","next":"2026-06-10","status":"soon"},
            {"name":"中村工業株式会社","addr":"きっかけ：金融機関紹介","work":"資金繰り・経営支援","date":"2026-04-01","next":"2026-07-01","status":"ok"},
            {"name":"アトリエ ノエル","addr":"きっかけ：HP問い合わせ","work":"個人事業主 顧問契約","date":"2026-03-20","next":"2026-08-01","status":"ok"},
        ],
    },
    {
        "slug": "yokohama-chuo-demo",
        "company": "横浜中央税理士法人",
        "subtitle": "顧問先・地域案件 業務管理",
        "address": "神奈川県横浜市中区（デモ用住所）",
        "tel": "045-XXX-XXXX",
        "icon": "⚓",
        "primary": "#01579b",
        "primary_dark": "#003c6b",
        "accent": "#ffc107",
        "secondary": "#e1f5fe",
        "yellow": "#ffc107",
        "kpis": [
            ("48", "normal", "👥 顧問契約数"),
            ("6", "soon", "🟠 申告期限 30日以内"),
            ("4", "accent", "✨ 地域別 新規問い合わせ"),
            ("11/15", "urgent", "📊 月次レポート進捗"),
        ],
        "section1_title": "🌊 地域別 新規問い合わせ（要対応）",
        "section2_title": "🟠 申告期限が近い顧問先",
        "core_feature": "横浜中央エリアの顧問先管理・地域密着案件管理",
        "clients": [
            {"name":"株式会社みなとみらい商会","addr":"横浜市西区","work":"法人税申告・月次顧問","date":"2026-04-20","next":"2026-05-18","status":"urgent"},
            {"name":"関内ベーカリー","addr":"横浜市中区","work":"個人事業主 確定申告","date":"2026-04-15","next":"2026-05-22","status":"urgent"},
            {"name":"株式会社元町クラフト","addr":"横浜市中区","work":"法人税申告（3月決算）","date":"2026-04-30","next":"2026-05-31","status":"soon"},
            {"name":"野毛食品工業","addr":"横浜市中区","work":"事業承継相談","date":"2026-03-10","next":"2026-06-05","status":"soon"},
            {"name":"株式会社ベイサイド","addr":"横浜市西区","work":"月次顧問・記帳代行","date":"2026-04-01","next":"2026-07-01","status":"ok"},
            {"name":"伊勢佐木モール商店","addr":"横浜市中区","work":"消費税申告・指導","date":"2026-03-25","next":"2026-08-15","status":"ok"},
        ],
    },
    {
        "slug": "asc-demo",
        "company": "税理士法人ASC",
        "subtitle": "種別別お問い合わせ・税務会計サポート管理",
        "address": "東京都新宿区（デモ用住所）",
        "tel": "03-XXXX-XXXX",
        "icon": "🏛️",
        "primary": "#1a1a1a",
        "primary_dark": "#000000",
        "accent": "#1e88e5",
        "secondary": "#e3f2fd",
        "yellow": "#1e88e5",
        "kpis": [
            ("56", "normal", "👥 顧問契約数"),
            ("7", "soon", "🟠 申告期限 30日以内"),
            ("5", "accent", "✨ 種別別 新規問い合わせ"),
            ("13/18", "urgent", "📊 月次決算進捗"),
        ],
        "section1_title": "📂 種別別 新規お問い合わせ（要対応）",
        "section2_title": "🟠 申告期限が近い顧問先",
        "core_feature": "種別別お問い合わせ管理・税務会計サポート進捗",
        "clients": [
            {"name":"株式会社オリオン技研","addr":"種別：法人顧問","work":"法人税申告・月次顧問","date":"2026-04-22","next":"2026-05-19","status":"urgent"},
            {"name":"高橋 直人 様","addr":"種別：相続税","work":"相続税申告・財産評価","date":"2026-04-05","next":"2026-05-15","status":"urgent"},
            {"name":"合同会社サンライズ","addr":"種別：法人設立","work":"法人設立・税務届出","date":"2026-04-12","next":"2026-05-25","status":"soon"},
            {"name":"森本 雅之 様","addr":"種別：確定申告","work":"個人事業主 確定申告","date":"2026-03-18","next":"2026-06-10","status":"soon"},
            {"name":"株式会社ニューウェーブ","addr":"種別：法人顧問","work":"月次顧問・記帳代行","date":"2026-04-01","next":"2026-07-01","status":"ok"},
            {"name":"白石 真由美 様","addr":"種別：贈与税","work":"贈与税申告・相談","date":"2026-03-25","next":"2026-08-01","status":"ok"},
        ],
    },
    {
        "slug": "toc-tax-demo",
        "company": "最高のIT税理士法人",
        "subtitle": "DX前向き 顧問先 業務管理",
        "address": "東京都渋谷区（デモ用住所）",
        "tel": "03-XXXX-XXXX",
        "icon": "🚀",
        "primary": "#00acc1",
        "primary_dark": "#00838f",
        "accent": "#7b1fa2",
        "secondary": "#e0f7fa",
        "yellow": "#7b1fa2",
        "kpis": [
            ("9", "urgent", "💡 DX導入 進行中案件"),
            ("4", "soon", "🟠 申告期限 30日以内"),
            ("10/14", "normal", "📊 月次レポート進捗"),
            ("3", "accent", "✨ 今月の新規顧問先"),
        ],
        "section1_title": "💡 DX導入・仕組み化 進行中案件",
        "section2_title": "🟠 申告期限が近い顧問先",
        "core_feature": "IT・DX前向きの仕組み化・顧問先別DX進捗管理",
        "clients": [
            {"name":"株式会社クラウドリンク","addr":"DX：会計freee連携","work":"クラウド会計導入支援","date":"2026-04-10","next":"2026-05-18","status":"urgent"},
            {"name":"スタートアップABC","addr":"DX：請求書電子化","work":"インボイス制度対応","date":"2026-04-15","next":"2026-05-20","status":"urgent"},
            {"name":"株式会社デジタルフォージ","addr":"DX：経費精算システム","work":"法人税申告・DX支援","date":"2026-04-30","next":"2026-05-30","status":"soon"},
            {"name":"テックパーク合同会社","addr":"DX：給与計算自動化","work":"労務・税務一括支援","date":"2026-03-20","next":"2026-06-08","status":"soon"},
            {"name":"株式会社ネオフロー","addr":"DX：仕訳自動化","work":"月次顧問・自動化支援","date":"2026-04-01","next":"2026-07-01","status":"ok"},
            {"name":"イノベートラボ","addr":"DX：ダッシュボード構築","work":"経営数値見える化","date":"2026-03-15","next":"2026-08-10","status":"ok"},
        ],
    },
]

COMPANY_EN = {
    "miraic-demo": ("Mirai Consulting Group", "Tokyo, Japan (demo)"),
    "mirai-partners-demo": ("Mirai Partners Tax Corp.", "Tokyo, Japan (demo)"),
    "yokohama-chuo-demo": ("Yokohama Chuo Tax Corp.", "Yokohama, Japan (demo)"),
    "asc-demo": ("ASC Tax Corp.", "Tokyo, Japan (demo)"),
    "toc-tax-demo": ("Top IT Tax Corp.", "Tokyo, Japan (demo)"),
}


def hex_to_rgb_str(h):
    h = h.lstrip("#")
    return f"{int(h[0:2],16)},{int(h[2:4],16)},{int(h[4:6],16)}"


# Use placeholder system: %%KEY%% to avoid Python format-string issues with CSS/JS braces.
TPL = r"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>%%COMPANY%% 業務管理システム（デモ）</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&display=swap" rel="stylesheet"/>
<style>
:root{
  --navy:%%PRIMARY_DARK%%;
  --blue:%%PRIMARY%%;
  --blue-light:%%SECONDARY%%;
  --yellow:%%YELLOW%%;
  --accent:%%ACCENT%%;
  --green:#16a34a;
  --green-light:#f0fdf4;
  --orange:#ea580c;
  --red:#dc2626;
  --gray-bg:#f3f4f8;
  --ink:#1a1a2e;
  --gray:#5a6070;
  --line:#dde3ea;
  --sidebar-w:220px;
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{font-family:'Noto Sans JP',sans-serif;color:var(--ink);background:var(--gray-bg);display:flex;flex-direction:column;-webkit-font-smoothing:antialiased}
.demo-bar{background:var(--navy);color:var(--yellow);text-align:center;padding:6px;font-size:11px;font-weight:700;letter-spacing:.1em;flex-shrink:0}
.app{display:flex;flex:1;overflow:hidden}
.sidebar{width:var(--sidebar-w);background:var(--navy);display:flex;flex-direction:column;flex-shrink:0}
.sidebar-logo{padding:20px 18px;border-bottom:1px solid rgba(255,255,255,.1)}
.sidebar-logo .company{font-size:14px;font-weight:700;color:#fff;line-height:1.4}
.sidebar-logo .system{font-size:10px;color:rgba(255,255,255,.5);margin-top:3px}
.sidebar-logo .icon{font-size:22px;margin-bottom:8px}
.nav-section{padding:12px 0}
.nav-label{font-size:10px;color:rgba(255,255,255,.35);letter-spacing:.15em;padding:8px 18px 4px;font-weight:700}
.nav-item{display:flex;align-items:center;gap:10px;padding:10px 18px;font-size:13px;color:rgba(255,255,255,.65);cursor:pointer;transition:background .15s}
.nav-item:hover{background:rgba(255,255,255,.06)}
.nav-item.active{background:rgba(255,255,255,.12);color:#fff;border-right:3px solid var(--yellow)}
.nav-item .ni{font-size:16px;width:20px;text-align:center}
.sidebar-footer{margin-top:auto;padding:16px 18px;border-top:1px solid rgba(255,255,255,.1);font-size:11px;color:rgba(255,255,255,.35);line-height:1.6}
.main{flex:1;overflow-y:auto;display:flex;flex-direction:column}
.topbar{background:#fff;border-bottom:1px solid var(--line);padding:0 24px;height:54px;display:flex;align-items:center;justify-content:space-between;flex-shrink:0}
.topbar-title{font-size:15px;font-weight:700;color:var(--navy)}
.topbar-right{display:flex;align-items:center;gap:12px}
.today-badge{font-size:12px;color:var(--gray);background:var(--gray-bg);padding:4px 12px;border-radius:4px}
.content{padding:24px;flex:1}
.page{display:none}
.page.active{display:block}
.kpi-row{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:24px}
@media(max-width:700px){.kpi-row{grid-template-columns:repeat(2,1fr)}}
.kpi{background:#fff;border-radius:8px;padding:16px 18px;border:1px solid var(--line)}
.kpi .knum{font-size:28px;font-weight:700;line-height:1;color:var(--navy)}
.kpi.urgent .knum{color:var(--red)}
.kpi.soon .knum{color:var(--orange)}
.kpi.accent .knum{color:var(--accent)}
.kpi .klabel{font-size:11px;color:var(--gray);margin-top:6px}
.card{background:#fff;border-radius:8px;border:1px solid var(--line);overflow:hidden;margin-bottom:20px}
.card-head{padding:14px 20px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--line)}
.card-title{font-size:14px;font-weight:700;color:var(--navy)}
.filter-bar{display:flex;gap:8px;align-items:center}
.f-select{border:1px solid var(--line);border-radius:5px;padding:6px 10px;font-size:12px;font-family:inherit;background:#fff}
.search-box{border:1px solid var(--line);border-radius:5px;padding:6px 10px;font-size:12px;font-family:inherit;width:140px}
.cust-table{width:100%;border-collapse:collapse}
.cust-table th{background:var(--gray-bg);padding:10px 14px;text-align:left;font-size:11px;font-weight:700;color:var(--gray);letter-spacing:.05em;border-bottom:1px solid var(--line)}
.cust-table td{padding:12px 14px;border-bottom:1px solid var(--line);font-size:13px;vertical-align:middle}
.cust-table tr:last-child td{border:none}
.cust-table tr:hover td{background:#fafbff}
.status-dot{display:inline-flex;align-items:center;gap:5px;font-size:12px;font-weight:700;padding:3px 10px;border-radius:4px}
.sd-urgent{background:#fef2f2;color:var(--red)}
.sd-soon{background:#fff7ed;color:var(--orange)}
.sd-ok{background:var(--green-light);color:var(--green)}
.action-cell{display:flex;gap:6px}
.act-btn{font-size:11px;font-weight:700;padding:5px 10px;border-radius:4px;border:none;cursor:pointer;font-family:inherit}
.act-call{background:var(--navy);color:#fff}
.act-mail{background:var(--yellow);color:#fff}
.act-est{background:var(--blue-light);color:var(--blue)}
.est-layout{display:grid;grid-template-columns:380px 1fr;gap:20px}
@media(max-width:760px){.est-layout{grid-template-columns:1fr}}
.est-form-card{background:#fff;border-radius:8px;border:1px solid var(--line);padding:20px}
.form-group{margin-bottom:14px}
.form-group label{font-size:12px;font-weight:700;color:var(--gray);display:block;margin-bottom:5px;text-transform:uppercase;letter-spacing:.05em}
.form-input,.form-select{width:100%;border:1px solid var(--line);border-radius:5px;padding:9px 11px;font-size:13px;font-family:inherit;transition:border-color .15s}
.form-input:focus,.form-select:focus{outline:none;border-color:var(--blue)}
.form-row-2{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.gen-btn{width:100%;background:var(--navy);color:#fff;border:none;padding:12px;border-radius:5px;font-size:13px;font-weight:700;cursor:pointer;font-family:inherit;margin-top:6px;transition:background .15s}
.gen-btn:hover{background:var(--blue)}
.est-preview{background:#fff;border-radius:8px;border:1px solid var(--line)}
.ep-head{padding:16px 20px;border-bottom:1px solid var(--line);display:flex;align-items:center;justify-content:space-between}
.ep-title{font-size:13px;font-weight:700;color:var(--navy)}
.ep-actions{display:flex;gap:8px}
.ep-btn{font-size:12px;font-weight:700;padding:7px 14px;border-radius:5px;border:none;cursor:pointer;font-family:inherit;display:flex;align-items:center;gap:5px}
.ep-pdf{background:var(--red);color:#fff}
.ep-print{background:var(--gray-bg);color:var(--ink);border:1px solid var(--line)}
.ep-body{padding:20px}
.ep-empty{text-align:center;padding:60px 20px;color:var(--gray);font-size:13px}
.est-doc{font-size:13px}
.est-doc-header{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:20px;padding-bottom:16px;border-bottom:2px solid var(--navy)}
.est-doc-company{font-size:16px;font-weight:700;color:var(--navy)}
.est-doc-label{font-size:20px;font-weight:700;color:var(--navy);text-align:right}
.est-doc-meta{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px;font-size:12px}
.est-doc-to{background:var(--gray-bg);padding:10px 12px;border-radius:4px;margin-bottom:14px}
.est-doc-to .to-label{font-size:10px;color:var(--gray);margin-bottom:3px}
.est-doc-to .to-name{font-size:15px;font-weight:700}
.est-table-doc{width:100%;border-collapse:collapse;margin-bottom:12px;font-size:12px}
.est-table-doc th{background:var(--navy);color:#fff;padding:8px 10px;text-align:left;font-weight:500}
.est-table-doc td{padding:8px 10px;border-bottom:1px solid var(--line)}
.est-total-row{background:var(--navy);color:#fff;border-radius:5px;padding:12px 16px;display:flex;justify-content:space-between;align-items:center;margin-top:10px}
.est-total-row .tl{font-size:12px;opacity:.8}
.est-total-row .tv{font-size:20px;font-weight:700;color:var(--yellow)}
.est-note{font-size:11px;color:var(--gray);margin-top:12px;line-height:1.7;padding:10px;background:var(--gray-bg);border-radius:4px}
@media(max-width:768px){
  .app{display:block}
  .sidebar{position:fixed;top:0;left:-100%;width:80%;max-width:280px;height:100%;z-index:1000;transition:left .3s ease;flex-direction:column}
  .sidebar.open{left:0}
  .overlay{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.5);z-index:999;}
  .overlay.open{display:block}
  .hamburger{display:flex;align-items:center;justify-content:center;width:40px;height:40px;cursor:pointer;font-size:20px;color:var(--ink);background:none;border:none;}
  .topbar{position:sticky;top:0;z-index:100;}
  .main{width:100%;overflow-x:hidden;}
  .sidebar-logo{padding:12px 16px}
  .nav-section{padding:4px 0}
  .nav-item{padding:8px 12px;font-size:11px}
  .nav-label{display:none}
  .sidebar-footer{display:none}
  .topbar{padding:0 12px;height:44px}
  .topbar-title{font-size:13px}
  .content{padding:12px}
  .kpi-row{grid-template-columns:repeat(2,1fr);gap:8px;margin-bottom:12px}
  .kpi .knum{font-size:20px}
  .card-head{padding:10px 12px;flex-wrap:wrap;gap:6px}
  .card-title{font-size:12px}
  .cust-table th,.cust-table td{padding:7px 8px;font-size:11px}
  .cust-table{display:block;overflow-x:auto;-webkit-overflow-scrolling:touch}
  .status-dot{font-size:10px;padding:2px 6px}
  .act-btn{font-size:10px;padding:4px 7px}
  .action-cell{flex-wrap:wrap}
  .est-form-card{padding:12px}
  .form-row-2{grid-template-columns:1fr}
  .gen-btn{padding:12px;font-size:13px}
  .ep-body{padding:12px}
  .est-doc{font-size:11px}
  .est-doc-meta{grid-template-columns:1fr}
  .est-doc-header{flex-direction:column;gap:8px}
  .est-doc-label{text-align:left;font-size:14px}
  .est-total-row .tv{font-size:16px}
  .filter-bar{flex-wrap:wrap}
  .nav-section{display:flex;flex-direction:row;overflow-x:auto;padding:4px 0;gap:0}
  .nav-item{white-space:nowrap;flex-shrink:0;padding:10px 14px}
  .nav-item.active{border-right:none;border-bottom:3px solid}
}
@media(max-width:480px){
  .kpi-row{grid-template-columns:1fr 1fr}
  .demo-bar{font-size:10px;padding:4px}
}
@media(min-width:769px){.hamburger{display:none}}
</style>
</head>
<body>
<div class="overlay" id="overlay" onclick="closeSidebar()"></div>
<div class="demo-bar">⚠️ デモ画面 — %%COMPANY%%様向け 業務管理システム イメージ（業務改善舎 作成）</div>

<div class="app">
  <aside class="sidebar">
    <div class="sidebar-logo">
      <div class="icon">%%ICON%%</div>
      <div class="company">%%COMPANY%%</div>
      <div class="system">%%SUBTITLE%%</div>
    </div>
    <nav class="nav-section">
      <div class="nav-label">メニュー</div>
      <div class="nav-item active" onclick="showPage('dashboard')">
        <span class="ni">🏠</span>ダッシュボード
      </div>
      <div class="nav-item" onclick="showPage('customers')">
        <span class="ni">👥</span>顧問先管理
      </div>
      <div class="nav-item" onclick="showPage('calendar')">
        <span class="ni">📅</span>申告期限カレンダー
      </div>
      <div class="nav-item" onclick="showPage('monthly')">
        <span class="ni">📊</span>月次試算表 進捗
      </div>
      <div class="nav-item" onclick="showPage('estimate')">
        <span class="ni">📋</span>見積書作成
      </div>
    </nav>
    <div class="sidebar-footer">
      %%COMPANY%%<br>
      %%ADDRESS%%<br>
      %%TEL%%
    </div>
  </aside>

  <div class="main">
    <div class="topbar">
      <button class="hamburger" onclick="openSidebar()">☰</button>
      <div class="topbar-title" id="pageTitle">ダッシュボード</div>
      <div class="topbar-right">
        <span class="today-badge" id="todayDate"></span>
      </div>
    </div>

    <div class="content">

      <div class="page active" id="page-dashboard">
        <div style="background:#fff;border-radius:8px;border:1px solid var(--line);padding:14px 18px;margin-bottom:16px;font-size:12px;color:var(--gray)">
          <span style="color:var(--navy);font-weight:700">核心機能：</span>%%CORE_FEATURE%%
        </div>
        <div class="kpi-row">
%%KPI_CARDS%%
        </div>

        <div class="card">
          <div class="card-head">
            <span class="card-title">%%SECTION1_TITLE%%</span>
          </div>
          <table class="cust-table">
            <thead>
              <tr><th>顧問先 / お客様</th><th>業務内容</th><th>受任日</th><th>次回対応</th><th>操作</th></tr>
            </thead>
            <tbody>
%%SECTION1_ROWS%%
            </tbody>
          </table>
        </div>

        <div class="card">
          <div class="card-head">
            <span class="card-title">%%SECTION2_TITLE%%</span>
          </div>
          <table class="cust-table">
            <thead>
              <tr><th>顧問先 / お客様</th><th>業務内容</th><th>受任日</th><th>次回対応</th><th>操作</th></tr>
            </thead>
            <tbody>
%%SECTION2_ROWS%%
            </tbody>
          </table>
        </div>
      </div>

      <div class="page" id="page-customers">
        <div class="card">
          <div class="card-head">
            <span class="card-title">顧問先管理</span>
            <div class="filter-bar">
              <select class="f-select" onchange="filterCustomers(this.value)">
                <option value="all">すべて</option>
                <option value="urgent">🔴 要対応</option>
                <option value="soon">🟠 もうすぐ</option>
                <option value="ok">🟢 余裕あり</option>
              </select>
              <input class="search-box" type="text" placeholder="顧問先名で検索..." oninput="searchCustomers(this.value)"/>
            </div>
          </div>
          <table class="cust-table" id="custTable">
            <thead>
              <tr><th>顧問先</th><th>業務内容</th><th>受任日</th><th>次回対応</th><th>状態</th><th>操作</th></tr>
            </thead>
            <tbody id="custBody"></tbody>
          </table>
        </div>
      </div>

      <div class="page" id="page-calendar">
        <div class="card">
          <div class="card-head">
            <span class="card-title">📅 申告期限カレンダー</span>
          </div>
          <table class="cust-table">
            <thead><tr><th>期限</th><th>顧問先</th><th>申告種別</th><th>状態</th><th>操作</th></tr></thead>
            <tbody>
%%CALENDAR_ROWS%%
            </tbody>
          </table>
        </div>
      </div>

      <div class="page" id="page-monthly">
        <div class="card">
          <div class="card-head">
            <span class="card-title">📊 月次試算表 進捗管理</span>
          </div>
          <table class="cust-table">
            <thead><tr><th>顧問先</th><th>対象月</th><th>進捗状況</th><th>担当</th><th>操作</th></tr></thead>
            <tbody>
%%MONTHLY_ROWS%%
            </tbody>
          </table>
        </div>
      </div>

      <div class="page" id="page-estimate">
        <div class="est-layout">
          <div class="est-form-card">
            <div style="font-size:14px;font-weight:700;color:var(--navy);margin-bottom:16px;padding-bottom:10px;border-bottom:1px solid var(--line)">見積書作成</div>
            <div class="form-group">
              <label>顧問先・お客様名</label>
              <input class="form-input" type="text" id="custName" placeholder="例：株式会社サンプル"/>
            </div>
            <div class="form-group">
              <label>業務の種類</label>
              <select class="form-select" id="jobType">
                <option value="">-- 選択してください --</option>
                <option value="komon_sm">月次顧問契約（小規模）</option>
                <option value="komon_md">月次顧問契約（中規模）</option>
                <option value="komon_lg">月次顧問契約（大規模）</option>
                <option value="houjin">法人税申告（決算・申告書作成）</option>
                <option value="kakutei">確定申告（個人事業主）</option>
                <option value="souzoku">相続税申告</option>
                <option value="zouyo">贈与税申告</option>
                <option value="setsuritsu">法人設立支援</option>
                <option value="kicho">記帳代行（月次）</option>
                <option value="cloud">クラウド会計導入支援</option>
              </select>
            </div>
            <div class="form-row-2">
              <div class="form-group">
                <label>件数 / 月数</label>
                <input class="form-input" type="number" id="qty" placeholder="例：12" min="1"/>
              </div>
              <div class="form-group">
                <label>難易度</label>
                <select class="form-select" id="floor">
                  <option value="1">標準</option>
                  <option value="2">複雑（追加あり）</option>
                </select>
              </div>
            </div>
            <div class="form-group">
              <label>備考</label>
              <input class="form-input" type="text" id="note" placeholder="例：分社化対応、複数拠点 等"/>
            </div>
            <button class="gen-btn" onclick="generateEstimate()">見積書を作成する</button>
          </div>

          <div class="est-preview">
            <div class="ep-head">
              <span class="ep-title">見積書プレビュー</span>
              <div class="ep-actions">
                <button class="ep-btn ep-print" id="printBtn" onclick="printEstimate()" style="display:none">🖨️ 印刷</button>
                <button class="ep-btn ep-pdf" id="pdfBtn" onclick="downloadPDF()" style="display:none">📄 PDFダウンロード</button>
              </div>
            </div>
            <div class="ep-body">
              <div class="ep-empty" id="epEmpty">← 左で業務内容を入力して<br>「見積書を作成する」を押してください</div>
              <div class="est-doc" id="estDoc" style="display:none">
                <div class="est-doc-header">
                  <div>
                    <div class="est-doc-company">%%COMPANY%%</div>
                    <div style="font-size:11px;color:var(--gray);margin-top:4px;line-height:1.7">%%ADDRESS%%<br>TEL: %%TEL%%</div>
                  </div>
                  <div>
                    <div class="est-doc-label">御 見 積 書</div>
                    <div style="font-size:11px;color:var(--gray);text-align:right;margin-top:6px" id="docDate"></div>
                  </div>
                </div>
                <div class="est-doc-to">
                  <div class="to-label">お客様</div>
                  <div class="to-name" id="docCustName">　　　　　 様</div>
                </div>
                <div class="est-doc-meta">
                  <div><span style="color:var(--gray);font-size:11px">件名：</span><span id="docJobName" style="font-weight:500"></span></div>
                  <div><span style="color:var(--gray);font-size:11px">有効期限：</span><span id="docExpiry"></span></div>
                </div>
                <table class="est-table-doc">
                  <thead><tr><th>業務項目</th><th style="text-align:right">数量</th><th style="text-align:right">単価</th><th style="text-align:right">金額</th></tr></thead>
                  <tbody id="docRows"></tbody>
                </table>
                <div class="est-total-row">
                  <span class="tl">合計金額（消費税10%込）</span>
                  <span class="tv" id="docTotal"></span>
                </div>
                <div class="est-note" id="docNote"></div>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</div>

<script>
function openSidebar(){document.querySelector('.sidebar').classList.add('open');document.getElementById('overlay').classList.add('open');}
function closeSidebar(){document.querySelector('.sidebar').classList.remove('open');document.getElementById('overlay').classList.remove('open');}
const today = new Date();
document.getElementById('todayDate').textContent = today.toLocaleDateString('ja-JP',{year:'numeric',month:'long',day:'numeric'});

function showPage(id){
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
  document.getElementById('page-'+id).classList.add('active');
  event.currentTarget.classList.add('active');
  const titles={dashboard:'ダッシュボード',customers:'顧問先管理',calendar:'申告期限カレンダー',monthly:'月次試算表 進捗',estimate:'見積書作成'};
  document.getElementById('pageTitle').textContent=titles[id];
}

const customers=%%CUSTOMERS_JSON%%;
const sLabel={urgent:'🔴 要対応',soon:'🟠 もうすぐ',ok:'🟢 余裕あり'};
const sClass={urgent:'sd-urgent',soon:'sd-soon',ok:'sd-ok'};

function renderCustomers(list){
  document.getElementById('custBody').innerHTML=list.map(c=>`
    <tr>
      <td><div style="font-weight:700">${c.name}</div><div style="font-size:11px;color:var(--gray)">${c.addr}</div></td>
      <td style="font-size:12px">${c.work}</td>
      <td style="font-size:12px">${c.date}</td>
      <td style="font-size:12px">${c.next}</td>
      <td><span class="status-dot ${sClass[c.status]}">${sLabel[c.status]}</span></td>
      <td><div class="action-cell">
        <button class="act-btn act-call">📞</button>
        <button class="act-btn act-mail">✉️</button>
        <button class="act-btn act-est" onclick="loadEstimate('${c.name}')">📋 見積</button>
      </div></td>
    </tr>`).join('');
}
renderCustomers(customers);

function filterCustomers(v){renderCustomers(v==='all'?customers:customers.filter(c=>c.status===v));}
function searchCustomers(v){renderCustomers(v?customers.filter(c=>c.name.includes(v)):customers);}

const jobs={
  komon_sm:{name:'月次顧問契約（小規模法人）',items:[
    {n:'月次訪問・打合せ',u:25000},{n:'月次試算表チェック',u:8000},{n:'税務相談対応',u:5000}]},
  komon_md:{name:'月次顧問契約（中規模法人）',items:[
    {n:'月次訪問・打合せ',u:40000},{n:'月次試算表チェック',u:12000},{n:'税務相談対応',u:8000},{n:'資金繰り表作成支援',u:5000}]},
  komon_lg:{name:'月次顧問契約（大規模法人）',items:[
    {n:'月次訪問・打合せ',u:60000},{n:'月次試算表チェック',u:18000},{n:'税務相談対応',u:12000},{n:'経営会議参加',u:15000}]},
  houjin:{name:'法人税申告（決算・申告書作成）',items:[
    {n:'決算書作成',u:80000},{n:'法人税・地方税申告書作成',u:60000},{n:'消費税申告書作成',u:30000},{n:'勘定科目内訳書作成',u:20000}]},
  kakutei:{name:'確定申告（個人事業主）',items:[
    {n:'青色申告決算書作成',u:50000},{n:'確定申告書作成',u:30000},{n:'消費税申告書作成',u:20000}]},
  souzoku:{name:'相続税申告',items:[
    {n:'財産評価（土地・建物）',u:120000},{n:'相続税申告書作成',u:200000},{n:'遺産分割協議書作成支援',u:50000},{n:'税務相談・面談',u:30000}]},
  zouyo:{name:'贈与税申告',items:[
    {n:'贈与税申告書作成',u:50000},{n:'財産評価',u:30000},{n:'税務相談',u:15000}]},
  setsuritsu:{name:'法人設立支援',items:[
    {n:'定款作成支援',u:50000},{n:'設立登記サポート',u:30000},{n:'税務署への各種届出',u:20000},{n:'創業時の税務相談',u:15000}]},
  kicho:{name:'記帳代行（月次）',items:[
    {n:'仕訳入力（〜100件）',u:15000},{n:'試算表出力',u:5000},{n:'資料整理・保管',u:3000}]},
  cloud:{name:'クラウド会計導入支援',items:[
    {n:'初期設定・科目設計',u:80000},{n:'銀行・カード連携設定',u:30000},{n:'操作レクチャー（3時間）',u:30000},{n:'運用フォロー（1ヶ月）',u:20000}]},
};

let currentEstData=null;

function loadEstimate(name){
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
  document.getElementById('page-estimate').classList.add('active');
  document.getElementById('pageTitle').textContent='見積書作成';
  document.querySelectorAll('.nav-item')[4].classList.add('active');
  document.getElementById('custName').value=name;
}

function generateEstimate(){
  const cname=document.getElementById('custName').value||'　';
  const jtype=document.getElementById('jobType').value;
  const qty=parseInt(document.getElementById('qty').value)||1;
  const floor=parseInt(document.getElementById('floor').value)||1;
  const note=document.getElementById('note').value;
  if(!jtype){alert('業務の種類を選択してください');return;}

  const job=jobs[jtype];
  let items=[...job.items.map(i=>({...i,amount:i.u*qty}))];
  if(floor===2) items.push({n:'複雑案件 追加料金',u:30000,amount:30000});

  const sub=items.reduce((s,i)=>s+i.amount,0);
  const tax=Math.floor(sub*.1);
  const total=sub+tax;

  const exp=new Date(today);
  exp.setDate(exp.getDate()+30);
  const expStr=exp.toLocaleDateString('ja-JP',{year:'numeric',month:'long',day:'numeric'});
  const todayStr=today.toLocaleDateString('ja-JP',{year:'numeric',month:'long',day:'numeric'});

  document.getElementById('docDate').textContent='発行日：'+todayStr;
  document.getElementById('docCustName').textContent=cname+' 様';
  document.getElementById('docJobName').textContent=job.name;
  document.getElementById('docExpiry').textContent=expStr;

  let rows=items.map(i=>`<tr><td>${i.n}</td><td style="text-align:right">${qty}式</td><td style="text-align:right">¥${i.u.toLocaleString()}</td><td style="text-align:right">¥${i.amount.toLocaleString()}</td></tr>`).join('');
  rows+=`<tr style="background:var(--gray-bg)"><td colspan="3" style="font-weight:500">小計</td><td style="text-align:right;font-weight:500">¥${sub.toLocaleString()}</td></tr>`;
  rows+=`<tr style="background:var(--gray-bg)"><td colspan="3">消費税（10%）</td><td style="text-align:right">¥${tax.toLocaleString()}</td></tr>`;
  document.getElementById('docRows').innerHTML=rows;
  document.getElementById('docTotal').textContent='¥'+total.toLocaleString();
  document.getElementById('docNote').textContent=
    (note?'備考：'+note+'\n':'')+'・お見積りの有効期限は発行日より30日間です。\n・正式契約前に業務範囲のすり合わせを行います。\n・上記金額には消費税（10%）が含まれています。';

  document.getElementById('epEmpty').style.display='none';
  document.getElementById('estDoc').style.display='block';
  document.getElementById('pdfBtn').style.display='flex';
  document.getElementById('printBtn').style.display='flex';

  currentEstData={cname,job,items,sub,tax,total,todayStr,expStr,note};
}

function printEstimate(){window.print();}

function downloadPDF(){
  if(!currentEstData){return;}
  const {jsPDF}=window.jspdf;
  const doc=new jsPDF({unit:'mm',format:'a4'});
  doc.setFont('helvetica');
  doc.setFillColor(%%RGB_DARK%%);
  doc.rect(0,0,210,28,'F');
  doc.setTextColor(255,255,255);
  doc.setFontSize(14);
  doc.text('%%COMPANY_EN%%',14,12);
  doc.setFontSize(9);
  doc.text('%%ADDRESS_EN%%  TEL: %%TEL%%',14,20);
  doc.setFontSize(20);
  doc.text('ESTIMATE',196,18,{align:'right'});
  doc.setTextColor(80,80,80);
  doc.setFontSize(9);
  doc.text('Date: '+currentEstData.todayStr,14,36);
  doc.text('Valid until: '+currentEstData.expStr,14,42);
  doc.setFillColor(243,244,248);
  doc.rect(14,48,182,12,'F');
  doc.setTextColor(40,40,80);
  doc.setFontSize(10);
  doc.text('To: '+currentEstData.cname+' sama',18,56);
  doc.setFontSize(9);
  doc.setTextColor(80,80,80);
  doc.text('Subject: '+currentEstData.job.name,14,68);
  doc.setFillColor(%%RGB_DARK%%);
  doc.rect(14,74,182,8,'F');
  doc.setTextColor(255,255,255);
  doc.setFontSize(8);
  doc.text('Item',16,79.5);
  doc.text('Qty',130,79.5);
  doc.text('Unit',150,79.5);
  doc.text('Amount',185,79.5,{align:'right'});
  let y=92;
  doc.setTextColor(40,40,40);
  currentEstData.items.forEach((item,i)=>{
    if(i%2===0){doc.setFillColor(249,250,251);doc.rect(14,y-5,182,8,'F');}
    doc.setFontSize(8);
    doc.text(item.n,16,y);
    doc.text('1',133,y);
    doc.text('Y'+item.u.toLocaleString(),152,y);
    doc.text('Y'+item.amount.toLocaleString(),196,y,{align:'right'});
    y+=10;
  });
  y+=4;
  doc.setFillColor(%%RGB_DARK%%);
  doc.rect(14,y,182,14,'F');
  doc.setTextColor(255,200,0);
  doc.setFontSize(12);
  doc.text('Total (incl. tax 10%):  Y '+currentEstData.total.toLocaleString(),196,y+9,{align:'right'});
  y+=22;
  doc.setTextColor(100,100,100);
  doc.setFontSize(8);
  doc.text('Note: This estimate is valid for 30 days from the date of issue.',14,y);
  if(currentEstData.note){doc.text('Remarks: '+currentEstData.note,14,y+6);}
  doc.setFillColor(243,244,248);
  doc.rect(0,280,210,17,'F');
  doc.setTextColor(130,130,130);
  doc.setFontSize(7);
  doc.text('%%COMPANY_EN%%  |  %%ADDRESS_EN%%  |  %%TEL%%',105,290,{align:'center'});
  doc.save('estimate_'+currentEstData.cname.replace(/\s/g,'')+'.pdf');
}
</script>
</body>
</html>
"""


def render(c):
    # KPI cards
    kpi_html = []
    for num, kind, label in c["kpis"]:
        cls = "kpi" + (f" {kind}" if kind in ("urgent", "soon", "accent") else "")
        kpi_html.append(
            f'          <div class="{cls}"><div class="knum">{num}</div><div class="klabel">{label}</div></div>'
        )

    def row_html(cl):
        return f"""              <tr>
                <td><div style=\"font-weight:700\">{cl['name']}</div><div style=\"font-size:11px;color:var(--gray)\">{cl['addr']}</div></td>
                <td>{cl['work']}</td>
                <td>{cl['date']}</td>
                <td>{cl['next']}</td>
                <td><div class=\"action-cell\"><button class=\"act-btn act-call\">📞</button><button class=\"act-btn act-mail\">✉️</button><button class=\"act-btn act-est\" onclick=\"loadEstimate('{cl['name']}')\">📋 見積</button></div></td>
              </tr>"""

    s1 = "\n".join(row_html(cl) for cl in c["clients"] if cl["status"] == "urgent")
    s2 = "\n".join(row_html(cl) for cl in c["clients"] if cl["status"] == "soon")

    cal_rows = []
    status_label_map = {
        "urgent": '<span class="status-dot sd-urgent">🔴 緊急</span>',
        "soon": '<span class="status-dot sd-soon">🟠 注意</span>',
        "ok": '<span class="status-dot sd-ok">🟢 余裕</span>',
    }
    for cl in c["clients"]:
        cal_rows.append(
            f'              <tr><td style="font-weight:700">{cl["next"]}</td><td>{cl["name"]}</td><td>{cl["work"]}</td><td>{status_label_map[cl["status"]]}</td><td><button class="act-btn act-est">詳細</button></td></tr>'
        )

    progress_states = ["完了", "レビュー中", "入力中", "未着手"]
    progress_label_map = {
        "完了": '<span class="status-dot sd-ok">✅ 完了</span>',
        "レビュー中": '<span class="status-dot sd-soon">📝 レビュー中</span>',
        "入力中": '<span class="status-dot sd-soon">⌨️ 入力中</span>',
        "未着手": '<span class="status-dot sd-urgent">⏳ 未着手</span>',
    }
    mon_rows = []
    for i, cl in enumerate(c["clients"]):
        state = progress_states[i % 4]
        mon_rows.append(
            f'              <tr><td style="font-weight:700">{cl["name"]}</td><td>2026年4月分</td><td>{progress_label_map[state]}</td><td>担当 A</td><td><button class="act-btn act-est">確認</button></td></tr>'
        )

    customers_json = json.dumps(c["clients"], ensure_ascii=False)
    en_name, en_addr = COMPANY_EN[c["slug"]]

    out = TPL
    repl = {
        "%%COMPANY%%": c["company"],
        "%%SUBTITLE%%": c["subtitle"],
        "%%ADDRESS%%": c["address"],
        "%%TEL%%": c["tel"],
        "%%ICON%%": c["icon"],
        "%%PRIMARY%%": c["primary"],
        "%%PRIMARY_DARK%%": c["primary_dark"],
        "%%ACCENT%%": c["accent"],
        "%%SECONDARY%%": c["secondary"],
        "%%YELLOW%%": c["yellow"],
        "%%KPI_CARDS%%": "\n".join(kpi_html),
        "%%SECTION1_TITLE%%": c["section1_title"],
        "%%SECTION2_TITLE%%": c["section2_title"],
        "%%SECTION1_ROWS%%": s1,
        "%%SECTION2_ROWS%%": s2,
        "%%CALENDAR_ROWS%%": "\n".join(cal_rows),
        "%%MONTHLY_ROWS%%": "\n".join(mon_rows),
        "%%CORE_FEATURE%%": c["core_feature"],
        "%%CUSTOMERS_JSON%%": customers_json,
        "%%RGB_DARK%%": hex_to_rgb_str(c["primary_dark"]),
        "%%COMPANY_EN%%": en_name,
        "%%ADDRESS_EN%%": en_addr,
    }
    for k, v in repl.items():
        out = out.replace(k, v)
    return out


for c in COMPANIES:
    folder = f"/tmp/gyomu-pages/{c['slug']}"
    os.makedirs(folder, exist_ok=True)
    html = render(c)
    with open(f"{folder}/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {folder}/index.html ({len(html)} bytes)")
