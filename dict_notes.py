
# # lists in square brackets broken into new lines for readability, separated by commas and each item of list being within inverted commas.

# things= [ "ipad - green ",
#          "bottle - blue ",
#          "lamp - black"]
# print (things[2])
# things[2]= "lamp-white"  # change the item at index position [2]
# print (things)
# print(len(things))   # to find the number of characters/ items in list]
# # list methods
# ## object.method()
# ## list.list.method()
# # after 'list._' whatever in purple box is a method of list
# things.append(" stand ")
# things.insert(2," mouse ")
# print (things)

#------------------------------------------------------------

# Activity 1

# shopping_list = [
#     "apple",
#     "carrot",
#     "pizza",
#     "carrot",
#     "dog food",
#     "orange juice",
#     "egg",
#     "kale",
#     "carrot",
#     "kale",
#     "orange juice",
#     "kale",
#     "toilet roll",
#     "stamps",
#     "noodles",
#     "pasta sauce",
#     "egg",
#     "pasta sauce"
# ]
# egg = (shopping_list.count("egg")) 
# kale = (shopping_list.count("kale")) 
# stamps = (shopping_list.count("stamps")) 
# carrot = (shopping_list.count("carrot")) 
# orangej = (shopping_list.count("orange juice")) 
# # print (f"You have ordered {egg} eggs")
# # print (f"You have ordered {kale} kales")
# # print (f"You have ordered {stamps} stamps")
# # print (f"You have ordered {carrot} carrots")
# # print (f"You have ordered {orangej} orange juice")
# print (f"You have ordered {egg} eggs, {kale} kales, {stamps} stamps, {carrot} carrots and {orangej} orange juice.")

# dictionaries- {"Key":"value", "key":"value"}
# dict are items with key and value separated by colon in inverted commas, and each item is separated by a comma.
# dict is immutable= i.e: data cannot be changed. (just like in word dict- data type not changed after its made.) 

# capital_cities = {
#     "England":"London",
#     "Scotland" : "Edinburgh",
#     "Wales": "Cardiff",
#     "Northern Ireland" : "Belfast",
#     "Ireland": "Dublin"
# }
# print (capital_cities["England"])

# dict item's/key's value should be unique, if there are two same keys, the value of last one would be read (top down)

# Activity 1

animals = {"lion" : "cub",
           "dog" : "puppy",
           "cat" : "kitten",
           "duck" : "duckling"} 
print (animals["cat"])

print(animals.keys())
print(animals.values())
print(animals.items())

print(animals["dog"])  # could break code/ error if key not present in dict
print(animals.get("zebra", "That key does not exist!"))  # safer to use to get the value of key from dictionary
# setdefault method allows to add new key, value pair to dict; it wouldn't change an existing key if present- to protect dict data from changes
animals.setdefault("gecko", " baby gecko")
animals.setdefault("dog", "Baby dog")

print(animals)
