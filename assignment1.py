# Data structures in python
#
# Topic :List
# Exercise
# Q1. Create a list of 5 random numbers and print the list.
random_list = [10, 12, 34, 45, 22]
print(random_list)

# Q2. Insert 3 new values to the list and print the updated list.

random_list.append(60)
random_list.insert(6, 70)
random_list.insert(7, 80)
print(random_list)
# Q3. Try to use a for loop to print each element in the list.
random_list = [10, 12, 34, 45, 22]
for num in random_list:
    print(num)
# Topic: Dictionary
# Exercise
# Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.
my_dict = {'name': 'John', 'age': 25, 'address': 'New York'}
print(my_dict)
# Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.

my_dict['phone'] = 1234567890
print(my_dict)
#
# Topic: Set
# Exercise
# Q1.Create a set with values 1, 2, 3, 4, and 5.
my_set = {1, 2, 3, 4, 5}
# Q2. Add the value 6 to the set created in Q1.
my_set.add(6)
# Q3. Remove the value 3 from the set created in Q1.
my_set.remove(3)
print(my_set)

# Topic:Tuple
# Exercise
# Q1. Create a tuple with values 1, 2, 3, and 4
my_tuple = (1, 2, 3, 4)

# Q2. Print the length of the tuple created in Q1.
print(len(my_tuple))
