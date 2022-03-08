def double(number):
  print(number * 2)

double(5)

#instead of printing you can rturn

def double2(number):
  return number * 2

double2(5) #still doesnt reutn but it  is an int

new_number = double2(5)

print(new_number)

#create a function that returns a string in all caps

def all_caps(mixed_case_word):
  return (mixed_case_word).upper()

fixed_case = all_caps('Bob')

print(fixed_case)

names = ['oliver', 'joey', 'Jesse']

for list in names:
  print(all_caps(list))