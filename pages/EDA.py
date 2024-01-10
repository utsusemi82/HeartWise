import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
  page_title="EDA",
  page_icon="📈",
  layout="wide"
)

st.sidebar.write("Menu")
st.sidebar.success("Exploratory Data Analysis")
st.sidebar.write("Guide")
st.sidebar.write("Model ")
st.sidebar.write("Playground")
st.sidebar.info("Presented by JiaWen Cher")

st.markdown("# Exploratory Data Analysis 📈")
st.write("Exploratory Data Analysis (EDA) is an essential step in the data analysis process to understand the dataset.")
st.divider()

st.markdown("### Data Dictionary: HRV Features")
st.write("#### This is a data dictionary for the features related to Heart Rate Variability (HRV):")
hrv_features = pd.DataFrame({
    "Feature": ["MEAN_RR", "MEDIAN_RR", "SDRR", "RMSSD", "SDSD", "SDRR_RMSSD", "HR", "pNN25", "pNN50", "RR"],
    "Description": [
        "Mean of RR intervals (milliseconds)",
        "Median of RR intervals (milliseconds)",
        "Standard deviation of RR intervals (milliseconds)",
        "Root Mean Square of Successive Differences between RR intervals (milliseconds)",
        "Standard deviation of Successive Differences between RR intervals (milliseconds)",
        "Ratio of SDRR to RMSSD",
        "Heart rate (beats per minute)",
        "Percentage of RR intervals >25 ms different from the previous (short-term HRV)",
        "Percentage of RR intervals >50 ms different from the previous (short-term HRV)",
        "Time between consecutive heartbeats, derived from ECG signal (milliseconds)"
    ]
})
st.table(hrv_features)
st.write("")

st.write("#### This is the condition of stress levels:")
stress_levels = pd.DataFrame({
    "Level": ["Level 1", "Level 2", "Level 3"],
    "Condition": [
        "Normal Stress Level: Normal or relaxed state",
        "Attention Needed: Moderate stress level",
        "Overload: High stress level, immediate intervention may be necessary"
    ]
})
st.table(stress_levels)
st.write(""" These features are commonly used in the analysis of HRV to assess an individual's physiological response to stress and can be valuable for stress level detection and management.
""")


st.divider()
st.markdown("### Dataset")
st.write("This is the dataset used for model training.")

# dataset details
st.image("HRV/data_head.jpg")
st.write("")

st.write("The details of the data are shown as below: ")
st.image("HRV/data_info.jpg")
st.image("HRV/data_describe.jpg")
st.write("")

st.write("")
st.write("The charts below show the HRV features and their correlation.")
st.image("HRV/correlation.png")
st.write("")

st.image("HRV/mean_median.png")
st.write("")

st.image("HRV/HRV features plot.png")
st.write("")

st.divider()

st.markdown("### Dashboard: HRV Analysis")
st.write("""
  This is an interactive dashboard that presents the analysis of the dataset used in my HRV model training, in an intuitive yet comprehensible format.
""")
st.write("")

st.components.v1.html("""
<iframe title="HRV Analysis" style="width:100%;height:600px;" src="https://app.powerbi.com/view?r=eyJrIjoiYTg5MDlhNWQtZTRhNi00ZWYxLTkxOTctZGFmNWE0YTgxYjIxIiwidCI6ImE2M2JiMWE5LTQ4YzItNDQ4Yi04NjkzLTMzMTdiMDBjYTdmYiIsImMiOjEwfQ%3D%3D" frameborder="0" allowFullScreen="true"></iframe>
""", height=600)  # Adjust the height as needed


st.divider()
st.write("EDA 📈")
