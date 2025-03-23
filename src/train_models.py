import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Function to train and save a model
def train_model(data_path, features, target, model_name):
    data = pd.read_csv(data_path)
    X = data[features]
    y = data[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    accuracy = accuracy_score(y_test, model.predict(X_test))
    print(f"{model_name} Accuracy: {accuracy:.2f}")

    joblib.dump(model, f"C:/Disha's corner/kubernetes_failure_prediction-dversion/models/{model_name}.pkl")
    print(f"Model saved: models/{model_name}.pkl\n")

# Train models for different issues
train_model("C:/Disha's corner/kubernetes_failure_prediction-dversion/src/training data/node_metrics.csv", ["cpu_usage", "memory_usage", "disk_pressure", "pod_restart_count"], "node_failure", "node_failure_predictor")
train_model("C:/Disha's corner/kubernetes_failure_prediction-dversion/src/training data/resource_metrics.csv", ["cpu_usage", "memory_usage", "disk_usage", "network_io"], "resource_exhaustion", "resource_exhaustion_predictor")
train_model("C:/Disha's corner/kubernetes_failure_prediction-dversion/src/training data/network_metrics.csv", ["network_latency", "packet_loss", "dns_failures", "connection_reset"], "network_issue", "network_issue_predictor")
train_model("C:/Disha's corner/kubernetes_failure_prediction-dversion/src/training data/scheduling_metrics.csv", ["pending_pods", "node_capacity", "resource_requests", "autoscaler_latency"], "scheduling_issue", "scheduling_issue_predictor")
