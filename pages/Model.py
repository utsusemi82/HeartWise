import streamlit as st
import pandas as pd

st.set_page_config(
  page_title="Model",
  page_icon = "🚀"
)

st.sidebar.write("Menu")
st.sidebar.write("Exploratory Data Analysis")
st.sidebar.write("Guide")
st.sidebar.success("Model ")
st.sidebar.write("Playground")
st.sidebar.info("Presented by JiaWen Cher")

st.markdown("# Model Comparison & Analysis 🗂️")
st.markdown("""
    #### Overview
    In order to develop a robust system for stress level detection based on HRV (Heart Rate Variability) analysis, I have trained and evaluated four different machine learning models:

    Random Forest, Logistic Regression, K-Nearest Neighbors (KNN), and Support Vector Machine (SVM), Decision Tree, Gradient Boosting and Lightweight Neural Network.

    Each model has been rigorously tested to ensure accuracy and reliability in real-world scenarios.
""")
st.write("")
st.image("HRV/assets/photo-1682706841281-f723c5bfcd83.jpeg")
st.divider()

st.markdown("### Model Classification Reports")
st.write("")
st.write("There are four models (Random Forest, K-Nearest Neighbors, Decision Tree and Lightweight Neural Network) have been showing high accuracy and F1-scores (>97%), which indicate high risk in overfitting.")
st.write("Thus, model selection has been carried out and let us focus on the other 3 potential models.")
st.write("")

st.markdown("#### Logistic Regression Classification Report")
data_logistic = {
    "Precision": [0.57, 0.61, 0.46, None, 0.55, 0.57],
    "Recall": [0.31, 0.87, 0.21, None, 0.46, 0.59],
    "F1-Score": [0.40, 0.72, 0.29, 0.59, 0.47, 0.55],
    "Support": [11782, 22158, 7093, 41033, 41033, 41033]
}
index_logistic = ["0", "1", "2", "Accuracy", "Macro Avg", "Weighted Avg"]
logistic_report_df = pd.DataFrame(data_logistic, index=index_logistic)
st.table(logistic_report_df)
st.write("")


st.markdown("#### Support Vector Machine Classification Report")
data_svm = {
    "Precision": [0.57, 0.62, 0.52, None, 0.57, 0.59],
    "Recall": [0.32, 0.89, 0.19, None, 0.47, 0.60],
    "F1-Score": [0.41, 0.73, 0.28, 0.60, 0.47, 0.56],
    "Support": [11782, 22158, 7093, 41033, 41033, 41033]
}
index_svm = ["0", "1", "2", "Accuracy", "Macro Avg", "Weighted Avg"]
svm_report_df = pd.DataFrame(data_svm, index=index_svm)
st.table(svm_report_df)
st.write("")

st.markdown("#### Gradient Boosting Classification Report")
data_gb= {
    "Precision": [0.87, 0.83, 0.83, None, 0.84, 0.84],
    "Recall": [0.73, 0.94, 0.70, None, 0.79, 0.84],
    "F1-Score": [0.80, 0.88, 0.76, 0.84, 0.81, 0.73],
    "Support": [11782, 22158, 7093, 41033, 41033, 41033]
}
index_gb = ["0", "1", "2", "Accuracy", "Macro Avg", "Weighted Avg"]
gb_report_df = pd.DataFrame(data_gb, index=index_gb)
st.table(gb_report_df)
st.write("")


st.divider()
st.markdown("""

    ### Model Performance Analysis

    Overall, Gradient Boosting outperforms both SVM and Logistic Regression in terms of precision, recall, and f1-score across all classes. Its accuracy is also significantly higher, suggesting it is the best model. Gradient Boosting model maintains a good balance between precison and recall indicating its robustness. With highest f1-score across all classes comparing the other 2 models, this suggests Gradient Boosting has demonstrated superior ability to classify stress levels accurately.
    
    Gradient Boosting is best suited for our application in stress level detection using HRV analysis.
    It strikes the right balance between understanding the complex patterns in the data and generalizing well to new, unseen data.
    """)

st.write("")

st.divider()
st.write("Exploratory Data Analysis & Model 🗂️")
