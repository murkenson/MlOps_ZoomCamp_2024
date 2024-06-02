from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(df: pd.DataFrame, **kwargs):
    categorical = ["PULocationID", "DOLocationID"]
    target = "duration"
    # Fit a dict vectorizer
    dv = DictVectorizer()

    train_dicts = df[categorical].to_dict(orient="records")
    X_train = dv.fit_transform(train_dicts)

    y_train = df[target].values

    # Train a linear regression with default parameres
    lr = LinearRegression()
    lr.fit(X_train, y_train)

    print("Intercept:", lr.intercept_)

    return dv, lr