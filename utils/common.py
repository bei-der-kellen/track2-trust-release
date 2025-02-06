import streamlit as st
from sidebar import render_sidebar_logo

def initialize_page():
    """Initialize common page elements like the sidebar logo and language selector."""
    render_sidebar_logo()
    
    # Add language selector (moved from main page)
    languages = {
        "🇬🇧 English": "English",
        "🇩🇪 Deutsch": "Deutsch",
        "🇫🇷 Français": "Français"
    }
    lang_choice = st.sidebar.selectbox("Select Language", list(languages.keys()))
    return languages[lang_choice] 