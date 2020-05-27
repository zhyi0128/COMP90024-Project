# COMP90024 Cluster and Cloud Computing 2020 Semester1
# This project is developed by Group38
#
# Zhe Wang      951996
# Zheng Xu      785974
# Zeng Tian     1072955
# Miaoqin Li    998914
# Yuming Lin    883717

import json
import geopandas as gp

list_dic = []

path = "./geojson/greater_melb_sub.json"
df = gp.read_file(path)
# add neighbors column
df["neighbors"] = None

# from stackoverflow https://gis.stackexchange.com/questions/281652/find-all-neighbors-using-geopandas
for index, country in df.iterrows():
    # get 'not disjoint' countries
    neighbors = df[~df.geometry.disjoint(country.geometry)].name.tolist()
    # remove own name from the list
    neighbors = [name for name in neighbors if country.name != name]
    # add names of neighbors as NEIGHBORS value
    df.at[index, "neighbors"] = ", ".join(neighbors)
# save GeoDataFrame as a new json
df.to_file("./rawdata/raw_neighbors.json", driver='GeoJSON')
mel_neighbor_geojson = json.load(open('./rawdata/raw_neighbors.json'))

for i in range(0, len(mel_neighbor_geojson['features'])):
    list_dic.append(mel_neighbor_geojson['features'][i]['properties'])
# get the keys-values that we need
for item in list_dic:
    del item['id']
    del item['prim_pcode']
    del item['loccl_code']
    del item['loc_pid']
    del item['dt_retire']
    del item['dt_gazetd']
    del item['state_pid']
    del item['dt_create']
    item['neighbors'] = item['neighbors'].split(', ')
    for suburb in item['neighbors']:
        if suburb in item['name']:
            item['neighbors'].remove(suburb)

newJson = json.dumps(list_dic)
path = './result/new_neighbors.json'
file = open(path, 'w')
file.write(newJson)
file.close()
