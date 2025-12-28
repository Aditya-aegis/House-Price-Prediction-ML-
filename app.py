import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd
import time
from sklearn.datasets import fetch_california_housing

st.title('🏠House Price prediction using ML')
st.image('https://i.pinimg.com/236x/08/b1/84/08b184bf0fa126158ed3d56a42e20414.jpg')

df = pd.read_csv('house_data.csv')
X = df.iloc[:,:-3]
y = df.iloc[:,-1]

st.sidebar.title('Selet House feature')
st.sidebar.image('https://i.pinimg.com/236x/08/b1/84/08b184bf0fa126158ed3d56a42e20414.jpg')
all_value = []
for i in X:
  ans = st.siderbar.slider(f'selet {i} value')
  all_vlaue.append(ans)  

st.write(all_value)
