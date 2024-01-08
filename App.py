
import streamlit as st
import pandas as pd

st.set_page_config(
  page_icon = "❤️‍🩹",
  page_title = "Introduction"
)

col1, col2 = st.columns([25,1])
with col1:
  st.write("# Welcome to HeartWise ❤️‍🩹")
with col2:
  st.image("/content/drive/MyDrive/HRV/assets/DALLE_2023-12-30_00.40.23_-_Design_a_very_simple_logo_for_HeartWise._The_logo_should_feature_the_name_HeartWise_in_a_clean_modern_sans-serif_font._Overlay_an_ECG_heart_rate.png", width=80)

st.sidebar.success("Menu")
st.sidebar.write("Exploratory Data Analysis")
st.sidebar.write("Guide")
st.sidebar.write("Model Performance")
st.sidebar.write("Playground")

st.sidebar.info("Presented by JiaWen Cher")

st.write("#### Hi. This is HeartWise, your innovative tool for stress management. ")
st.write("HeartWise leverages Heart Rate Variability (HRV) analysis to provide insights into your stress levels. It's a user-friendly web app designed to help you monitor and manage stress through real-time, non-invasive HRV tracking.")
st.write("")
st.image("/content/drive/MyDrive/HRV/assets/photo-1530508943348-b8f606ea2bf2.jpeg")


st.write("### HeartWise: Your Companion in Stress Management")
st.write("At HeartWise, we harness the power of HRV, a non-invasive and real-time indicator of your body's response to stress. Our approach is rooted in extensive research, showing that HRV changes significantly during stress, making it an effective tool for stress detection. Whether you're at home, at work, or on the go, HeartWise empowers you to monitor your stress levels effortlessly and take proactive steps towards a healthier, more balanced life. Dive into the world of self-awareness and well-being with HeartWise! ")
st.divider()

st.image("/content/drive/MyDrive/HRV/assets/photo-1532798442725-41036acc7489.jpeg")

st.write("### Heart Rate Variability(HRV) 🌿🌈💖")
st.write(
  """
We utilize HRV, a key indicator of your autonomic nervous system's activity, to detect stress. HRV measures the variation in time between heartbeats, which changes under stress. When stressed, this variation tends to decrease, signaling a heightened 'fight-or-flight' response. Conversely, a relaxed state is indicated by increased variability.

HRV is chosen for its non-invasive nature and real-time feedback, offering a practical and accessible way to monitor stress levels.
"""
)
st.divider()

st.image("/content/drive/MyDrive/HRV/assets/photo-1507295171851-ee18df27c2a2.jpeg")
st.write("### Start Managing Stress Today 🌟✨💪 ")
st.write(
  """
HeartWise isn't just about detecting stress; it's your personal tool for managing it effectively. By monitoring HRV, you can recognize stress patterns early and take action, whether it's practicing relaxation techniques, adjusting your lifestyle, or seeking professional guidance.

HeartWise is designed to be user-friendly, making stress management accessible and integrative into your daily routine. Start your journey towards better stress management with HeartWise – a step towards a calmer, healthier you!
Join us in embracing a proactive approach to stress management with HeartWise by checking out the button below.
""")

st.divider()
st.write("Welcome to HeartWise ❤️‍🩹")

