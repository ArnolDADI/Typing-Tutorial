 
import os

def check(name):
    try:
        with open(name, 'r') as f:
            # Comment: 
            f.readline()
        # end readline file
    except FileNotFoundError:
        try:
            with open(name, 'x') as f:
                # Comment: 
                f.write('')
            # end readline file
        except FileExistsError:
            with open(list_name[1], 'x') as f:
                # Comment: 
                f.write('')
        except FileNotFoundError:
            list_name = list(name.split('/'))
            os.mkdir(list_name[0])
            with open(list_name[1], 'x') as f:
                # Comment: 
                f.write('')
            # end open file
        # end open file


def CheckFiles():

    list = ['courses/course1','courses/course2','courses/course3','courses/course4','courses/course5','courses/course6', 'profiles/profile_list', 'profiles/last_profile']

    for i in list:
        check(i)

    with open('profiles/profile_list', 'r') as f:
            # Comment: 
            list_profile_names = f.readline()
        # end readline file

    for i in list_profile_names:
        check(f'profiles/{i}')
