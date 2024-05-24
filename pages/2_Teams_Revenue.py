import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="SportEasy Revenue", page_icon='sporteasy_logo.png', layout="wide")


st.title(':green[Teams Revenue]')

with st.sidebar:
    st.write("Choose the current team type plan :")
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=BtJcuV&theme=horizon&opt=ctxmenu",
        height=140,
        width=200)
    
    st.write("Choose the team country:")
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=bjAJDAZ&theme=horizon&opt=ctxmenu",
        height=140,
        width=200)
    
    
st.header('1. Sales Team')
# profiles created
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=Lhvbszb&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption('*using transaction.checkout_at as the date')

st.header('2. MRR Team')
# profiles created
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=Lhvbszb&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption('*using transaction.spread_start_at as the date')
