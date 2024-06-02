from typing import Tuple
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(df: pd.DataFrame, **kwargs
) -> Tuple[pd.DataFrame]:
    categorical = kwargs.get('categorical')
    train_dicts = df[categorical].to_dict(orient='records')

    dv = DictVectorizer()
    X_train = dv.fit_transform(train_dicts)

    target = kwargs.get('target')
    y_train = df[target].values

    lr = LinearRegression()
    lr.fit(X_train, y_train)
    print(lr.intercept_)

    return dv, lr