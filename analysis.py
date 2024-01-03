# Import necessary libraries
import dash
from dash.dependencies import Input, Output
from dash import dcc, html
import plotly.express as px
import pandas as pd
import numpy as np
import datetime
import base64
import io

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the function to parse and process the uploaded file
def parse_contents(contents, filename):
    if contents is not None and ',' in contents:
        content_type, content_string = contents.split(',', 1)  # split at the first comma
    else:
        return html.Div(['File format not recognized or file not uploaded correctly.'])
    
    try:
        decoded = base64.b64decode(content_string)
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            print("File read successfully.")
        else:
            return html.Div(['Only CSV file format is supported.'])
        
        # Data processing (similar to your existing code)
        df['timestamp'] = df['timestamp'].apply(parse_custom_timestamp)
        df_clean = df[df['HR'] > 0]
        df_clean['RR'] = 60000 / df_clean['HR']
        
        diff_rr = np.diff(df_clean['RR'])
        df_clean['RMSSD'] = np.sqrt(np.mean(diff_rr**2))
        df_clean['SDSD'] = np.std(diff_rr)
        df_clean['pNN25'] = np.sum(np.abs(diff_rr) > 25) / len(diff_rr) * 100
        df_clean['pNN50'] = np.sum(np.abs(diff_rr) > 50) / len(diff_rr) * 100
        df_clean['SDRR'] = np.std(df_clean['RR'])
        df_clean['SDRR_RMSSD'] = df_clean['SDRR'] / df_clean['RMSSD']
        
        print("Data processed successfully.")
        
        # Generate plots
        fig_hr_time_series = px.line(df_clean, x='timestamp', y='HR', title='Heart Rate Over Time')
        fig_hr_time_series.update_layout(
            plot_bgcolor='white', 
            title_font_color='blue', 
            title_font_size=20,
            xaxis_title='Timestamp',
            yaxis_title='Heart Rate (bpm)',
            xaxis_color='grey', 
            yaxis_color='grey',
            xaxis_showgrid=False, 
            yaxis_showgrid=True, 
            gridcolor='lightgrey'
        )
        fig_hr_time_series.update_traces(line=dict(color='red', width=2))

        fig_rr_intervals = px.line(df_clean, x='timestamp', y='RR', title='RR Intervals Over Time')
        fig_rr_intervals.update_layout(
            plot_bgcolor='white', 
            title_font_color='blue', 
            title_font_size=20,
            xaxis_title='Timestamp',
            yaxis_title='RR Intervals',
            xaxis_color='grey', 
            yaxis_color='grey',
            xaxis_showgrid=False, 
            yaxis_showgrid=True, 
            gridcolor='lightgrey'
        )
        fig_rr_intervals.update_traces(line=dict(color='orange', width=2))
                
        # Styling for fig_hr_distribution (Histogram for Heart Rate)
        fig_hr_distribution = px.histogram(df_clean, x='HR', nbins=20, title='Distribution of Heart Rate')
        fig_hr_distribution.update_layout(
            plot_bgcolor='lavender', 
            title_font_color='darkblue', 
            title_font_size=20,
            xaxis_title='Heart Rate (bpm)',
            yaxis_title='Frequency',
            xaxis_color='darkblue', 
            yaxis_color='darkblue',
            xaxis_showgrid=True, 
            yaxis_showgrid=True, 
            gridcolor='lightblue'
        )
        fig_hr_distribution.update_traces(marker_color='navy', marker_line_color='black', 
                                        marker_line_width=1.5, opacity=0.6)

        # Styling for fig_rr_distribution (Histogram for RR Intervals)
        fig_rr_distribution = px.histogram(df_clean, x='RR', nbins=20, title='Distribution of RR Intervals')
        fig_rr_distribution.update_layout(
            plot_bgcolor='mintcream',
            title_font_color='green',
            title_font_size=20,
            xaxis_title='RR Intervals (ms)',
            yaxis_title='Frequency',
            xaxis_color='green',
            yaxis_color='green',
            xaxis_showgrid=True,
            yaxis_showgrid=True,
            gridcolor='lightgreen'
        )
        fig_rr_distribution.update_traces(marker_color='darkgreen', marker_line_color='black', 
                                        marker_line_width=1.5, opacity=0.6)

        # Styling for fig_rr_vs_hr (Scatter Plot of RR Intervals vs Heart Rate)
        fig_rr_vs_hr = px.scatter(df_clean, x='HR', y='RR', title='RR Intervals vs Heart Rate')
        fig_rr_vs_hr.update_layout(
            plot_bgcolor='floralwhite',
            title_font_color='darkred',
            title_font_size=20,
            xaxis_title='Heart Rate (bpm)',
            yaxis_title='RR Intervals (ms)',
            xaxis_color='darkred',
            yaxis_color='darkred',
            xaxis_showgrid=True,
            yaxis_showgrid=True,
            gridcolor='lightcoral'
        )
        fig_rr_vs_hr.update_traces(marker_color='crimson', marker_size=10, marker_line_color='black', 
                                marker_line_width=1)
        
        print("Plots generated successfully.")
        
        return html.Div([
            dcc.Graph(figure=fig_hr_time_series),
            dcc.Graph(figure=fig_rr_intervals),
            dcc.Graph(figure=fig_hr_distribution),
            dcc.Graph(figure=fig_rr_distribution),
            dcc.Graph(figure=fig_rr_vs_hr)
        ])

        
    except Exception as e:
        print(e)
        return html.Div(['There was an error processing this file.'])

# Define the app layout
app.layout = html.Div([
    html.H1("Heart Rate Variability Analysis Dashboard"),
    
    dcc.Upload(
        id='upload-data',
        children=html.Button('Upload File'),
        multiple=False
    ),
    
    html.Div(id='output-data-upload')
])


# Callback to handle file upload
@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [dash.dependencies.State('upload-data', 'filename')])
def update_output(list_of_contents, list_of_names):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n) for c, n in
            zip(list_of_contents, list_of_names)]
        return children

def parse_custom_timestamp(ts):
    year = int(ts[0:4])
    month = int(ts[4:6])
    day = int(ts[6:8])
    hour = int(ts[9:11])
    minute = int(ts[11:13])
    second = int(ts[13:15])
    milliseconds = int(ts[15:18])
    return datetime.datetime(year, month, day, hour, minute, second, milliseconds*1000)


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

