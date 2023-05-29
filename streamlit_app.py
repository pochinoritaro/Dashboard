import streamlit as st
import pyvis
import wikipedia as wiki

wiki.set_lang("ja")
text = wiki.summary("python", auto_suggest=False)
page = wiki.page("python", auto_suggest=False)

st.title(page.title)
st.header(page.url)
st.text(text)
st.text(page.content)
