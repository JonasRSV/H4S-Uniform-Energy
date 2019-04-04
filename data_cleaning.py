import numpy as np
import pandas as pd

def str2float(x: "unknown"):
    if type(x) == str:
        return float(x.replace(",", "."))
    elif type(x) == float:
        return x
    else:
        return float(x)

def nordpool_energy(dataframe: pd.DataFrame, out: str):
    swedish_energy_data = pd.DataFrame()

    swedish_energy_data["price"] = dataframe["SE4"].apply(str2float)
    swedish_energy_data["date"] = dataframe.index.values
    swedish_energy_data["hour"] = dataframe["Hours"].apply(lambda x: x[:3].strip())
    swedish_energy_data.to_csv(out, index=False)

    



if __name__ == "__main__":
    nordpool_energy(pd.read_csv("data/nordpool2018.csv"), "data/nordpool2018_clean.csv")

