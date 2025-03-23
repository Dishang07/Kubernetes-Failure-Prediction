
import pandas as pd
import joblib

# Function to make predictions
def make_predictions(model_path, input_df):
    model = joblib.load(model_path)
    predictions = model.predict(input_df)
    return predictions

# File paths for test datasets
test_files = {
    "network_metrics": "C:/Disha's corner/kubernetes_failure_prediction-dversion/data/network_metrics_test.csv",
    "node_metrics": "C:/Disha's corner/kubernetes_failure_prediction-dversion/data/node_metrics_test.csv",
    "resource_metrics": "C:/Disha's corner/kubernetes_failure_prediction-dversion/data/resource_metrics_test.csv",
    "scheduling_metrics": "C:/Disha's corner/kubernetes_failure_prediction-dversion/data/scheduling_metrics_test.csv",
}

# Model file paths (update paths as needed)
model_paths = {
    "node_failure": "C:/Disha's corner/kubernetes_failure_prediction-dversion/models/node_failure_predictor.pkl",
    "resource_exhaustion": "C:/Disha's corner/kubernetes_failure_prediction-dversion/models/resource_exhaustion_predictor.pkl",
    "network_issue": "C:/Disha's corner/kubernetes_failure_prediction-dversion/models/network_issue_predictor.pkl",
    "scheduling_issue": "C:/Disha's corner/kubernetes_failure_prediction-dversion/models/scheduling_issue_predictor.pkl",
}

# **Predict Node Failure**
node_df = pd.read_csv(test_files["node_metrics"])
node_df["node_failure_prediction"] = make_predictions(model_paths["node_failure"], node_df.drop(columns=["node_failure"]))
node_df["Words"] = ['Failure' if a == 1 else 'No Failure' for a in node_df["node_failure_prediction"]]
print("Node Metrics Predictions:\n", node_df[["node_failure", "node_failure_prediction","Words"]])

# **Predict Resource Exhaustion**
resource_df = pd.read_csv(test_files["resource_metrics"])
resource_df["resource_exhaustion_prediction"] = make_predictions(model_paths["resource_exhaustion"], resource_df.drop(columns=["resource_exhaustion"]))
resource_df["Words"] = ['Exhaustion' if a == 1 else 'No Exhaustion' for a in resource_df["resource_exhaustion_prediction"]]
print("Resource Metrics Predictions:\n", resource_df[["resource_exhaustion", "resource_exhaustion_prediction","Words"]])

# **Predict Network Issues**
network_df = pd.read_csv(test_files["network_metrics"])
network_df["network_issue_prediction"] = make_predictions(model_paths["network_issue"], network_df.drop(columns=["network_issue"]))
network_df["Words"] = ['Issue' if a == 1 else 'No Issue' for a in network_df["network_issue_prediction"]]
print("Network Metrics Predictions:\n", network_df[["network_issue", "network_issue_prediction","Words"]])


# **Predict Scheduling Issues**
scheduling_df = pd.read_csv(test_files["scheduling_metrics"])
scheduling_df["scheduling_issue_prediction"] = make_predictions(model_paths["scheduling_issue"], scheduling_df.drop(columns=["scheduling_issue"]))
scheduling_df["Words"] = ['Issue' if a == 1 else 'No Issue' for a in scheduling_df["scheduling_issue_prediction"]]
print("Scheduling Metrics Predictions:\n", scheduling_df[["scheduling_issue", "scheduling_issue_prediction","Words"]])

# **Save updated datasets with predictions**
node_df.to_csv("C:/Disha's corner/kubernetes_failure_prediction-dversion/src/result_data/node_metrics_with_predictions.csv", index=False)
resource_df.to_csv("C:/Disha's corner/kubernetes_failure_prediction-dversion/src/result_data/resource_metrics_with_predictions.csv", index=False)
network_df.to_csv("C:/Disha's corner/kubernetes_failure_prediction-dversion/src/result_data/network_metrics_with_predictions.csv", index=False)
scheduling_df.to_csv("C:/Disha's corner/kubernetes_failure_prediction-dversion/src/result_data/scheduling_metrics_with_predictions.csv", index=False)
