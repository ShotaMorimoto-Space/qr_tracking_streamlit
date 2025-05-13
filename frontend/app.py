import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from frontend.components.generate_uids import generate_uids_ui
from frontend.components.access_logs import access_logs_ui

st.title("DMトラッキング管理システム")

menu = st.sidebar.selectbox(
    "メニューを選択してください",
    ("UID一括生成", "アクセスログ一覧")
)

st.write("ポートの値:", st.secrets["database"]["port"])
st.write("ポートの型:", type(st.secrets["database"]["port"]))


if menu == "UID一括生成":
    generate_uids_ui()
elif menu == "アクセスログ一覧":
    access_logs_ui()
