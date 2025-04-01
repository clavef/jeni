# shared.py
import streamlit as st

def show_menu(active_page: str):
    st.sidebar.title("🌟 제니앱")
    st.sidebar.page_link("home.py", label="홈", icon="🏠")
    st.sidebar.page_link("pages/audit.py", label="정산 도우미", icon="📊")
    st.sidebar.page_link("pages/insta_unfollow_check.py", label="인스타 언팔체크", icon="📱")
