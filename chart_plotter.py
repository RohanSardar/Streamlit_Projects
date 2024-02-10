import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd

def random_plot(ops):
    col1, col2 = st.columns(2)
    x = col1.number_input('Lower range', value=None, placeholder='Type lower range...')
    y = col2.number_input('Upper range', value=None, placeholder='Type upper range...')
    n = st.slider('Number of random variables', 0, 100)
    if x and y and n:
        st.write('### Output')
        chart_data = pd.DataFrame(np.random.randint(int(x), int(y) + 1, int(n)), columns=["1"])
        if ops == 'Line Chart':
            st.line_chart(chart_data)
        else:
            st.scatter_chart(chart_data)

def custom_plot(ops):
    n = st.text_input('Data points',
                      placeholder="Type as many data points as you can")
    if len(n) > 0:
        if ' ' in n:
            n = np.array(n.split()).astype('int')
        else:
            if len(n) > 0 and n[-1] == ',':
                n = n[:-1]
                n = np.array(n.split(',')).astype('int')

        st.write('### Output')

        if ops == 'Line Chart':
            st.line_chart(n)
        else:
            st.scatter_chart(n)

st.title("Chart Plotter")

ops = st.selectbox(
    "Type of chart",
    ('Line Chart', 'Scatter Chart')
)

custom = st.toggle('Custom data mode')

if custom == True:
    st.write('###### Currently in custom mode')
    custom_plot(ops)

else:
    st.write('###### Currently in random mode')
    random_plot(ops)
