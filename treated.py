import pandas as pd
import ast

data = pd.read_csv(
    'C://Users/felip/OneDrive/Documents/creditdecisionresultlogs_hour.csv', sep=",")

data.head()

data["Logs"] = data["Logs"].apply(ast.literal_eval)


dflogs = pd.concat({k: pd.DataFrame(v) for k, v in data['Logs'].items()})
