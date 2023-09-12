import pandas as pd
import numpy as np

def points_per_year_per_driver(driver_name):
    df=pd.read_csv('data/race_results.csv')
    res = df[['season', 'driver', 'points']].groupby(['season',
                                                      'driver']).sum()
    res.reset_index(inplace=True)
    print(res[res['driver'] == driver_name])
    return res[res['driver']==driver_name]


def points_per_race_race_driver(driver_name, race_name):
    df = pd.read_csv('data/race_results.csv')
    res = df[['season', 'driver', 'circuit_id','points']].groupby(['season',
                                                      'driver','circuit_id']).sum()
    res.reset_index(inplace=True)
    print(res[np.logical_and((res['driver'] == driver_name),
              (res['circuit_id'] == race_name))])
    return res[np.logical_and((res['driver'] == driver_name),
                               (res['circuit_id'] == race_name))]

def average_end_position(driver_name):
    df = pd.read_csv('data/race_results.csv')
    res = df[['season', 'driver', 'podium']].groupby(['season', 'driver']).mean()
    res.reset_index(inplace=True)
    print(res[res['driver'] == driver_name])
    return res[res['driver'] == driver_name]

def average_points_per_race(driver_name):
    df = pd.read_csv('data/race_results.csv')
    res = df[['season', 'driver', 'points']].groupby(['season',
                                                      'driver']).mean()
    res.reset_index(inplace=True)
    print(res[res['driver'] == driver_name])
    return res[res['driver'] == driver_name]

def number_race_per_driver(driver_name):
    df = pd.read_csv('data/race_results.csv')
    res = df[['driver', 'points']].groupby(['driver']).count()
    res.reset_index(inplace=True)
    print(res[res['driver'] == driver_name])
    return res[res['driver'] == driver_name]





if __name__ == "__main__":
    #points_per_year_per_driver('sainz')
    #points_per_race_race_driver('sainz', 'silverstone')
    #average_end_position('sainz')
    #average_points_per_race('sainz')
    number_race_per_driver('sainz')
