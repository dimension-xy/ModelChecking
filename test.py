from py2neo import Graph

graph = Graph("http://neo4j:mypassword@:7474/db/data/")

statement = """
  MERGE (person:Person {name:{person_name}}) ON CREATE SET
    person.age = {person_age},
    person.sex = {person_sex}

  MERGE (pet:Pet {name:{pet_name}}) ON CREATE SET
    pet.type = {pet_type}

  MERGE (person)-[:owns]->(pet)

  RETURN person
  """

tx = graph.begin()

persons = [
    {'name': 'Homer', 'age': 32, 'sex': 'Male', 'pet_name': 'Buller', 'pet_type': 'Dog'},
    {'name': 'Lucy', 'age': 12, 'sex': 'Male', 'pet_name': 'Buller', 'pet_type': 'Dog'},
    {'name': 'Lucy', 'age': 12, 'sex': 'Male', 'pet_name': 'Betty', 'pet_type': 'Cat'}
]

for person in persons:
    print person
    tx.append(statement, {
      'person_name': person['name'],
      'person_age': person['age'],
      'person_sex': person['sex'],

      'pet_name': person['pet_name'],
      'pet_type': person['pet_type']
    })

tx.process()

tx.commit()
