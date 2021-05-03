from neo_db.config import graph, CA_LIST, similar_words
from spider.show_profile import get_profile
import codecs
import os
import json
import base64

## cate 代表 category 指的是人物所属的府邸
def query(name):
    data = graph.run(     # 匹配所有与查询人有关系的完整数据（无论是正向关系还是反向关系），包括实体及其各种属性
    "match(p)-[r]->(n:Person{Name:'%s'}) return  p.Name,r.relation,n.Name,p.cate,n.cate\
        Union all\
     match(p:Person {Name:'%s'}) -[r]->(n) return p.Name, r.relation, n.Name, p.cate, n.cate" % (name,name)
    )                     
    data = list(data)
    return get_json_data(data)  # 
def get_json_data(data):
    json_data={'data':[],"links":[]}
    d=[]
    for i in data:
        # print(i["p.Name"], i["r.relation"], i["n.Name"], i["p.cate"], i["n.cate"])
        d.append(i['p.Name']+"_"+i['p.cate'])
        d.append(i['n.Name']+"_"+i['n.cate'])
        d=list(set(d))   # 人物与所属单位组成的字符串为元素的字典去重后建立列表
    name_dict={}
    count=0
    for j in d:
        j_array=j.split("_")
    
        data_item={}
        name_dict[j_array[0]]=count
        count+=1
        data_item['name']=j_array[0]
        data_item['category']=CA_LIST[j_array[1]]
        json_data['data'].append(data_item)
    for i in data:
   
        link_item = {}
        
        link_item['source'] = name_dict[i['p.Name']]
        
        link_item['target'] = name_dict[i['n.Name']]
        link_item['value'] = i['r.relation']
        json_data['links'].append(link_item)

    return json_data
# f = codecs.open('./static/test_data.json','w','utf-8')
# f.write(json.dumps(json_data,  ensure_ascii=False))  # json.dumps将一个Python数据结构转换为JSON
def get_KGQA_answer(array):
    data_array=[]
    print(len(array))
    array_length = len(array)

    for i in range(array_length-1):
        if i==0:
            name=array[0]
        else:
            name=data_array[-1]['p.Name']
            print(name)
           
        data = graph.run("match(p)-[r:%s{relation: '%s'}]->(n:Person{Name:'%s'}) return  p.Name,n.Name,r.relation,p.cate,n.cate" % (similar_words[array[i+1]], similar_words[array[i+1]], name))
        data = list(data)
        print(data)
        data_array.extend(data)
        
        print("==="*36)
    with open("./spider/images/"+"%s.jpg" % (str(data_array[-1]['p.Name'])), "rb") as image:
            base64_data = base64.b64encode(image.read())
            b=str(base64_data)
          
    return [get_json_data(data_array), get_profile(str(data_array[-1]['p.Name'])), b.split("'")[1]]
def get_answer_profile(name):
    with open("./spider/images/"+"%s.jpg" % (str(name)), "rb") as image:
        base64_data = base64.b64encode(image.read())
        b = str(base64_data)
    return [get_profile(str(name)), b.split("'")[1]]