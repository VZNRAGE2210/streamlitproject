import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide',
                   page_title='Premier league dashboard',
                   page_icon=":scoccer:")

@st.cache_data
def load():
    return pd.read_csv('premierLeague.csv')

#main code starts here 
st.image('pl.webp', use_column_width=True)
st.title("Premier League Dashboard")

df= load()
with st.expander("view raw premier league data"):
    st.dataframe(df.sample(1000)) # random record

rows, col = df.shape
c1,c2 = st.columns(2)
c1.markdown(f'###total records : {rows}')
c2.markdown(f'###total columns : {col}')

numeric_df =df.select_dtypes(include="number")
cat_df = df.select_dtypes(exclude="number")
with st.expander("column names"):
    st.markdown(f'columns with number: {", ".join(numeric_df)}')
    st.markdown(f'columns without number: {", ".join(cat_df)}')
   
# visulasization 
c1,c2 = st.columns([1,4])
xcol = st.selectbox('choose a column for x axis', numeric_df.columns)       
ycol = st.selectbox('choose a column for y axis', numeric_df.columns)       
zcol = st.selectbox('choose a column for z axis', numeric_df.columns)
color = c1.selectbox('choose colum for color', cat_df.columns)
fig = px.scatter_3d(df,x=xcol,y=ycol,z=zcol,color=color,height= 600) 
c2.plotly_chart(fig,use_container_width=True)     

st.title("Premier League Highlights")
c1,c2 = st.columns(2)
c1.video("https://www.youtube.com/watch?v=cKeL28dPzIw")
c2.markdown(''''The Premier League, England's top football division, emerged in 1992 as a breakaway from the Football League, aiming to increase revenue and competitiveness. Initially comprising 22 teams, it trimmed to 20 in 1995. Manchester United dominated the early years under manager Alex Ferguson. Arsenal's "Invincibles" went unbeaten in the 2003-04 season. The league expanded its global reach through lucrative TV deals, attracting top talent worldwide. Chelsea's emergence under owner Roman Abramovich and manager José Mourinho brought new dominance. Manchester City's financial injection transformed them into title contenders. Leicester City's miraculous title win in 2016 remains a legendary moment.''')

st.title("Premier League clubs")
clubs = df['HomeTeam'].unique() + df['AwayTeam'].unique()
clubs = sorted(set(clubs))
st.info(", ".join(clubs))
