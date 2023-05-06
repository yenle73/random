import streamlit as st
import numpy as np
import bs4 as bs
import urllib.request
import pandas as pd
import time
from PIL import Image

link = "https://en.wikipedia.org/wiki/List_of_Vietnamese_dishes"

source = urllib.request.urlopen(link).read()
soup = bs.BeautifulSoup(source,'lxml')

tables = soup.find_all('table',class_='wikitable sortable')

df1 = pd.read_html(str(tables[0]))[0]
df2 = pd.read_html(str(tables[1]))[0]
df3 = pd.read_html(str(tables[2]))[0]
df4 = pd.read_html(str(tables[3]))[0]
df5 = pd.read_html(str(tables[4]))[0]
df6 = pd.read_html(str(tables[5]))[0]
df7 = pd.read_html(str(tables[6]).replace("'1\"\'",'"1"'))[0]

df = pd.concat([df1, df2, df3, df4, df5, df6, df7])

df_name = df[['Name']]

st.markdown("<h1 style='text-align: center; color: black;'>Hôm nay ăn gì??</h1>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.write(' ')
with col2:
    st.markdown("![Alt Text](https://media.giphy.com/media/jKaFXbKyZFja0/giphy.gif)")
with col3:
    st.write(' ')
with col4:
    st.write(' ')

_, _, _, col, _, _, _ = st.columns([1]*6+[1.18])
button = col.button('Click!')

if button:
    with st.spinner('Processing...'):
        time.sleep(1)
        result = np.random.choice(df_name['Name'])
    col.markdown(f"<h4 style='color: black;'>{result}</h4>", unsafe_allow_html=True)