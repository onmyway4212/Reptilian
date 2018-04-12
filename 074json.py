import json
str = [{'username':'七夜', 'age':'24'}, (2,3),1]

#把python对象转化成JSON对象是编码
json_str = json.dumps(str, ensure_ascii=False)  #dumps是生成一个字符串
#print(json_str)

with open('qiye.txt', 'w') as f:
    json.dump(str, fp=f, ensure_ascii=False)  #ensure_ascii=False 如果dict内含有非ASCII的字符，设置false后才能正常显示

#用load和loads解码
new_str = json.loads(json_str)
print(new_str)

with open('qiye.txt', 'r') as fp:
    print(json.load(fp))
