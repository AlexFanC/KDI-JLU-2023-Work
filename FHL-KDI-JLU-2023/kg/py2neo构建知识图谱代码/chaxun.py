from py2neo import Graph

# 建立与数据库的连接
graph = Graph("bolt://localhost:7689",user="neo4j",password="neo4jneo4j")

# 编写 Cypher 查询
cypher_query = """
MATCH (n:证券公司)
WITH n.name AS name, n.age AS age, COLLECT(n) AS nodelist, COUNT(*) AS count
WHERE count > 1
CALL apoc.refactor.mergeNodes(nodelist) YIELD node
RETURN node
"""

# 执行查询
result = graph.run(cypher_query)

# 处理结果
for record in result:
    print(record)
