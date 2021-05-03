from py2neo import Graph, Node, Relationship
from config import graph

graph.delete_all()  # 每次重新构建图数据库之前将之前的数据清空
with open("./raw_data/relation.txt", encoding='utf-8') as f:
    for line in f.readlines():
        rela_array=line.strip("\n").split(",")
        print(rela_array)                                                   # ['贾演', '贾代化', '父亲', '贾家宁国府', '贾家宁国府']
        graph.run("MERGE(p: Person{cate:'%s',Name: '%s'})"%(rela_array[3],rela_array[0]))  # 建立包含人物姓名和所属单位为属性的结点，从 .txt 文件第3列和第0列进行匹配
        graph.run("MERGE(p: Person{cate:'%s',Name: '%s'})" % (rela_array[4], rela_array[1]))
        graph.run(                                                          # 给已经存在的结点创建关系，其中e 和 cc 的位置可以是任意字母，只要前后使用上保持一致
            "MATCH(e: Person), (cc: Person) \
            WHERE e.Name='%s' AND cc.Name='%s'\
            CREATE(e)-[r:%s{relation: '%s'}]->(cc)\
            RETURN r" % (rela_array[0], rela_array[1], rela_array[2],rela_array[2])
        )