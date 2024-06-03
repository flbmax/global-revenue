import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="SportEasy Revenue", page_icon='sporteasy_logo.png', layout="wide")


st.title(':green[Clubs Revenue]')

with st.sidebar:
    st.write("Choose the current club type plan :")
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=WJWy&theme=horizon&opt=ctxmenu",
        height=140,
        width=200)
    
    st.write("Choose the club country:")
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=fUKXWP&theme=horizon&opt=ctxmenu",
        height=140,
        width=200)
    
    st.write("Choose the sales:")
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=JaQREm&theme=horizon&opt=ctxmenu",
        height=140,
        width=200)

st.write("Choose the club sport:")
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=ASEf&theme=horizon&opt=ctxmenu",
        height=140,
        width=1000)
st.header('1. Sales Club')
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=kXpw&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption('''**Notes :** \n
- Using transaction.checkout_at as the date apart for the "Yearly Plan Average Basket where it is club_subscription.start_at, which means it is not possible to filter on it \n
- "To Date" compares amounts for the months ended in the current year with previous years over the same period''')

st.header('2. MRR Club') 
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=FSfpJ&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption('''**Notes :** \n
- Using transaction.spread_start_at as the date \n
- "To Date" compares amounts for the months ended in the current year with previous years over the same period''')

