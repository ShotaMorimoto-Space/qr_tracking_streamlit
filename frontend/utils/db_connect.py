import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@st.cache_resource
def get_streamlit_db():
    db_user = st.secrets["database"]["user"]
    db_pass = st.secrets["database"]["password"]
    db_host = st.secrets["database"]["host"]
    db_port = int(str(st.secrets["database"]["port"]).strip())
    db_name = st.secrets["database"]["database"]

    db_url = f"postgresql://access_logs_db_user:DWAXFSpfyAxkEBu5HCs624F2fyHeKbFQ@dpg-d0gontjuibrs73fqm64g-a.singapore-postgres.render.com/access_logs_db"
    engine = create_engine(db_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()