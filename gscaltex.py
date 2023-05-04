import re
import json
import os
from pathlib import Path
path="D:\\recorded_files\\"
file_list=os.listdir(path)
file_list_dat=[file for file in file_list if file.endswith(".dat")]
mod_dict ={}
with open(path+"mod_param.txt", mode="r", encoding="UTF-8") as mod_file:
        modfile = mod_file.readlines()
for modParam in modfile:
    tempArray = modParam.strip().split(" ")
    mod_dict[tempArray[0]] = tempArray[1];
def change_json_param(json_dict, param_name, new_value):
    for key in json_dict.keys():
        # 파라미터 이름이 일치하면 값을 변경
        if key == param_name:
            json_dict[key] = new_value
        else:
            # 파라미터가 dict 형식이면 재귀 호출
            if isinstance(json_dict[key], dict):
                change_json_param(json_dict[key], param_name, new_value)
            # 파라미터가 list 형식이면 각 요소에 대해 재귀 호출
            elif isinstance(json_dict[key], list):
                for item in json_dict[key]:
                    if isinstance(item, dict):
                        change_json_param(item, param_name, new_value)
# 파일 열기 및 읽어오기
for file_dat in file_list_dat:
    print("File Input: ",path+file_dat)
    with open(path+file_dat, mode="r", encoding="ISO-8859-1") as file:
        content = file.readlines()
    result_list = []
    for line in content:
        if(line.find('{',0,2) != -1):
            start = line.find('{')
            end = line.split('TPMS002')[0].rfind('}')
            sum = line[start:end+1]
            parsed_json = json.loads(sum)
            for modDict in mod_dict.keys():
                change_json_param(parsed_json, modDict, mod_dict[modDict])
            #result_list.append(json.dumps(parsed_json,ensure_ascii=False))
            result_list.append(json.dumps(parsed_json,ensure_ascii=False).replace('": ','":').replace(', ',','))
            result_list.append(line[end+1:])
        else:
            result_list.append(line)
    file.close()
    write_file_path = path
    write_file_name = "mod_"+file_dat
    print("File Output: ",write_file_path + write_file_name)
    with open(write_file_path + write_file_name, 'w', encoding='ISO-8859-1') as f:
        f.writelines(result_list)
