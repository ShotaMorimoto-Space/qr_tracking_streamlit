# frontend/components/generate_uids.py
import streamlit as st
import uuid
import pandas as pd
from sqlalchemy.orm import Session
from backend.db_control.database import SessionLocal
from backend.db_control import crud

def generate_uids_ui():
    st.header("UID一括生成フォーム")

    # 入力項目
    zebra_id = st.text_input("案件ID（zebra_id）")
    campaign_name = st.text_input("キャンペーン名（campaign_name）")
    target_url = st.text_input("ターゲットURL（https://から）")
    num_uids = st.number_input("発行するUID数", min_value=1, value=10, step=1)

    if st.button("UIDを生成して登録"):
        if not (zebra_id and campaign_name and target_url):
            st.error("すべての項目を入力してください。")
            return

        db = SessionLocal()
        uid_list = []  # 生成したUIDとURLを保存するリスト

        for i in range(1, num_uids + 1):
            new_uid = uuid.uuid4().hex  # 32文字ランダムUID
            crud.create_uid(
                db=db,
                client_id=i,
                zebra_id=zebra_id,
                campaign_name=campaign_name,
                uid=new_uid,
                target_url=target_url
            )

            # RenderのURL（デプロイ済みのサービスのURL）
            base_tracking_url = "https://qr-tracking-streamlit.onrender.com/track"


            # 完成版URLを組み立てる
            full_url = f"{base_tracking_url}?uid={new_uid}"
            uid_list.append({
                "client_id": i,
                "zebra_id": zebra_id,
                "campaign_name": campaign_name,
                "uid": new_uid,
                "url": full_url
            })

        db.close()
        st.success(f"{num_uids}件のUIDを登録しました！")

        # UIDリストをデータフレーム化
        df = pd.DataFrame(uid_list)

        # テーブル表示
        st.subheader("作成されたUIDリスト")
        st.dataframe(df)

        # CSVダウンロードボタン
        csv = df.to_csv(index=False).encode('utf-8-sig')
        st.download_button(
            label="CSVファイルをダウンロード",
            data=csv,
            file_name="uid_list.csv",
            mime="text/csv"
        )
