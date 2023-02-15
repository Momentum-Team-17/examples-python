def greet(names):
    '''this is a
    multi-line comment'''
    for name in names:
        # for of loop
        print(f'Hi, {name}!')
        # console.log, like a template literal


our_names = ['Michael',
             'Candace',
             'Daniel',
             'Emmaline',
             'Chris',
             'Christina',
             "Gerardo 'The Rock' Roman"]
# it's a list

other_names = ['A', 'B', 'C']

# greet(our_names)
# greet(other_names)


def greet_in_spanish():
    name = input("¿Como te llamas? ")
    print("¡Hola, " + name + "!")


# greet_in_spanish()

animals = ['zebra', 'pika', 'octopus', 'black bear']
print(animals.count('zebra'))
# print(animals[3])
# print(len(['apples', 'peaches', 'pumpkin pie', 'pecans']))

dinosaurs = ('brachiosaur', 'pterodactyl', 't-rex')
# tuples are similar to lists, but they are in ()
print(dinosaurs.index('t-rex'))
# we can do index() and count() but not pop(), push(), or remove()
(first_dinosaur, second_dinosaur, third_dinosaur) = (
    'brachiosaur', 'pterodactyl', 't-rex')
# unpacking assigns multiple variables at once, based on position in the tuple
print(first_dinosaur)
print(second_dinosaur)
print(third_dinosaur)

first_dinosaur = dinosaurs[0]
second_dinosaur = dinosaurs[1]
third_dinosaur = dinosaurs[2]
# this is long way of what we did in one line in 41/42
(a, b, c) = (1, 2, 3)
# annoyingly, also ok to write
# a, b, c = 1, 2, 3
# because of the above line, the variables a, b, and c have the following values
# a -> 1
# b -> 2
# c ->  3
d = 4
e = 5
f = 6
new_tuple = (d, e, f)
print(new_tuple)
# can put variables in a tuple *if* they have been defined
d = 7
print(new_tuple)

new_list = [d, e, f]
print(new_list)

f = 10
print(new_list)
new_list[2] = 10
# can change values in a list, can't do that with a tuple
print(new_list)
new_list[0] = e
print(new_list)
print(new_list[0])
print(type(new_list[0]))

dinosaur_list = ['brachiosaur', 'pterodactyl', 't-rex']

# print(type(dinosaur_list[0]))
# dinosaur_list[0] = 'brontosaurus'
# print(dinosaur_list)
# dinosaur_list[0] = False
# print(dinosaur_list)
milk = None
fruit = None
bev = None
# observe that we are out of these items

shopping_list = ('milk', 'fruit', 'bev')
# make a shopping list

milk = 'whole milk'
fruit = 'oranges'
bev = 'coke'
# purchase specific items and put them in the fridge

fridge_items = [milk, fruit, bev]
# fridge_items is what is actually in the fridge
print(fridge_items)


def sort_list(list):
    sorted_list = sorted(our_names, key=sort_key)
    return sorted_list


def sort_key(word):
    return word[1]


# dictionaries have key-value pairs like objects in JS
pink_slip = {
    'bass': "Emmaline",
    'vocals': "Ruby",
    'guitar': "Jasmine",
    'drums': "Frankie",
    # ok to put a comma after the last value
}
print("Dictionary stuff starts here:")
# print(f"{pink_slip['bass']} plays bass in Pink Slip")
# print(f"{pink_slip['vocals']} is the lead singer of in Pink Slip")


# to add a key, value pair to a dictionary
pink_slip['rhythm guitar'] = 'Michael'

pink_slip['rhythm guitar'] = 'Kelly'
# to update the value, use the name of the dict and the name of the key

# if we wanted to add to the existing value, rather than replace
# we can use +=
pink_slip['rhythm guitar'] += ' & Michael'
# I am concatenating the strings into one big string containing
# 'Kelly & Michael'


# if I wanted the values to be collections with multiple names,
# I would have to make the values into lists
pink_slip = {
    'bass': ["Emmaline"],
    'vocals': ["Ruby"],
    'guitar': ["Jasmine"],
    'drums': ["Frankie"],
    'rhythm guitar': ["Kelly"]
    # ok to put a comma after the last value
}

# then to add to a value, I would use
pink_slip['rhythm guitar'].append('Michael')

# for instrument, person in pink_slip.items():
#     print(f'{person} plays {instrument} in Pink Slip')

# print(pink_slip['banjo'])
# if you use [] to look up a key that does not exist in a dict,
# you get a KeyError

# print(pink_slip.get('banjo'))
# if you use dict.get('key'), you won't get an error, and will get the value None if the key doesn't exist

# .items() gives us the key, value pairs as tuples, which you can unpack
for key, value in pink_slip.items():
    print(key, value)

# if you don't use .items(), you get the keys
# for key in pink_slip:
#     print(key)

# you can also use .keys() or .values() if you want only the keys or values, respectively
# for value in pink_slip.values():
#     print(value)
