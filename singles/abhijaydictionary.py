import json

# This is the place where I create my dictionary and I have 4 attributes for each person.

me = { "name":"Abhijay", "age":17, "birthplace":"US", "city":"San Diego"}
sibling = { "name":"Aneesh", "age":10, "birthplace":"US", "city":"Denver"}
parent1 = { "name":"Vanaja", "age":16, "birthplace":"India", "city":"Hyderabad"}
parent2 = { "name":"Srinivas", "age":16, "birthplace":"India", "city":"Vijayawada"}
grandparent1 = { "name":"Radhakrishna", "age":16, "birthplace":"India", "city":"Delhi"}
grandparent2 = { "name":"Lakshmi", "age":16, "birthplace":"India", "city":"Vijayawada"}

# This is the code where it allows me to turn the dictionary into a list
# This is the line that makes the dictionary into a list with the variable list_of_family
list_of_family = [me, sibling, parent1, parent2, grandparent1, grandparent2]
# This first just prints a statement
print("List of my family")
# This line prints out the type of the variable, "list_of_family". In this case, it is a list, so the output would be class: list
print(type(list_of_family))
# This line creates an unformatted version of the dictionary. It literally just puts each dictionary next to each other.
print(list_of_family)
# This line creates a for loop where it iterates through the variable and checks each part of the list
# It first starts with me, where finds each part of the dictionary. Inside the [ ], it holds the key that the code looks for
# Right next to the key is the item, which the code outputs.
# We also put in a comma plus a space in between each item to make it look clean
# This cycles through for every part of the list
for person in list_of_family:
    print(person['name'] + ", " + str(person['age']) + ", " + person['birthplace'] + ", " + person['city'])
print()



# This code takes that list we created before and converts it back to a dictionary
# Here, we are introducing a new variable called dict_family, and we are creating a dictionary with it
# In the dictionary, we are putting our list that we created before in line 14
dict_family = {'people': list_of_family}
# Now we have a basic print statement that just says "dictionary of family"
print("Dictionary of family")
# This peice of code once again just prints the type of the variable. In this case, it is a dictionary, so it should output "class: dictionary"
print(type(dict_family))
# This prints out the list_of_family list that was stored into the dict_family variable
print(dict_family)
# Here we are creating a new variable, "list_of_family2" and we are taking the information from the dict_family variable
list_of_family2 = dict_family['people']
# Now, we create another for loop and basically do exactly what was done in line 26.
for person in list_of_people2:
    print(person['name'] + ", " + str(person['age']) + ", " + person['birthplace'] + ", " + person['city'])
print()

# Now we are taking that dictionary and we are turning into a JSON
# This peice of code here creates a new variable called json_family which is converting the list we created earlier (list_of_family) and turning into a JSON with the json.dump command
json_family = json.dumps(list_of_family)
# Just printing out "JSON Family #1"
print("JSON Family #1")
# This is once again printing the type of our new variable, json_family, which should turn out to be "class: json"
print(type(json_family))
# This here prints out what json_family holds, which is a JSON version of the out list, list_of_family
print(json_family)
# This code creates another for loop
# The char here is stating that after every character, we are putting in a plus sign.
# This repeats throughout each piece of the list and adds a plus after every single character
for char in json_family:
    print(char, end = "+")
print()


# Here we are once again turning our dictionary into a JSON using the json.dumps command
json_family2 = json.dumps(list_of_family)
# This piece of code is just printing the statement "JSON People #2"
print("JSON People #2")
# This is just printing out the type of that json_family2 variable
print(type(json_family2))
# This is printing out all the contents of the json_family2 variable
print(json_family2)
# Now we are unloading this variable into a new variable called json_family3 using the json.loads variable
json_family3 = json.loads(json_family2)
# Now we start up another for loop which looks just like the sentence we got from the first 2 things we did
for person in json_family3:
    print(person['name'] + ", " + str(person['age']) + ", " + person['birthplace'] + ", " + person['city'])
print()
