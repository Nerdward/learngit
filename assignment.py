import csv

print('-'.ljust(20, '-'))
print('Welcome To Phone_book v1.0')
print('-'.ljust(20, '-'))
print('Menu  :')
print('1.  Add')
print('2.  Lookup')
print('3.  Update Phone Number')
print('4.  Delete')
print('5.  Exit \n')
file = 'phonebook.csv'

while True:
    val = int(input('Enter your selection : '))
    if val == 1:
        with open(file, 'a') as file_app:
            csv_write = csv.writer(file_app)
            new_row = list(input('Input new phone details:'))
            csv_write.writerow(new_row)

    elif val == 2:
        with open(file, 'r') as file_read:
            csv_read = csv.reader(file_read)
            for row in csv_read:
                print(row)

    elif val == 3:
        print(row[2])

    elif val == 4:
        del csv_write

    elif val == 5:
        break
