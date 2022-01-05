import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error,mean_squared_log_error
@st.cache()
def prediction(cars_df,car_width,enginesize,horsepower,drive_wheel_fwd,car_company_buick):
	x=cars_df.iloc[:,:-1]
	y=cars_df["price"]
	X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
	lg=LinearRegression()
	lg.fit(X_train,y_train)
	score=lg.score(X_train,y_train)
	price=lg.predict([[car_width,enginesize,horsepower,drive_wheel_fwd,car_company_buick]])
	price=price[0]
	y_test_pred=lg.predict(X_test)
	test_r2_score=r2_score(y_test,y_test_pred)
	test_mae=mean_absolute_error(y_test,y_test_pred)
	test_msle=mean_squared_log_error(y_test,y_test_pred)
	test_rmse=np.sqrt(mean_squared_error(y_test,y_test_pred))
	return price,score,test_r2_score,test_rmse,test_msle,test_mae
def app(cars_df):
	st.markdown("<p style='color:blue;font-size:25px'>This app uses <b>LinearRegression</b> to predict the price of a car based on your input",unsafe_allow_html=True)
	st.subheader("Select Value:")
	car_width=st.slider("Car Width",float(cars_df["carwidth"].min()),float(cars_df["carwidth"].max()))
	enginesize=st.slider("Engine Size",int(cars_df["enginesize"].min()),int(cars_df["enginesize"].max()))
	horsepower=st.slider("Horse Power",int(cars_df["horsepower"].min()),int(cars_df["horsepower"].max()))
	drive_fwd=st.radio("Is it a forward drive car",("Yes","No"))
	if drive_fwd=="No":
		drive_fwd=0
	else:
		drive_fwd=1
	car_company_buick=st.radio("Is the car manufacured by buick?",("Yes","No"))
	if car_company_buick=="No":
		car_company_buick=0
	else:
		car_company_buick=1
	if st.button("Predict"):
		st.subheader("prediction Results:")
		price,score,r2,rmse,msle,mae=prediction(cars_df,car_width,enginesize,horsepower,drive_fwd,car_company_buick)
		st.success(f"The Predicted Price of the car:${int(price):,}")
		st.info(f"Accuracy Score={score:.2f}")
		st.info(f"R2 Score={r2:.3f}")
		st.info(f"MAE={mae:.3f}")
		st.info(f"RMSE={rmse:.3f}")
		st.info(f"MSLE={msle:.3f}")