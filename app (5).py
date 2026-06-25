import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Dino-Raptor-Blue-Killer",
    page_icon=":dragon:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
  #MainMenu, header, footer { visibility: hidden; }
  .block-container { padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

GAME_HTML = open("game.html", "r", encoding="utf-8").read()
components.html(GAME_HTML, height=800, scrolling=False)
