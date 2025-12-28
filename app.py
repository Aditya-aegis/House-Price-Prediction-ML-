import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd
import time
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor

st.title('🏠House Price prediction using ML')
st.image('https://i.pinimg.com/236x/08/b1/84/08b184bf0fa126158ed3d56a42e20414.jpg')

df = pd.read_csv('house_data.csv')
X = df.iloc[:,:-3]
y = df.iloc[:,-1]

st.sidebar.title('Selet House feature')
st.sidebar.image('https://i.pinimg.com/236x/08/b1/84/08b184bf0fa126158ed3d56a42e20414.jpg')
all_value = []
for i in X:
  min_value = int(X[i].min())
  max_vlaue = int(X[i].max())
  ans = st.siderbar.slider(f'selet {i} value', min_value, max_value)
  all_vlaue.append(ans)  

# st.write(all_value)

scaler = StandardScaler()
scaled_X = scaler.fit_transform(X)
final_value = scaler.transform([all_value])

model = st.cache(RandomForestRegressor)()
model.fit(X,y)
house_price = model.pridect(final_value)[0]

with st.spinner('Predicting House price'):
  time.sleep(1)
msg = f'''House price is: ${round(house_price*100000,2)}'''
st.success(msg)

st.markdown('''**Deign and Developed by: Aditya Kumar**''')





