import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@st.cache_resource
def get_streamlit_db():
    db_user = st.secrets["database"]["user"]
    db_pass = st.secrets["database"]["password"]
    db_host = st.secrets["database"]["host"]
    db_port = st.secrets["database"]["port"]
    db_name = st.secrets["database"]["name"]

    db_url = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(db_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()