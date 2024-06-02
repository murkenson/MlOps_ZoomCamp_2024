import mlflow
import pickle
import traceback
import sys
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data(data, *args, **kwargs):
    dv, model = data

    mlflow.set_tracking_uri("http://mlflow:6001")
    
    try:
        experiment_name = "nyc-taxi-experiment"
        experiment = mlflow.get_experiment_by_name(experiment_name)
        if experiment is None:
            mlflow.create_experiment(experiment_name)
        mlflow.set_experiment(experiment_name)

        with mlflow.start_run():
            # Save DictVectorizer to a file
            encoder_path = "encoder.b"
            with open(encoder_path, "wb") as f_out:
                pickle.dump(dv, f_out)

            # Get the size of the encoder file
            encoder_size = os.path.getsize(encoder_path)

            # Log the encoder artifact and its size
            mlflow.log_artifact(encoder_path, artifact_path="encoder")
            mlflow.log_param("encoder_size_bytes", encoder_size)

            # Save and log the model
            model_path = "model_lr.pkl"
            with open(model_path, "wb") as f_out:
                pickle.dump(model, f_out)
            
            # Get the size of the model file
            model_size = os.path.getsize(model_path)

            # Log the model artifact and its size
            mlflow.log_artifact(model_path, artifact_path="model_lr")
            mlflow.log_param("model_size_bytes", model_size)
    
    except Exception as e:
        print(f"Error occurred: {e}")
        traceback.print_exc(file=sys.stdout)
    
    return data
