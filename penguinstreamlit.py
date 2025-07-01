
import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn.objects as so

st.title("Fiza Khan's Penguin Data Visualizer")

# Load the dataset from seaborn
penguins = sns.load_dataset("penguins").dropna()

st.write("### Violin Plot: Body Mass by Species and Sex")

fig = px.violin(
    penguins,
    x="species",
    y="body_mass_g",
    color="sex",
    box=True,
    points="all"
)

fig.update_layout(title="Penguin Body Mass by Species and Sex")

st.plotly_chart(fig)
