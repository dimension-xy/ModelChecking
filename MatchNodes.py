from py2neo import Graph

graph = Graph("http://neo4j:mypassword@:7474/db/data/")

dict = graph.data("MATCH (n) RETURN n")

print dict