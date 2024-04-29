import requests
import pandas as pd

def download_updated_data():
    #create a dictionnary to get the result
    race_results = {'season': [],
          'round':[],
           'circuit_id':[],
          'driver': [],
           'date_of_birth': [],
           'nationality': [],
          'constructor': [],
          'grid': [],
          'time': [],
          'status': [],
          'points': [],
          'podium': [],
          'url': []}

    # range to be updated depending on the year needed
    for date in range(1950,2025):

        #request the Ergast API to get info of each year
        url_round=f'https://ergast.com/api/f1/{date}.json'
        response_round = requests.get(url_round).json()
        print(date)

        #get the races info of each year.
        for race_round in range(len(response_round['MRData']['RaceTable']['Races'])):

            #get the race results for each year/each round
            url=f'https://ergast.com/api/f1/{date}/{race_round}/results.json'
            response = requests.get(url).json()

            print(race_round)
            if race_round: # if the race round exists

                if len(response['MRData']['RaceTable']['Races'])>0:

                    for item in response['MRData']['RaceTable']['Races'][0]['Results']:

                        try:
                            race_results['season'].append(int(response['MRData']['RaceTable']['Races'][0]['season']))
                        except:
                            race_results['season'].append(None)

                        try:
                            race_results['round'].append(int(response['MRData']['RaceTable']['Races'][0]['round']))
                        except:
                            race_results['round'].append(None)

                        try:
                            race_results['circuit_id'].append(response['MRData']['RaceTable']['Races'][0]['Circuit']['circuitId'])
                        except:
                            race_results['circuit_id'].append(None)

                        try:
                            race_results['driver'].append(item['Driver']['driverId'])
                        except:
                            race_results['driver'].append(None)

                        try:
                            race_results['date_of_birth'].append(item['Driver']['dateOfBirth'])
                        except:
                            race_results['date_of_birth'].append(None)

                        try:
                            race_results['nationality'].append(item['Driver']['nationality'])
                        except:
                            race_results['nationality'].append(None)

                        try:
                            race_results['constructor'].append(item['Constructor']['constructorId'])
                        except:
                            race_results['constructor'].append(None)

                        try:
                            race_results['grid'].append(int(item['grid']))
                        except:
                            race_results['grid'].append(None)

                        try:
                            race_results['time'].append(int(item['Time']['millis']))
                        except:
                            race_results['time'].append(None)

                        try:
                            race_results['status'].append(item['status'])
                        except:
                            race_results['status'].append(None)

                        try:
                            race_results['points'].append(int(item['points']))
                        except:
                            race_results['points'].append(None)

                        try:
                            race_results['podium'].append(int(item['position']))
                        except:
                            race_results['podium'].append(None)
                    else : continue

    # transform the dict to a dataframe
    df = pd.DataFrame.from_dict(race_results, orient='index')
    df = df.transpose()

    #new created dataframe saved in a csv file
    df.to_csv('data/race_results.csv')


if __name__ == "__main__":
    download_updated_data()
