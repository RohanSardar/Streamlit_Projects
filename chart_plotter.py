import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd

st.title("Chart Plotter")

ops = st.selectbox(
    "Type of chart",
    ('Line Chart', 'Scatter Chart')
)

col1, col2 = st.columns(2)
x = col1.number_input('Lower range', value=None, placeholder='Type lower range...')
y = col2.number_input('Upper range', value=None, placeholder='Type upper range...')

n = st.slider('Number of random variables', 0, 100)

if x and y:
    st.write('### Output')

    chart_data = pd.DataFrame(np.random.randint(int(x), int(y)+1, int(n)), columns=["a"])
    
    if ops == 'Line Chart':
        st.line_chart(chart_data)
    elif ops == 'Scatter Chart':
        st.scatter_chart(chart_data)
