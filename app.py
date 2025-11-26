# -----------------------------
# Streamlit App: Semmelweis Case Study
# Code snippet assisted by ChatGPT
# -----------------------------

import streamlit as st
import pandas as pd
import altair as alt

# -----------------------------
# Load data
# -----------------------------
df = pd.read_csv("yearly_deaths_by_clinic.csv")

# -----------------------------
# App Title + Description
# -----------------------------
st.title("🧼 Semmelweis and the Discovery of Handwashing")

st.write("""
In the mid-1800s, Dr. Ignaz Semmelweis noticed that mortality rates in one of the Vienna General Hospital’s maternity clinics 
were drastically higher than in the other. After introducing mandatory hand-washing with chlorinated lime in 1847, mortality 
rates dropped dramatically. This app visualizes the data that helped Semmelweis make his groundbreaking discovery.
""")

# -----------------------------
# Filters (Optional for Assignment)
# -----------------------------
clinics = df['Clinic'].unique()
selected_clinic = st.selectbox("Select a Clinic:", clinics)

filtered_df = df[df['Clinic'] == selected_clinic]

# -----------------------------
# Line Chart: Births vs. Deaths Over Time
# -----------------------------
st.subheader(f"📈 Mortality Trends in {selected_clinic}")

line_chart = alt.Chart(filtered_df).transform_fold(
    ['Birth', 'Deaths'],
    as_=['variable', 'value']
).mark_line().encode(
    x='Year:Q',
    y='value:Q',
    color='variable:N'
).properties(
    width=700,
    height=400
)

st.altair_chart(line_chart, use_container_width=True)

# -----------------------------
# Mortality Rate Chart
# -----------------------------
st.subheader("☠️ Mortality Rate Over Time")

filtered_df['mortality_rate'] = filtered_df['Deaths'] / filtered_df['Birth']

mortality_chart = alt.Chart(filtered_df).mark_line(point=True).encode(
    x='Year:Q',
    y='mortality_rate:Q'
).properties(
    width=700,
    height=400
)

st.altair_chart(mortality_chart, use_container_width=True)

# -----------------------------
# Findings Explanation (2–3 Sentences)
# -----------------------------
st.subheader("📌 Key Findings")

st.write("""
After hand-washing was introduced in 1847, mortality rates dropped sharply, 
especially in Clinic 1, where doctors frequently moved between autopsies and childbirth. 
This visualization highlights how Semmelweis’s intervention directly correlated with a 
reduction in preventable maternal deaths.
""")

# -----------------------------
# Show Raw Data (Optional)
# -----------------------------
with st.expander("View Raw Data"):
    st.dataframe(df)