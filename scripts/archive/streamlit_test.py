import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

import matplotlib.pyplot as plt
import seaborn as sns
# import plotly.express as px
# from sqlalchemy import create_engine

from PIL import Image

DATA_URL = (
    "https://movie2010s.s3-us-west-1.amazonaws.com/data/movie2010s.csv"
)

st.title("Beyond Parasite")
st.markdown(
"""
This is a demo of a Streamlit app that recommends Korean Movies.
[See source code](https://github.com/happyt3/beyond-parasite/master/app.py)
""")

st.subheader('Texi Driver')
image = Image.open('Texi_Driver.jpg')
st.image(image,caption='Texi Driver',use_column_width=True)
'A widowed father and taxi driver who drives a German reporter from Seoul to Gwangju to cover the 1980 uprising, soon finds himself regretting his decision after being caught in the violence around him.'

@st.cache
def load_data():
    data = pd.read_csv()
    return data

df = pd.read_csv(DATA_URL)
# 'data', data
year_min, year_max = st.slider('Year', 2010, 2019, (2018, 2019))
df = df[np.logical_and(df['Released.1'] >= year_min, df['Released.1'] <= year_max)]

genre = st.selectbox(
    "Genre",('Adventure',
            'Drama',
            'Action',
            'Comedy',
            'Thriller/Suspense',
            'Horror',
            'Romantic Comedy'))

attribute = st.selectbox(
    "Attribute",('Topic1/Cluster1',
                'Topic2/Cluster2',
                'Tpoic3/Cluster3'))

c = alt.Chart(df[(
            df['Production Budget']>=1000000)
            #& (df['Rank']<=20)
            & (df['Genre']==genre)
            ],
    height=500).mark_circle().encode(
    x="Production Budget",y="Ratio",size='Opening Weekend Revenue',color="Theatrical Distributor",
    tooltip=['Production Budget', 'Ratio', 'Title']
    ).interactive()
st.altair_chart(c, use_container_width=True)



DATA_URL2 = (
    "https://movie2010s.s3-us-west-1.amazonaws.com/data/youtube_videoid_2019.csv"
)
df2 = pd.read_csv(DATA_URL2)

level = st.sidebar.selectbox('Level', ('Beginner','Intermediate','Advanced'))

options = [" - "] + list(set(df2['Title']))
option1 = st.sidebar.selectbox('What is your favorite 2019 movie?',options)
# 'You Option 1:', option1

remaining_options = [" - "] + list(set(df2['Title'])-set([option1]))
option2 = st.sidebar.selectbox('2nd:',remaining_options)
# 'You Option 2:', option2

remaining_options2 = [" - "] + list(set(df2['Title'])-set([option1])-set([option2]))
option3 = st.sidebar.selectbox('3rd:',remaining_options2)
# 'You Option 3:', option3

# option2 = st.sidebar.selectbox(
#     'Which 2019 movie do you choose?',
#      df2['Title'])
# 'You Option 2:', option2
#
# option3 = st.sidebar.selectbox(
#     'Which 2019 movie do you choose?',
#      df2['Title'])
# 'You Option 3:', option3
