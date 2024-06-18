#!/usr/bin/env python
# coding: utf-8

import pickle
import pandas as pd
import sys

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    categorical = ['PULocationID', 'DOLocationID']
    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df


def validate(taxi_type, year, month):

    # load model
    print(f"loading model")
    with open('model.bin', 'rb') as f_in:
        dv, model = pickle.load(f_in)
    
    # read data
    file_name = f'https://d37ci6vzurychx.cloudfront.net/trip-data/{taxi_type}_tripdata_{year:04d}-{month:02d}.parquet'

    print(f"reading file: {file_name}")    
    df = read_data(file_name)

    categorical = ['PULocationID', 'DOLocationID']
    dicts = df[categorical].to_dict(orient='records')
    
    # predict
    print(f"applying model")
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)

    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')

    # save predictions
    print(f"saving predictions")
    df_result = pd.DataFrame(data={"ride_id": df['ride_id'], "predictions": y_pred})
    
    output_file = f"{year:04d}-{month:02d}_predictions.parquet"
    
    df_result.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False
    )

    print(f"Mean of predictions: {round(y_pred.mean(axis=0), 2)}")

if __name__ == "__main__":
    
    taxi_type = sys.argv[1]  # "yellow"
    year = int(sys.argv[2])  # 2023
    month = int(sys.argv[3]) # 3
    
    validate(taxi_type, year, month)