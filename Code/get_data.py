import os
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd
import panel as pn
import plotly.express as px
import hvplot.pandas
import matplotlib.pyplot as plt


def get_alien_data():
    file_path = Path("../Resources/Scrubbed_data.csv")
    alien_df = pd.read_csv(file_path)
    alien_df['duration (seconds)'] = alien_df['duration (seconds)'].astype(float)
    alien_df = alien_df.rename(columns={"city_1": "city"})
    return alien_df
    # data cleaning    
    # alien_df = alien_data.groupby('city').size().reset_index(name='Number of Sightings')
    # return alien_df

def get_cleaned_alien_data():
    file_path = Path("../Resources/Cleansed_Alien_DataSet.csv")
    alien_df = pd.read_csv(file_path)
    return alien_df


def get_military_bases():
    military_data = Path("../Resources/military-bases.csv")
    military_df = pd.read_csv(military_data)
    return military_df

def get_combined_data():
# todo check do we need it    
    return pd.concat([get_alien_data(), get_military_bases()], axis="columns", join="inner")

def yearly_sightings():
    csvpath = Path("../Resources/sightings_all_years.csv")
    years_df = pd.read_csv(csvpath)
    years_df = years_df.sort_index()
    return years_df

def monthly_sightings():
    csvpath = Path("../Resources/scrubbed_sarah_cleanup.csv")
    sightings_df = pd.read_csv(
    csvpath, index_col="datetime", infer_datetime_format=True, parse_dates=True)
    sightings_df = sightings_df.sort_index()
    sightings_month  = sightings_df[["month","sightings"]]
    sightings_per_month = sightings_month.groupby("month").sum().reset_index()
    new_index = [3,7,11,1,0,6,5,2,4,10,9,8]
    sightings_per_month["new index"] = new_index
    sightings_per_month = sightings_per_month.set_index(["new index"])
    sightings_per_month = sightings_per_month.sort_index(ascending=True)
    sightings_per_month['percent'] = (sightings_per_month['sightings'] / 
                                  sightings_per_month['sightings'].sum()) * 100
    return sightings_per_month


def daily_sightings():
    csvpath = Path("../Resources/scrubbed_sarah_cleanup.csv")
    sightings_df = pd.read_csv(
    csvpath, index_col="datetime", infer_datetime_format=True, parse_dates=True)
    sightings_df = sightings_df.sort_index()
    sightings_day  = sightings_df[["day","sightings"]]
    sightings_per_day = sightings_day.groupby("day").sum().reset_index()
    new_index = [5,1,6,0,4,2,3]
    sightings_per_day["new index"] = new_index
    sightings_per_day = sightings_per_day.set_index(["new index"])
    sightings_per_day = sightings_per_day.sort_index(ascending=True)
    sightings_per_day['percent'] = (sightings_per_day['sightings'] / 
                              sightings_per_day['sightings'].sum()) * 100
    return sightings_per_day