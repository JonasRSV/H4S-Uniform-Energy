import numpy as np
import pandas as pd
import re


def str2float(x: "unknown"):
    if x == "nan":
        return 0
    elif x != x:
        return 0
    elif type(x) == str:
        return float(x.replace(",", "."))
    elif type(x) == float:
        return x
    else:
        return float(x)


def nordpool_energy(dataframe: pd.DataFrame, out: str):
    swedish_energy_data = pd.DataFrame()

    swedish_energy_data["price"] = dataframe["SE4"].apply(str2float)
    swedish_energy_data["date"] = dataframe["Unnamed: 0"]
    swedish_energy_data["hour"] = dataframe["Hours"].apply(
        lambda x: x[:3].strip())
    swedish_energy_data["day"] = dataframe["Unnamed: 0"].apply(
        lambda x: re.findall("(..)-*", x)[0])
    swedish_energy_data["month"] = dataframe["Unnamed: 0"].apply(
        lambda x: re.findall("..-(..)-*", x)[0])
    swedish_energy_data["year"] = dataframe["Unnamed: 0"].apply(
        lambda x: re.findall("..-..-(....)", x)[0])
    swedish_energy_data.fillna(0)
    swedish_energy_data.to_csv(out, index=False)


if __name__ == "__main__":
    nordpool_energy(
        pd.read_csv("data/nordpool2018.csv"), "data/nordpool2018_clean.csv")
    nordpool_energy(
        pd.read_csv("data/nordpool2017.csv"), "data/nordpool2017_clean.csv")
    nordpool_energy(
        pd.read_csv("data/nordpool2016.csv"), "data/nordpool2016_clean.csv")
