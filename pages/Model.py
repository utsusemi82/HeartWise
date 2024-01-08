import streamlit as st
import pandas as pd

st.set_page_config(
  page_title="Model",
  page_icon = "🚀"
)

st.markdown("# Model Comparison & Analysis 🗂️")
st.sidebar.header("Model")
st.markdown("""
    #### Overview
    In order to develop a robust system for stress level detection based on HRV (Heart Rate Variability) analysis, I have trained and evaluated four different machine learning models:

    Random Forest, Logistic Regression, K-Nearest Neighbors (KNN), and Support Vector Machine (SVM).

    Each model has been rigorously tested to ensure accuracy and reliability in real-world scenarios.
""")
st.write("")
st.image("HRV/assets/photo-1682706841281-f723c5bfcd83.jpeg")
st.divider()

st.markdown("### Model Classification Reports")
st.write("")


st.markdown("#### Random Forest Classification Report")
data_rf = {
    "Precision": [0.95, 0.99, 0.78, None, 0.91, 0.94],
    "Recall": [0.96, 0.90, 0.98, None, 0.95, 0.93],
    "F1-Score": [0.95, 0.95, 0.87, 0.93, 0.92, 0.94],
    "Support": [11782, 22158, 7093, 41033, 41033, 41033]
}
index_rf = ["0", "1", "2", "Accuracy", "Macro Avg", "Weighted Avg"]
rf_report_df = pd.DataFrame(data_rf, index=index_rf)
st.table(rf_report_df)
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

st.markdown("#### K-Nearest Neighbors Classification Report")
data_knn = {
    "Precision": [1.00, 1.00, 1.00, None, 1.00, 1.00],
    "Recall": [1.00, 1.00, 1.00, None, 1.00, 1.00],
    "F1-Score": [1.00, 1.00, 1.00, 1.00, 1.00, 1.00],
    "Support": [11782, 22158, 7093, 41033, 41033, 41033]
}
index_knn = ["0", "1", "2", "Accuracy", "Macro Avg", "Weighted Avg"]
knn_report_df = pd.DataFrame(data_knn, index=index_knn)
st.table(knn_report_df)
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
st.write("")

st.markdown("### Comparison between the models using Accuracy and ROC AUC")
st.image("HRV/accuracy.png")
st.write("")

st.markdown("### Confusion Matrix for Each Model")
st.image("HRV/cf_rf.png")
st.image("HRV/cf_logistic.png")
st.image("HRV/cf_knn.png")
st.image("HRV/cf_svm.png")
st.write("")

st.markdown("### ROC AUC for Each Model")
st.image("HRV/roc_rf.png")
st.image("HRV/roc_logistic.png")
st.image("HRV/roc_knn.png")

st.divider()
st.markdown("""

    ### Model Performance Analysis

    **1. Random Forest Classifier**
    - **Accuracy**: 93%
    - **Strengths**: Exhibits high precision, recall, and f1-scores across all classes.
      Balanced performance makes it robust in various scenarios.
    - **Highlights**: Achieved the highest overall accuracy among all models,
      indicating excellent generalization capabilities.

    **2. Logistic Regression Classifier**
    - **Accuracy**: 59%
    - **Strengths**: Useful for linearly separable data; however, its performance is modest in this case.
    - **Considerations**: Lower precision, recall, and f1-scores compared to other models,
      indicating challenges in handling complex patterns in the data.

    **3. K-Nearest Neighbors Classifier**
    - **Accuracy**: 100%
    - **Strengths**: Achieved perfect scores in precision, recall, and f1-score.
    - **Note**: While the perfect scores might seem ideal, they are typically indicative of overfitting.
      This perfection might not translate well to unseen data.

    **4. Support Vector Machine Classifier**
    - **Accuracy**: 60%
    - **Strengths**: Good for higher-dimensional spaces but showed moderate performance in this case.
    - **Considerations**: Performance is better than Logistic Regression but still lags behind the Random Forest model.


    #### Why Random Forest is the Best Choice?

    Based on the performance metrics, the **Random Forest Classifier** emerges as the leading model for the following reasons:
    - **High Accuracy**: At 93% accuracy, it significantly outperforms the other models,
      suggesting it can reliably interpret the HRV data to assess stress levels.
    - **Balanced Metrics**: Showcases high precision, recall, and f1-scores, ensuring that it not only predicts accurately
      but also maintains a balanced sensitivity (recall) and specificity (precision) across all classes.
    - **Robustness**: The model's ability to handle the intricacies and variations in the data without overfitting
      (unlike the KNN model) makes it more reliable for practical applications.
    - **Versatility**: Performs well across multiple classes, essential for categorizing different levels of stress accurately.

    #### Conclusion
    The Random Forest Classifier, with its superior accuracy and balanced performance across various metrics,
    is best suited for our application in stress level detection using HRV analysis.
    It strikes the right balance between understanding the complex patterns in the data and generalizing well to new, unseen data.
    """)

st.write("")

st.divider()
st.write("Exploratory Data Analysis & Model 🗂️")
