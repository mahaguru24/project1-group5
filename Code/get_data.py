import os
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd

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