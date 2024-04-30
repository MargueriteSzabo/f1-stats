import pandas as pd


def num_round_per_circuit(): # no parameters; just updated after new rounds
    # gives the number of races on each circuits
    df=pd.read_csv('data/race_results.csv')
    res = df[['circuit_id','season']].groupby(['circuit_id']).nunique().sort_values(by='season',
                                                                ascending = False)
    res.rename(columns={'season':'Number of rounds'}, inplace=True)
    return res

def winner_per_circuit(circuit):
    #gives the top winners per circuits
    df=pd.read_csv('data/race_results.csv')
    res = df[['circuit_id', 'driver']].groupby(['circuit_id']).value_counts()
    res = pd.DataFrame(res)
    res.reset_index(inplace=True)
    res = res[res['circuit_id']==circuit].head()
    return res




if __name__ == "__main__":
    #num_round_per_circuit()
    winner_per_circuit('silverstone')
