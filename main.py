# задание 1
def reverse_text(input_text):
     reversed_text = ""
     for char in input_text:
         reversed_text = char + reversed_text
     return reversed_text

text_input = input("Введите строку: ")
reversed_input = reverse_text(text_input)
print("Строка в обратном порядке:", reversed_input)
import itertools

# задание 2
def replace_h_H(input_text):
     count = 0
     for i in range(len(input_text)):
         if input_text[i] == 'h':
             count += 1
     new_text = input_text.replace('h', 'H', count - 1).replace('H', 'h', 1)
     return new_text

text_input2 = input("Введите строку: ")
print("Измененная строка:", replace_h_H(text_input2))

# задание 3
def words_count(input_text):
     return len(input_text.split())

text_input3 = input("Введите строку: ")
print("Количество слов в строке:", words_count(text_input3))

# задание 4
import re

def words_count_without_split(input_text):
     return len(re.findall(r'\w+', input_text))

text_input4 = input("Введите строку: ")
print("Количество слов в строке:", words_count_without_split(text_input4))

# задание 5
def replace_words(input_text):
     first_word = input_text[:input_text.find(' ')]
     second_word = input_text[input_text.find(' ') + 1:]
     return second_word + ' ' + first_word

text_input5 = input("Введите строку из 2 слов: ")
print("Перемещение слов местами:", replace_words(text_input5))

# задание 6
def update_full_name(input_text):
       arr = input_text.split()
       surname = arr[0]
       name = arr[1]
       patronymic = arr[2]
       return surname + ' ' + name[0] + '. ' + patronymic[0] + '.'

text_input6 = input("Введите ФИО:")
print("Сокращенное ФИО:", update_full_name(text_input6))

# задание 7
matryoshka = [5, [5.65, [5+15j, [[], 15, "Иголка"]]]]
print(matryoshka[1][1][1][2])

# задание 8
# 1 способ
list1 = ['собака', 'кошка', 'хомяк']
list2 = ['55', '66', '77']
mixed_list1 = list1 + list2
print(mixed_list1)
# 2 способ
list3 = ['55', '66', '77']
list4 = ['собака', 'кошка', 'хомяк']
mixed_list2 = list3.extend(list4)
print(mixed_list2)

# задание 9
list5 = [10, 1, 5, 6]
list6 = [12, 15, 5, 7]

mixed_list3 = list5 + list6
sorted_list = sorted(mixed_list3)
no_repetitions_list = list(set(sorted_list))

print(no_repetitions_list)

# задание 10
def check_unique_list(list):
     if len(list) == len(set(list)):
         return True
     else:
         return False

list7 = [3, 1, 5, 3, 2]
is_unique_list = check_unique_list(list7)
print(is_unique_list)

# задание 11
date_dict = {'year': 2024, 'month': 4, 'day': 14}
expression_date = f"{date_dict['year']}-{date_dict['month']}-{date_dict['day']}"
print(expression_date)

# задание 12
text_input7 = input("Введите числа, разделенные запятой:")
numbers_list = text_input7.split(',')
numbers_tuple = tuple(numbers_list)

print("Список чисел:", numbers_list)
print("Кортеж чисел:", numbers_tuple)

# задание 13
students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}

# все люди
all_people1 = students.union(employees)
all_people2 = result = {*students, *employees}
print('Все люди 1:', all_people1)
print('Все люди 2:', all_people2)

# и учатся, и работают
matching_people1 = students & employees
matching_people2 = students.intersection(employees)
print('И учатсся, и работают 1:', matching_people1)
print('И учатсся, и работают 2:', matching_people2)

# только работают, но не учатся
workers1 = employees - students
workers2 = employees.difference(students)
print('Только работают, но не учатся 1:', workers1)
print('Только работают, но не учатся 2:', workers2)

#либо учатся, либо работают, но не одновременно
unique_people1 = students ^ employees
unique_people2 = students.symmetric_difference(employees)
print('Либо учатся, либо работают, но не одновременно 1:', unique_people1)
print('Либо учатся, либо работают, но не одновременно 2:', unique_people2)

# задание 14
array = [
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55]
]
transposed_array = [[row[i] for row in array] for i in range(len(array[0]))]
for row in transposed_array:
     print(row)

# задание 15
for r in range(5):
     print("X" + "x" * (2*r) + "X")