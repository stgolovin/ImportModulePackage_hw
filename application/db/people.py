from datetime import date

list_of_empolyees = list()
list_of_empolyees.append('Lera Philyushina')
list_of_empolyees.append('Lena Timofeeva')


def get_employees():
    print('Here is your employees: {}'.format(list_of_empolyees))
    print('Currnet date: {}'.format(date.today()))
