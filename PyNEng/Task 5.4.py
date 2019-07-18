# Задание 5.4

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

num = int(input('Enter number and give an index: '))
last_num_index = len(num_list) - 1 - num_list[::-1].index(num)
print(last_num_index)

word = input('Enter word and give an index: ')
last_word_index = len(word_list) - 1 - word_list[::-1].index(word)
print(last_word_index)