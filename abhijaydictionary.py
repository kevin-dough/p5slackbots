import json

# This is the place where I create my dictionary and I have 4 attributes for each person.
me = { "name":"Abhijay", "age":17, "birthplace":"US", "city":"San Diego"}
sibling = { "name":"Aneesh", "age":10, "birthplace":"US", "city":"Denver"}
parent1 = { "name":"Vanaja", "age":16, "birthplace":"India", "city":"Hyderabad"}
parent2 = { "name":"Srinivas", "age":16, "birthplace":"India", "city":"Vijayawada"}
grandparent1 = { "name":"Radhakrishna", "age":16, "birthplace":"India", "city":"Delhi"}
grandparent2 = { "name":"Lakshmi", "age":16, "birthplace":"India", "city":"Vijayawada"}

# a list of dictionaries
list_of_family = [me, sibling, parent1, parent2, grandparent1, grandparent2]
print("List of my family")
print(type(list_of_family))
print(list_of_family)
for person in list_of_family:
    print(person['name'] + ", " + str(person['age']) + ", " + person['birthplace'] + ", " + person['city'])
print()



# turn list to dictionary of people
dict_people = {'people': list_of_people}
print("Dictionary of people")
print(type(dict_people))
print(dict_people)
# write some code to Print People from Dictionary
list_of_people2 = dict_people['people']
for person in list_of_people2:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()

# turn dictionary to JSON (aka string)
json_people = json.dumps(list_of_people)
print("JSON People #1")
print(type(json_people))
print(json_people)
# write some code to print a space between each character of JSON
# hint use print(char, end ="-")
# INSERT CODE HERE
for char in json_people:
    print(char, end = "+")
print()


# turn dictionary to JSON, this can be sent via a browser
json_people = json.dumps(list_of_people)
# the result is a JSON file:
print("JSON People #2")
print(type(json_people))
print(json_people)
# write some code to unwind JSON using json.loads and print the people
# INSERT CODE HERE
unload_json_people = json.loads(json_people)
for person in unload_json_people:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()
