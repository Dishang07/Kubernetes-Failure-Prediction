# Kubernetes Failure Prediction System

## Table of Contents

1. [Overview](#overview)
2. [Installation Requirements](#installation)
3. [Usage](#usage)
   - [Training Models](#training)
   - [Making Predictions](#predictions)
4. [Features and Implementation](#features)
5. [Prediction Types](#prediction-types)
6. [Model Information](#model-info)
7. [Output Format](#output)
8. [License](#license)

## Overview <a name="overview"></a>
This project implements a machine learning-based system for predicting different types of failures in Kubernetes clusters. The system can predict four distinct failure categories:
- Node failures
- Resource exhaustion issues
- Network issues
- Scheduling issues

By forecasting potential failures before they occur, this system helps maintain Kubernetes cluster stability and reliability, reducing downtime and improving overall system performance.

## Installation Requirements <a name="installation"></a>
```
pip install -r requirements.txt
```

## Usage <a name="usage"></a>

### Training Models <a name="training"></a>
1. Ensure your training data is placed in a properly formatted directory
2. Add the paths in the train_models function and the paths of the dataset paths
2. Run the model training script:
```
python ../train_models.py
```
3. This will train RandomForest classifiers for each failure type and save them to the `models/`

### Making Predictions <a name="predictions"></a>
1. Ensure all test data files are placed in the preoperly formatted directory
2. Run the prediction pipeline:
```
python ../predict.py
```
3. Check the results in the `src/result_data/` directory

## Features and Implementation <a name="features"></a>

### Model Training
- Uses RandomForest classifiers with 100 estimators
- Features used for node failure prediction: cpu_usage, memory_usage, disk_pressure, pod_restart_count
- Features used for resource exhaustion: cpu_usage, memory_usage, disk_usage, network_io
- Features used for network issue prediction: network_latency, packet_loss, dns_failures, connection_reset
- Features used for scheduling issue prediction: pending_pods, node_capacity, resource_requests, autoscaler_latency
- Standard 80/20 train/test split for model evaluation

### Prediction Pipeline
- Loads pre-trained models using joblib
- Applies models to new metric data
- Adds human-readable interpretation of binary prediction results
- Saves comprehensive results to CSV files

## Prediction Types <a name="prediction-types"></a>

### Node Failure Prediction
Identifies nodes that are at risk of complete failure based on system metrics, memory usage, CPU load, and other node-specific indicators.

### Resource Exhaustion Prediction
Detects when pods or nodes are approaching resource limits that could lead to throttling, evictions, or performance degradation.

### Network Issue Prediction
Predicts potential network connectivity problems, latency spikes, or packet loss situations before they impact service availability.

### Scheduling Issue Prediction
Forecasts situations where pod scheduling might fail due to resource constraints, node selector issues, or other scheduling-related problems.

## Model Information <a name="model-info"></a>
The system uses RandomForest classifier models (saved as .pkl files) that have been trained on historical Kubernetes metrics data. Each model is specialized for a specific type of failure prediction:

- Node Failure Predictor
- Resource Exhaustion Predictor
- Network Issue Predictor
- Scheduling Issue Predictor

## Output Format <a name="output"></a>
The prediction results are saved as CSV files with the following columns:   
- Original metrics data
- Prediction column (binary: 1 for failure, 0 for no failure)
- Human-readable label column (e.g., "Failure"/"No Failure")

## License <a name="license"></a>
This project is licensed under the MIT License .See the [LICENSE](LICENSE) file for details