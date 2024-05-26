EXPERIMENT_NAME = 'hw-2-experiment'

import os
import pickle
import click

import mlflow
import mlflow.sklearn

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error


def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


@click.command()
@click.option(
    "--data_path",
    default="./output",
    help="Location where the processed NYC taxi trip data was saved"
)
def run_train(data_path: str):

    # Set the MLflow tracking URI
    mlflow.set_tracking_uri('sqlite:///mlflow.db')

    # Set the experiment
    mlflow.set_experiment(EXPERIMENT_NAME)

    # Enable MLflow autologging
    mlflow.sklearn.autolog()

    X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
    X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))

    with mlflow.start_run():  # wrap train with mlflow
        print(f'Starting experiment {EXPERIMENT_NAME}')
        rf = RandomForestRegressor(max_depth=10, random_state=0)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_val)

        rmse = root_mean_squared_error(y_val, y_pred)
        mlflow.log_metric("rmse", rmse)  # Log RMSE as a metric

        print("Experiment finished")

    # Disable autologging to avoid potential issues
    mlflow.sklearn.autolog(disable=True)

if __name__ == '__main__':
    run_train()