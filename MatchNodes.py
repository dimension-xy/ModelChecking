import time
from py2neo import Graph
from pandas import DataFrame

start = time.time()

graph = Graph("http://neo4j:mypassword@:7474/db/data/")

df = DataFrame(graph.data("""
            MATCH (start: Person{name: 'A'}), (end: Person{name: 'D'}),
            path = (start)-[*]->(end)
            WITH EXTRACT(person IN NODES (path) | person.name) AS allpath
            RETURN allpath;
"""))

print df

end = time.time() - start

print ("\ntime:{0}".format(end) + "[sec]")