import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Dino-Raptor-Blue-Killer",
    page_icon=":dragon:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
  #MainMenu, header, footer { visibility: hidden; }
  .block-container { padding: 0 !important; margin: 0 !important; }
</style>
""", unsafe_allow_html=True)

html_path = os.path.join(os.path.dirname(__file__), "game.html")
with open(html_path, "r", encoding="utf-8") as f:
    game_html = f.read()

components.html(game_html, height=820, scrolling=False)
