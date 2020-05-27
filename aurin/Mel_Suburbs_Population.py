# COMP90024 Cluster and Cloud Computing 2020 Semester1
# This project is developed by Group38
#
# Zhe Wang      951996
# Zheng Xu      785974
# Zeng Tian     1072955
# Miaoqin Li    998914
# Yuming Lin    883717

import json

# read geojson and aurin data
mel_geojson = json.load(open('./geojson/greater_melb_sub.json'))
raw_population = json.load(open('./rawdata/Mel_Population.json'))
# list_dic is to save raw data in aurin; final_list is to save the final json style
list_dic = []
final_list = []
# read name from geojson
au_suburbs_name = [i['properties']['name'] for i in mel_geojson["features"]]
print(au_suburbs_name)

# match the name
for i in range(0, len(raw_population['features'])):
    print(raw_population['features'][i]['properties']['sa2_name16'])

    for suburb in au_suburbs_name:
        if suburb.lower() == raw_population['features'][i]['properties']['sa2_name16'].lower():
            raw_population['features'][i]['properties']['sa2_name16'] = suburb
            list_dic.append(raw_population['features'][i]['properties'])

print(list_dic)


# rename all keys in the list_dic
for item in list_dic:
    del item['sa2_main16']
    item.update({'name': item.pop('sa2_name16')})
    item.update({'year': item.pop('yr')})
    item.update({'Total population': item.pop('est_res_pop_ur_erp_30_jun_p_tot_num')})
    item.update({'Median age': item.pop('est_res_pop_ur_erp_30_jun_med_age_ur_erp_30_jun_p_yrs')})
    item.update({'Total male population': item.pop('est_res_pop_ur_erp_30_jun_m_tot_num')})
    item.update({'Total Female population': item.pop('est_res_pop_ur_erp_30_jun_f_tot_num')})
    item.update({'0 to 14 years old': item.pop('est_res_pop_ur_erp_30_jun_p_0_14_yrs_pr100')})
    item.update({'15 to 24 years old': item.pop('est_res_pop_ur_erp_30_jun_p_15_24_yrs_pr100')})
    item.update({'25 to 34 years old': item.pop('est_res_pop_ur_erp_30_jun_p_25_34_yrs_pr100')})
    item.update({'35 to 44 years old': item.pop('est_res_pop_ur_erp_30_jun_p_35_44_yrs_pr100')})
    item.update({'45 to 54 years old': item.pop('est_res_pop_ur_erp_30_jun_p_45_54_yrs_pr100')})
    item.update({'55 to 64 years old': item.pop('est_res_pop_ur_erp_30_jun_p_55_64_yrs_pr100')})
    item.update({'65 to 74 years old': item.pop('est_res_pop_ur_erp_30_jun_p_65_74_yrs_pr100')})
    item.update({'75 to 84 years old': item.pop('est_res_pop_ur_erp_30_jun_p_75_84_yrs_pr100')})
    item.update({'85 to 99 years old': item.pop('est_res_pop_ur_erp_30_jun_p_85_yrs_ov_pr100')})

    # different dic to save the data style we need; final_dict is to combine all dic
    gender_proportion = {}
    age_proportion = {}
    final_dict = {}

    # save value to different dic
    for key in item:
        if key == 'Total male population':
            gender_proportion['Total male population'] = item.get('Total male population')
        if key == 'Total Female population':
            gender_proportion['Total Female population'] = item.get('Total Female population')
        if key == '0 to 14 years old':
            age_proportion['0 to 14 years old'] = item.get('0 to 14 years old')
        if key == '15 to 24 years old':
            age_proportion['15 to 24 years old'] = item.get('15 to 24 years old')
        if key == '25 to 34 years old':
            age_proportion['25 to 34 years old'] = item.get('25 to 34 years old')
        if key == '35 to 44 years old':
            age_proportion['35 to 44 years old'] = item.get('35 to 44 years old')
        if key == '45 to 54 years old':
            age_proportion['45 to 54 years old'] = item.get('45 to 54 years old')
        if key == '55 to 64 years old':
            age_proportion['55 to 64 years old'] = item.get('55 to 64 years old')
        if key == '65 to 74 years old':
            age_proportion['65 to 74 years old'] = item.get('65 to 74 years old')
        if key == '75 to 84 years old':
            age_proportion['75 to 84 years old'] = item.get('75 to 84 years old')
        if key == 'over 85 years old':
            age_proportion['85 to 99 years old'] = item.get('85 to 99 years old')

    # combine all dic to final_dict
    final_dict['Name'] = item.get('name')
    final_dict['Total population'] = item.get('Total population')
    final_dict['Median age'] = item.get('Median age')
    final_dict['Gender proportion'] = gender_proportion
    final_dict['Age proportion'] = age_proportion

    final_list.append(final_dict)

    # print(gender_proportion)
    # print(age_proportion)
print(final_list)

# write json
newJson = json.dumps(final_list)
path = './result/mel_suburbs_population.json'
file = open(path, 'w')
file.write(newJson)
file.close()
