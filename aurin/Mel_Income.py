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
raw_population = json.load(open('./rawdata/Mel_Income.json'))
# list_dic is to save raw data in aurin; final_list is to save the final json style
list_dic = []
final_list = []
# read name from geojson
au_suburbs_name = [i['properties']['name'] for i in mel_geojson["features"]]
# match the name
for i in range(0,len(raw_population['features'])):
    for suburb in au_suburbs_name:
        if suburb.lower() == raw_population['features'][i]['properties']['sa2_name16'].lower():
            raw_population['features'][i]['properties']['sa2_name16'] = suburb
            list_dic.append(raw_population['features'][i]['properties'])



# rename all keys in the list_dic
for item in list_dic:
    del item['sa2_main16']
    del item['ogc_fid']
    item.update({'name': item.pop('sa2_name16')})
    item.update({'year': item.pop('yr')})
    item.update({'Personal mean total income': item.pop('est_p_inc_avg_tot_inc_excl_gov_pnsn_aud')})
    item.update({'Personal median total income': item.pop('est_p_inc_med_tot_inc_excl_gov_pnsn_aud')})
    item.update({'Employee personal income': item.pop('est_p_inc_emply_inc_mn_src_inc_pr100')})
    item.update({'Investment personal income': item.pop('est_p_inc_investment_inc_mn_src_inc_pr100')})
    item.update({'Own unincorporated business income': item.pop('est_p_inc_own_unincorportd_bsns_inc_mn_src_inc_pr100')})
    item.update({'Superannuation & annuity income': item.pop('est_p_inc_super_annuity_inc_mn_src_inc_pr100')})
    item.update({'Negative income': item.pop('tot_p_inc_wk_p_ov_15_yrs_p_negative_inc_pr100')})
    item.update({'Zero income': item.pop('tot_p_inc_wk_p_ov_15_yrs_p_earn_nil_inc_pr100')})
    item.update({'1$ to 499$ per week': item.pop('tot_p_inc_wk_p_ov_15_yrs_p_earn_aud1_aud499wk_pr100')})
    item.update({'500$ to 999$ per week': item.pop('tot_p_inc_wk_p_ov_15_yrs_p_earn_aud500_aud999wk_pr100')})
    item.update({'1000$ to 1999$ per week': item.pop('tot_p_inc_wk_p_ov_15_yrs_p_earn_aud1000_aud1999wk_pr100')})
    item.update({'2000$ to 2999$ per week': item.pop('tot_p_inc_wk_p_ov_15_yrs_p_earn_aud2000_aud2999wk_pr100')})
    item.update({'Over 3000$ per week': item.pop('tot_p_inc_wk_p_ov_15_yrs_p_earn_aud3000_plswk_pr100')})

    # different dic to save the data style we need; final_dict is to combine all dic
    source_proportion = {}
    income_proportion = {}
    final_dict = {}

    # save value to different dic
    for key in item:
        if key == 'Employee personal income':
            source_proportion['Employee personal income'] = item.get('Employee personal income')
        if key == 'Investment personal income':
            source_proportion['Investment personal income'] = item.get('Investment personal income')
        if key == 'Own unincorporated business income':
            source_proportion['Own unincorporated business income'] = item.get('Own unincorporated business income')
        if key == 'Superannuation & annuity income':
            source_proportion['Superannuation & annuity income'] = item.get('Superannuation & annuity income')
        if key == 'Negative income':
            income_proportion['Negative income'] = item.get('Negative income')
        if key == 'Zero income':
            income_proportion['Zero income'] = item.get('Zero income')
        if key == '1$ to 499$ per week':
            income_proportion['1$ to 499$ per week'] = item.get('1$ to 499$ per week')
        if key == '500$ to 999$ per week':
            income_proportion['500$ to 999$ per week'] = item.get('500$ to 999$ per week')
        if key == '1000$ to 1999$ per week':
            income_proportion['1000$ to 1999$ per week'] = item.get('1000$ to 1999$ per week')
        if key == '2000$ to 2999$ per week':
            income_proportion['2000$ to 2999$ per week'] = item.get('2000$ to 2999$ per week')
        if key == 'Over 3000$ per week':
            income_proportion['Over 3000$ per week'] = item.get('Over 3000$ per week')

    # combine all dic to final_dict
    final_dict['Name'] = item.get('name')
    final_dict['Personal mean total income'] = item.get('Personal mean total income')
    final_dict['Personal median total income'] = item.get('Personal median total income')
    final_dict['Main source proportion'] = source_proportion
    final_dict['Income proportion'] = income_proportion

    final_list.append(final_dict)

    # print(source_proportion)
    # print(income_proportion)
print(final_list)

# write json
newJson = json.dumps(final_list)
path = './result/mel_income.json'
file = open(path,'w')
file.write(newJson)
file.close()


