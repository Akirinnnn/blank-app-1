import streamlit as st
left, right=st.columns(2)
left.image("Bild.jpg", width=200)
right.header("Kira Akimov")
right.write("""
            🏡 Hertha-Firnberg-Straße7
            🖨️ 1100 Wien
            📱 Mobil: +43 066 08613308
            📧 kiraakimov2@gmail.com
""")

st.write("")
st.write("")

st.header("IT-Kompetenz", anchor=False, divider="blue")

st.markdown("""
            👩‍💻 Office: Guter Umfang mit Powerpoint, Excel und Word
            💻 Programmier Sprachen: HTML, Python
            👩‍💼 Programmierung: Praktische Erfahrung in Python, Entwicklung kleine Website
            📊 Eigene Projekt: konzeption und Umsetzung verschiedener Projekte inklusive diese Website
            🎒 Schule: Fach Bereich IT mit positivem Erfolg
            """,)

st.write("")
st.write("")

st.header("Schulbildung", anchor=False, divider="blue")
st.markdown("🛠️ Berufspraktische Tage 1:Gesundheitszentrum Favoriten, Wien - 18./22.11.2024")

st.write("")

st.header("Sprachen", anchor=False, divider="blue")

import streamlit as st

st.subheader("English", anchor=False)
levels= ("A1", "A2", "B1", "B2", "C1", "C2")
levels= st.select_slider("", options=levels, value="B2")

st.subheader("Ukrainian", anchor=False)
levels = ("A1", "A2", "B1", "B2", "C1", "C2")
levels=st.select_slider("",options=levels, value="B1")

