import re


def remove_brackets(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_path, 'w', encoding='utf-8') as file:
        for line in lines:
            space_index = line.find(' ')
            if space_index != -1:
                new_line = line[:space_index + 1] + ' '
            else:
                new_line = line
            file.write(new_line + '\n')

input_file = '/Users/lucifior/Downloads/CET4_edited.txt'
output_file = '/Users/lucifior/Documents/CET4_edited01.txt'

remove_brackets(input_file, output_file)