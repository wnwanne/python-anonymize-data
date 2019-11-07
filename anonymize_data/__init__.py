import pandas as pd
__version__ = 'v0.1'

class BasicDataframe():
    def __init__(self, df=pd.DataFrame(), mapping={}):
        self.df = df
        self.mapping = mapping

    def anonymize(self):
        for col in list(self.mapping):
            self.df[col] = self.df[col].replace(self.mapping[col])

    def unanonymize(self):
        revert = {col: {self.mapping[col][val]: val
            for val in list(self.mapping[col])} for col in list(self.mapping)}
        for col in list(revert):
            self.df[col] = self.df[col].replace(revert[col])
