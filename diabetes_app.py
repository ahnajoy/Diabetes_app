import streamlit as st

page1 = st.Page(
    page="views\web.py",
    title="Prediksi Risiko Diabetes Melitus",
    default=True,
)
page2 = st.Page(
    page="views\MassaIndex.py",
    title="Body Mass Index (BMI)",
)
page3 = st.Page(
    page="views\Solusi.py",
    title="Diabetes Melitus",
)

st.logo("assets\Untitled (1100 x 900 px)new2.png", size='large')

pg = st.navigation(pages=[page1, page2, page3])

pg.run()
