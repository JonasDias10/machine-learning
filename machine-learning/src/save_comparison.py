import os

def save_algorithms_comparison(file_path1, file_path2, file_path3):
    file1_data = read_file(file_path1)
    file2_data = read_file(file_path2)
    file3_data = read_file(file_path3)

    file1_column = format_data(file1_data)
    file2_column = format_data(file2_data)
    file3_column = format_data(file3_data)

    write_to_file('outputs/algorithms_comparison.txt', file1_column, file2_column, file3_column)

    delete_algorithms_results(file_path1, file_path2, file_path3)

def delete_algorithms_results(file_path1, file_path2, file_path3):
    delete_file(file_path1)
    delete_file(file_path2)
    delete_file(file_path3)

def delete_file(file_path):
    if os.path.exists('outputs/' + file_path):
        os.remove('outputs/' + file_path)

def read_file(file_path):
    with open('outputs/' + file_path, 'r') as file:
        return file.readlines()

def format_data(data):
    return [line.strip() for line in data]


def write_to_file(output_file, column1, column2, column3):
    with open(output_file, 'w') as file:
        for data1, data2, data3 in zip(column1, column2, column3):
            formatted_line = f"{data1.ljust(20)} | {data2.ljust(20)} | {data3.ljust(20)}\n"
            file.write(formatted_line)