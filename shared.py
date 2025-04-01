import streamlit as st

def show_menu(active_page: str):
    st.sidebar.title("🎯 제니앱")

    pages = {
        "홈": "home.py",
        "정산 도우미": "audit.py",
    }

    for label, filename in pages.items():
        if st.sidebar.button(f"{'▶' if label == active_page else '  '} {label}"):
            st.switch_page(filename)
