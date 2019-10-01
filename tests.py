import pandas as pd
import numpy as np
from copy import deepcopy
import anonymize_data as ad

def get_df():
    return pd.DataFrame({
        'old_column2': np.random.randint(1, 100, (10,)),
        'old_column1': np.random.randint(1, 100, (10,)),
        'old_column3': np.random.randint(1, 100, (10,))
    })

def test_df_anonymize():
    helper = ad.BasicDataframe()
    df = get_df()
    mapping = {col: {str(val): str(val*2) for val in df[col].unique()}
        for col in df.columns}
    df = df.astype(str)
    helper.df = df.copy()
    helper.mapping = deepcopy(mapping)
    helper.anonymize()
    old = df.columns.tolist()
    new = helper.df.columns.tolist()
    assert any([all(helper.df[old[i]] != df[new[i]]) for i in range(len(old))])

def test_df_unanonymize():
    helper = ad.BasicDataframe()
    df = get_df()
    mapping = {col: {str(val): str(val*2) for val in df[col].unique()}
        for col in df.columns}
    df = df.astype(str)
    helper.df = df.copy()
    helper.mapping = deepcopy(mapping)
    helper.anonymize()
    helper.unanonymize()
    old = df.columns.tolist()
    new = helper.df.columns.tolist()
    assert any([all(helper.df[old[i]] == df[new[i]]) for i in range(len(old))])


if __name__ == '__main__':
    test_df_anonymize()
    test_df_unanonymize()
