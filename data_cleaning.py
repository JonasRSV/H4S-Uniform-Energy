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


def smhi(dataframe: pd.DataFrame, out: str):
    smhi_data = pd.DataFrame()

    smhi_data["date"] = pd.to_datetime(dataframe["Date"])
    smhi_data["temperature"] = dataframe["Temperatur"]
    smhi_data["rain"] = dataframe["Nederbord"]

    smhi_data = smhi_data[smhi_data["date"] >= "2016-01-01"]

    smhi_data["is_snow"] = smhi_data[["temperature", "rain"]].apply(
        lambda x: int(x.iloc[0] < 0 and x.iloc[1] > 0), axis=1)

    smhi_data.to_csv(out, index=False)


if __name__ == "__main__":
    nordpool_energy(
        pd.read_csv("data/nordpool2018.csv"), "data/nordpool2018_clean.csv")
    nordpool_energy(
        pd.read_csv("data/nordpool2017.csv"), "data/nordpool2017_clean.csv")
    nordpool_energy(
        pd.read_csv("data/nordpool2016.csv"), "data/nordpool2016_clean.csv")
    smhi(pd.read_csv("data/weather1.csv"), "data/weather_1_clean.csv")
