import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt

st.title("🎈 My first dashboard")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("Hellow *Dashboard!*")

#Load data
@st.cache_data
def load_data():
    return pd.read_csv("https://github.com/dataprofessor/population-dashboard/raw/master/data/us-population-2010-2019-reshaped.csv", index_col=0)

df=load_data()

st.header("1. Inspect the data 🎈")
st.write("'st.data_editor'allows us to display AND edit data")
st.data_editor(df)

st.header("2. Get started with a simple bar chart 📊")
st.write("Let's start the US state population data from the year 2019")
st.bar_chart(df[['year','states','population']],
            x='states',
            y='population')

st.header("3. Now make it interactive 🪄")
st.write("It's your turn to select a year")

# Using st.selectbox
# selected_year=st.selectbox("Select a year",
#                           list(df.year.unique())[::-1])

# Using st.slider
# selected_year=st.slider("Select a year", 2010,2019)

# Using st.number_input
selected_year=st.number_input("Enter a year",
                              placeholder="Enter a year from 2010-2019",
                              value=2019)

if selected_year:
    df_select_year = df[df.year==selected_year]

    # Display chart
    st.bar_chart(df_select_year,
                 x='states',
                 y= 'population')

st.header("4. How about a line chart 📈")
st.write("Track changes over time")
df_line_chart=df.copy()
df_line_chart['year']=df_line_chart['year'].astype(str)
c=(
        alt.Chart(df_line_chart)
        .mark_line()
        .encode(x=alt.X('year'),
                y=alt.Y('population'),
                color='states')
)
st.altair_chart(c,use_container_width=True)

st.header("5. Sprinkle in more interactivity ✨")
st.write("Use 'st.multiselect' and 'st.slider' for data filter before chart creation")
states=st.multiselect("Pick your states",
                      list(df.states.unique())[::-1],
                      "California")
data_range=st.slider("Pick your date range",
                     2010,2019,
                     (2010,2019))
if states:
    chart_data=df[df['states'].isin(states)]
    chart_data=chart_data[chart_data['year'].between(data_range[0],data_range[1])]
    chart_data['year']=chart_data['year'].astype(str)
    c=(
        alt.Chart(chart_data)
        .mark_line()
        .encode(x=alt.X('year'),
                y=alt.Y('population'),
                color='states')
    )

    st.altair_chart(c,use_container_width=True)
