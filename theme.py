from qt_material import apply_stylesheet




def theme_toggle(app):
    
    with open('theme.save', 'r') as f:
        # Comment: 
        number =  f.readline()
        number = int(number)
        number %= 18
        number += 1
        
    with open('theme.save', 'w') as f:
        f.write(str(number))
    # end readline file
    theme(app)


def theme(app):
    '''reads previously set theme number and sets according to it'''
    try:
        with open('theme.save', 'r') as f:
            # Comment: 
            number =  f.readline()
            number = int(number)
        # end readline file
    
    except FileNotFoundError:
        with open('theme.save', 'x') as f:
            # Comment: 
            f.write('1')
            number = 1
        # end readline file

    list = ['dark_amber.xml',
            'dark_blue.xml',
            'dark_cyan.xml',
            'dark_lightgreen.xml',
            'dark_pink.xml',
            'dark_purple.xml',
            'dark_red.xml',
            'dark_teal.xml',
            'dark_yellow.xml',
            'light_amber.xml',
            'light_blue.xml',
            'light_cyan.xml',
            'light_cyan_500.xml',
            'light_lightgreen.xml',
            'light_pink.xml',
            'light_purple.xml',
            'light_red.xml',
            'light_teal.xml',
            'light_yellow.xml']
    apply_stylesheet(app, theme=f'{list[number%18]}')
