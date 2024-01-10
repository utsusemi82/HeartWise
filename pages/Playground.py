
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import datetime

# Load your model and scaler
scaler = joblib.load('scaler.joblib')
model = joblib.load('rf_model.joblib')
label_mapping_pred = {1: 'Normal state', 2: 'Attention needed', 0: 'Overload'}

# Define function to parse timestamps
def parse_custom_timestamp(ts):
    year, month, day = int(ts[0:4]), int(ts[4:6]), int(ts[6:8])
    hour, minute, second = int(ts[9:11]), int(ts[11:13]), int(ts[13:15])
    milliseconds = int(ts[15:18])
    return datetime.datetime(year, month, day, hour, minute, second, milliseconds*1000)

# Function for data preprocessing
def preprocess_data(df):
    df['HR'] = pd.to_numeric(df['HR'], errors='coerce')  # Convert to numeric, set non-numeric to NaN
    df.dropna(subset=['HR'], inplace=True)  # Drop rows with NaN in 'HR' column
    df = df[df['HR'] > 0]  # Keep rows where HR is greater than 0
    df['HR'] = df['HR'].astype(int)  # Convert HR to integer
    return df

# Function to calculate features
def calculate_features(df):
    df['RR'] = 60000 / df['HR']
    df['successive_diff'] = df['RR'].diff().abs()

    # RMSSD
    df['squared_diff'] = df['successive_diff'] ** 2
    RMSSD = np.sqrt(df['squared_diff'].mean())

    # SDSD
    SDSD = df['successive_diff'].std()

    # pNN25 and pNN50
    pNN25 = (df['successive_diff'] > 25).sum() / len(df['successive_diff']) * 100
    pNN50 = (df['successive_diff'] > 50).sum() / len(df['successive_diff']) * 100

    # SDRR_RMSSD
    SDRR_RMSSD = df['RR'].std() / RMSSD

    df['MEAN_RR'] = df['RR'].mean()
    df['MEDIAN_RR'] = df['RR'].median()
    df['SDRR'] = df['RR'].std()
    df['RMSSD'] = RMSSD
    df['SDSD'] = SDSD
    df['pNN25'] = pNN25
    df['pNN50'] = pNN50
    df['SDRR_RMSSD'] = SDRR_RMSSD

    required_features = ['MEAN_RR', 'MEDIAN_RR', 'SDRR', 'RMSSD', 'SDSD', 'SDRR_RMSSD', 'HR', 'pNN25', 'pNN50']
    features_for_prediction = df[required_features].values
    hrv_metrics_display = df[required_features].describe()
    return features_for_prediction, hrv_metrics_display, df

def display_figures(df, decoded_predictions):
    # Heart Rate Over Time
    fig_hr_time_series = px.line(df, x='timestamp', y='HR', title='Heart Rate Over Time')
    fig_hr_time_series.update_layout(
        plot_bgcolor='#000000',
        title_font_color='white',
        title_font_size = 20,
        xaxis_title='Timestamp',
        yaxis_title='Heart Rate (bpm)',
        xaxis_color='white',
        yaxis_color='white',
        xaxis_showgrid=False,
        yaxis_showgrid=True,
        yaxis_gridcolor='#555555'  # Dark grey grid lines for subtle contrast
    )
    fig_hr_time_series.update_traces(line=dict(color='yellow', width=2))

    # RR Intervals Over Time
    fig_rr_intervals = px.line(df, x='timestamp', y='RR', title='RR Intervals Over Time')
    fig_rr_intervals.update_layout(
        plot_bgcolor='black',
        title_font_color='white',
        title_font_size=20,
        xaxis_title='Timestamp',
        yaxis_title='RR Intervals',
        xaxis_color='white',
        yaxis_color='white',
        xaxis_showgrid=False,
        yaxis_showgrid=True,
        yaxis_gridcolor='#555555'
    )
    fig_rr_intervals.update_traces(line=dict(color='orange', width=2))

    # Histogram for Heart Rate
    fig_hr_distribution = px.histogram(df, x='HR', nbins=20, title='Distribution of Heart Rate')
    fig_hr_distribution.update_layout(
        plot_bgcolor='black',
        title_font_color='white',
        title_font_size=20,
        xaxis_title='Heart Rate (bpm)',
        yaxis_title='Frequency',
        xaxis_color='white',
        yaxis_color='white',
        xaxis_showgrid=True,
        yaxis_showgrid=True
    )
    fig_hr_distribution.update_traces(marker_color='yellow', marker_line_color='red', marker_line_width=1.5, opacity=0.6)

    # Histogram for RR Intervals
    fig_rr_distribution = px.histogram(df, x='RR', nbins=20, title='Distribution of RR Intervals')
    fig_rr_distribution.update_layout(
        plot_bgcolor='black',
        title_font_color='white',
        title_font_size=20,
        xaxis_title='RR Intervals (ms)',
        yaxis_title='Frequency',
        xaxis_color='white',
        yaxis_color='white',
        xaxis_showgrid=True,
        yaxis_showgrid=True
    )
    fig_rr_distribution.update_traces(marker_color='green', marker_line_color='white', marker_line_width=1.5, opacity=0.6)

    # Scatter Plot of RR Intervals vs Heart Rate
    fig_rr_vs_hr = px.scatter(df, x='HR', y='RR', title='RR Intervals vs Heart Rate')
    fig_rr_vs_hr.update_layout(
        plot_bgcolor='black',
        title_font_color='white',
        title_font_size=20,
        xaxis_title='Heart Rate (bpm)',
        yaxis_title='RR Intervals (ms)',
        xaxis_color='white',
        yaxis_color='white',
        xaxis_showgrid=True,
        yaxis_showgrid=True
    )
    fig_rr_vs_hr.update_traces(marker_color='yellow', marker_size=10, marker_line_color='black', marker_line_width=1)

    # Stress Levels vs Timestamp
    df['detected stress levels'] = decoded_predictions
    fig_predict_vs_time = px.scatter(df, x='timestamp', y='detected stress levels', title='Stress Levels vs Timestamp')  # Changed 'decoded_prediction' to 'detected stress levels'
    fig_predict_vs_time.update_layout(
        template='plotly_dark',
        title_font_color='white',
        title_font_size=20,
        xaxis_title='Timestamp',
        yaxis_title='Detected Stress Levels',  # Updated the axis title to match
        xaxis_color='orange',
        yaxis_color='orange',
        xaxis_showgrid=True,
        yaxis_showgrid=True
    )
    fig_predict_vs_time.update_traces(marker_color='crimson', marker_size=10, marker_line_color='white', marker_line_width=1)

    # Display the figures in Streamlit
    st.plotly_chart(fig_hr_time_series)
    st.plotly_chart(fig_rr_intervals)
    st.plotly_chart(fig_hr_distribution)
    st.plotly_chart(fig_rr_distribution)
    st.plotly_chart(fig_rr_vs_hr)
    st.plotly_chart(fig_predict_vs_time)

def display_stress_levels(df, decoded_predictions):
    df['detected stress levels'] = decoded_predictions
    stress_level_table = df[['timestamp', 'HR', 'detected stress levels']]
    st.write("Stress Level Detections:")
    st.dataframe(stress_level_table)

# Streamlit app layout
st.set_page_config(page_title="Playground", page_icon="🛝")
st.markdown("## Let's Detect Your Stress Level💓")
st.write("Your csv file must include only two columns 'timestamp' and 'HR' with a minimum of 20 data points for each column to ensure the accuracy of the detection.")
st.sidebar.header("Playground")

# File uploader
try:
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Original DataFrame:")
        st.dataframe(df.head(5))

        df['timestamp'] = df['timestamp'].apply(parse_custom_timestamp)
        df_preprocessed = preprocess_data(df.copy())
        st.write("DataFrame after Preprocessing:")
        st.dataframe(df_preprocessed.head(5))

        features, hrv_metrics_display, df_featured = calculate_features(df_preprocessed.copy())
        st.write("DataFrame with Calculated Features:")
        st.dataframe(df_featured.head(5))

        scaled_features = scaler.transform(features)
        predictions = model.predict(scaled_features)
        decoded_predictions = [label_mapping_pred[label] for label in predictions]

        display_figures(df_featured, decoded_predictions)
        display_stress_levels(df_featured, decoded_predictions)

except Exception as e:
    st.error(f"An error occurred: {e}")
