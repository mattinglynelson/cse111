import csv
from fileinput import filename
def main():
    i_number = (input('Enter a Students I-number: '))
    first_name_index = 1
    id_index = 0
    student_id_dict = read_dict('Programming With Functions (CSE 111)\Assignments\students.csv', id_index)


    

    if i_number in student_id_dict:
        value = student_id_dict[i_number]
        name = value[first_name_index]
        id = value[id_index]

        print(f'{name} is their name, their inumber is {id}' )
    else:
        print('no such student found')




def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    """  
    dictionary = {}  

    with open(filename, 'rt') as csv_file:
    
        reader = csv.reader(csv_file)

        next(reader)

        for rows in reader:
            key = rows[key_column_index]
            dictionary[key] = rows
            

    return dictionary




        # id = read_list(filename, key_column_index)
    """Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    
main()