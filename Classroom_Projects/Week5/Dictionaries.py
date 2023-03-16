my_dictionary = {"John": "0412312314", "Sara": "0421321332", "Joe": "0402948472"}

keys = my_dictionary.keys()
print("Keys> ", keys)

values = my_dictionary.values()
print("Values> ", values)

items = my_dictionary.items()
print("Items> ", items)

key_one = my_dictionary["John"]
print(key_one)

my_dictionary["Joe"] = "0438495584"
print(my_dictionary)

for one_key, one_value in my_dictionary.items():
    print(one_key, one_value)

