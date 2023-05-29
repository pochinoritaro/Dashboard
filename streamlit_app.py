import streamlit as st
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from pyvis.network import Network
import wikipedia as wiki

wiki.set_lang("ja")
text = wiki.summary("python", auto_suggest=False)
page = wiki.page("python", auto_suggest=False)

df = pd.read_csv("data/book1.csv")
df = df.loc[df['weight'] > 10, :]


G = nx.from_pandas_edgelist(df,)
net = Network(notebook=True)
net.from_nx(G)


st.title(page.title)
st.header(page.url)
st.text(text)
st.text(page.content)
