import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Superstore Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Superstore Sales & Profit Dashboard")
st.markdown("""
Diese Anwendung bettet das interaktive Tableau-Dashboard zur Analyse der Finanz- und Vertriebsdaten des **US Superstore** ein.
""")

# URL deines Dashboards von Tableau Public (mit ?:showVizHome=no&:embed=true am Ende)
tableau_url = "https://public.tableau.com/views/SuperstoreSalesDashboard_1_17918168200350/bersicht?:showVizHome=no&:embed=true"

# Einbettung per IFrame (funktioniert zuverlässig in Streamlit)
components.iframe(tableau_url, width=1200, height=850, scrolling=True)