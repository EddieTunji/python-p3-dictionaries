def pour_coffee(size):
    size_to_ounce_map = {
        "tall": 12,
        "grande": 16,
        "venti": 20,
    }
    return size_to_ounce_map.get(size, "Please enter a valid cup size.")
print(pour_coffee("jumbo"))
print(pour_coffee("tall"))
pour_coffee("grande")

my_dict = {
    'key_one': 'value_one',
    'key_two': 'value_two',
}

my_dict['key_one'] = 'I have changed!'

my_dict['key_three'] = 'value_three'

print(my_dict)

my_dict.update({'key_three': 'watchumeen', 'key_four': 'irronknoww'})
print(my_dict)

my_dict = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
}
[item for item in my_dict.items()]

[key for key, value in my_dict.items()]

[value for key, value in my_dict.items()]