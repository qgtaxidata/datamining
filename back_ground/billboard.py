"""
    Billboard location recommendation
"""
import pandas as pd
import numpy as np

data = pd.read_csv('trajectories12.csv')
geo_hash_set = list(set(data['GEOHASH_BEGIN'].values) | set(data['GEOHASH_END'].values))
m, n = len(geo_hash_set), 5
data_df = pd.DataFrame(np.zeros((m, n), dtype=np.str), columns=['geohash', 'flow', 'arrival_rate',
                                                                'daytime', 'weekday'])
for i in range(m):
    data_df.iloc[i, 0] = geo_hash_set[i]