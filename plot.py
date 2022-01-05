import streamlit as st 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def app(cars_df):
	st.header("Visualise Data")
	st.set_option("deprecation.showPyplotGlobalUse",False)
	st.subheader("Scatter Plot")
	features_list=st.multiselect("Select the X axis value",("carwidth","enginesize","horsepower","drivewheel_fwd","car_company_buick"))
	for feature in features_list:
		st.subheader(f"Scatter Plot for {feature}")
		plt.figure(figsize=(15,5))
		sns.scatterplot(x=feature,y="price",data=cars_df)
		st.pyplot()
	st.subheader("Visualisation Selector")
	plot_type=st.multiselect("Select the chart or plot",("Histogram","Boxplot","Correlation Heatmap"))
	if "Histogram" in plot_type:
		st.subheader('Histogram')
		columns=st.selectbox("Select the Column",("carwidth","enginesize","horsepower"))
		plt.figure(figsize=(15,5))
		plt.title(f"Histogram for {columns}")
		plt.hist(cars_df[columns],bins="sturges",edgecolor="black")
		st.pyplot()
	if "Boxplot" in plot_type:
		st.subheader("Boxplot")
		columns=st.selectbox("Select the Column",("carwidth","enginesize","horsepower"))
		plt.figure(figsize=(15,5))
		sns.boxplot(cars_df[columns])
		st.pyplot()
	if "Correlation Heatmap" in plot_type:
		st.subheader("Correlation Heatmap")
		plt.figure(figsize=(15,5))
		ax=sns.heatmap(cars_df.corr(),annot=True)
		bottom,top=ax.get_ylim()
		ax.set_ylim(bottom+0.5,top-0.5)
		st.pyplot()