import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# アプリ設定
st.set_page_config(page_title="Glink", layout="wide")
st.title("📬 Glink")

# スタイリングのためのCSS
st.markdown("""
<style>
    .email-item {
        border: 1px solid #e6e6e6;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 10px;
        background-color: white;
    }
    .email-item:hover {
        border-color: #1E88E5;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .email-subject {
        font-weight: bold;
        font-size: 16px;
    }
    .email-sender {
        color: #555;
        font-size: 14px;
    }
    .email-preview {
        color: #777;
        font-size: 14px;
        margin-top: 5px;
    }
    .label-item {
        display: inline-block;
        padding: 3px 8px;
        border-radius: 12px;
        font-size: 12px;
        margin-right: 5px;
        color: white;
    }
    .analyze-result {
        background-color: #f7f9fc;
        border-left: 4px solid #4285F4;
        padding: 15px;
        margin: 10px 0;
        border-radius: 0 5px 5px 0;
    }
    .checkbox-item {
        margin: 5px 0;
    }
    .action-button {
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ログインしていないときはログインボタンのみ表示
if not st.experimental_user.is_logged_in:
    st.markdown("### ようこそ Glink へ！")
    st.write("Gmail連携アプリ Glink にログインしてはじめましょう。")
    if st.button("🔐 Googleでログイン"):
        st.login("google")

# ログイン済みのときの処理
if st.experimental_user.is_logged_in:
    # サイドバーのナビゲーション
    with st.sidebar:
        st.header(f"こんにちは、{st.experimental_user.name.split()[0]}さん")

        # メニュー区切り
        st.markdown("---")

        # ページリスト
        pages = ["🏠 Home", "🏷️ ラベル管理", "✉️ 自動返信", "💬 チャットボット", "🔄 Slack連携", "⚙️ Settings", "🔔 Notifications", "🚪 Logout"]

        # ページ選択の状態保持（デフォルトは Home）
        if "page" not in st.session_state:
            st.session_state.page = pages[0]

        # サイドバーのメニュー
        for page in pages[:-1]:  # Logout 以外のページ
            if st.button(page, key=f"nav_{page}"):
                st.session_state.page = page
        st.markdown("---")
        if st.button(pages[-1], key="nav_logout"):  # Logout ボタン
            st.logout()

    # メインコンテンツ - ページ切り替え
    page = st.session_state.page

    # ラベル管理ページ
    if page == "🏷️ ラベル管理":
        st.header("🏷️ AIラベル管理")

        # ラベル管理タブ
        tabs = st.tabs(["ラベル設定", "自動ラベリング", "ラベル一覧", "メール分析"])

        # タブ1: ラベル設定
        with tabs[0]:
            st.subheader("新しいラベルの作成")
        # タブ2: 自動ラベリング
        with tabs[1]:
            st.subheader("AIを活用した自動ラベリングルール")

        # タブ3: ラベル一覧
        with tabs[2]:
            st.subheader("ラベル付きメール一覧")

        # タブ4: メール分析
        with tabs[3]:
            st.subheader("AIメール分析")

    # 自動返信ページ
    elif page == "✉️ 自動返信":
        st.header("✉️ 自動返信")

    # チャットボットページ
    elif page == "💬 チャットボット":
        st.header("💬 チャットボット")

        st.markdown("""
        このページでは、受信したメールに対してチャット形式で返信内容を作成したり、
        会話ログを参照する機能を提供する予定です。
        """)

        st.info("※ 現在、このページは開発中です。今後のアップデートにご期待ください。")

        # 仮のチャットUI
        with st.chat_message("user"):
            st.write("こんにちは、サポートをお願いできますか？")

        with st.chat_message("assistant"):
            st.write("はい、どういったご用件でしょうか？")

    # Slack連携ページ
    elif page == "🔄 Slack連携":
        st.header("🔄 Slack連携")

        st.markdown("""
        このページでは、Slackとの連携を行い、メールの受信や送信をSlackチャンネルで行う機能を提供します。
        """)

        st.info("※ 現在、このページは開発中です。今後のアップデートにご期待ください。")

    # Settings ページ
    elif page == "⚙️ Settings":
        st.header("⚙️ Settings")

        st.markdown("""
        このページでは、Glinkの設定を変更できます。
        """)

        st.info("※ 現在、このページは開発中です。今後のアップデートにご期待ください。")
    
    # Notifications ページ
    elif page == "🔔 Notifications":
        st.header("🔔 Notifications")

        st.markdown("""
        このページでは、通知設定を変更できます。
        """)

        st.info("※ 現在、このページは開発中です。今後のアップデートにご期待ください。")
    
