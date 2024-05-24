import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="SportEasy Revenue", page_icon='sporteasy_logo.png', layout="wide")


st.title(':green[Teams Revenue]')

with st.sidebar:
    st.write("Choose the current team type plan :")
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=RyHRyH&theme=horizon&opt=ctxmenu",
        height=140,
        width=200)
    
    st.write("Choose the team country:")
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=jnHptB&theme=horizon&opt=ctxmenu",
        height=140,
        width=200)
    
    
st.header('1. Sales Team')
# profiles created
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=XXjJWP&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption('''**Notes :** \n
- Using transaction.checkout_at as the date \n
- "To Date" compares amounts for the months ended in the current year with previous years over the same period''')

st.header('2. MRR Team')
# profiles created
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=qvjAes&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption('''**Notes :** \n
- Using transaction.spread_start_at as the date \n
- "To Date" compares amounts for the months ended in the current year with previous years over the same period''')