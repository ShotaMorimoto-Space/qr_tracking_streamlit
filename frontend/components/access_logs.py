# frontend/components/access_logs.py
import streamlit as st
import pandas as pd
from backend.db_control.database import SessionLocal
from backend.db_control import crud

def access_logs_ui():
    st.header("アクセスログ一覧")

    db = SessionLocal()

    # 全レコード取得
    logs = crud.get_all_logs(db)
    db.close()

    if not logs:
        st.info("まだアクセス記録がありません。")
        return

    # レコードをPandas DataFrameに変換
    df = pd.DataFrame([{
        "client_id": log.client_id,
        "zebra_id": log.zebra_id,
        "campaign_name": log.campaign_name,
        "uid": log.uid,
        "access_count": log.access_count,
        "last_accessed_at": log.last_accessed_at
    } for log in logs])

    # データフレーム表示
    st.dataframe(df)

    # ダウンロードボタンもつける
    csv = df.to_csv(index=False).encode('utf-8-sig')
    st.download_button(
        label="アクセスログをCSVでダウンロード",
        data=csv,
        file_name="access_logs.csv",
        mime="text/csv"
    )
