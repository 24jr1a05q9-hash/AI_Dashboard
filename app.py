import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Titanic AI Dashboard")

df = pd.read_csv("titanic.csv")

# Data Cleaning
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

st.subheader("Dataset Overview")

st.dataframe(df.head())

st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])

st.subheader("Data Cleaning")

st.write("Missing values after cleaning:")

st.dataframe(df.isnull().sum())

st.subheader("Key Metrics (KPIs)")

total_passengers = len(df)
total_survived = df["Survived"].sum()
survival_rate = (total_survived / total_passengers) * 100

col1, col2, col3 = st.columns(3)

col1.metric("Total Passengers", total_passengers)
col2.metric("Total Survivors", total_survived)
col3.metric("Survival Rate (%)", round(survival_rate, 2))

st.subheader("Interactive Filter")

gender_filter = st.selectbox(
    "Select Gender",
    ["All"] + list(df["Sex"].unique())
)

if gender_filter != "All":
    filtered_df = df[df["Sex"] == gender_filter]
else:
    filtered_df = df

st.dataframe(filtered_df.head())


st.subheader("Visualizations")

# 1. Survival Count
fig1 = px.bar(
    df["Survived"].value_counts().reset_index(),
    x="Survived",
    y="count",
    title="Survival Count"
)
st.plotly_chart(fig1)

# 2. Passenger Class Distribution
fig2 = px.pie(
    df,
    names="Pclass",
    title="Passenger Class Distribution"
)
st.plotly_chart(fig2)

# 3. Age Distribution
fig3 = px.histogram(
    df,
    x="Age",
    title="Age Distribution"
)
st.plotly_chart(fig3)

# 4. Gender Distribution
fig4 = px.bar(
    df["Sex"].value_counts().reset_index(),
    x="Sex",
    y="count",
    title="Gender Distribution"
)
st.plotly_chart(fig4)

# 5. Fare Distribution
fig5 = px.histogram(
    df,
    x="Fare",
    title="Fare Distribution"
)
st.plotly_chart(fig5)