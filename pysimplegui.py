######################################
# Opening Comments
# Author Robert Ball
# Edited by Shane Donivan
# 11/16/20
# My First Window
#######################################
import PySimpleGUI as sg


sg.theme('Dark')
#This variable is for the unclosable popup loop
C = 0

#Create the layout
layout = [[sg.Text('MyComicalWindow',relief='groove',font=('Comic Sans MS',18)),sg.Text('Powered by Jams Ramseys',font=('Comic Sans MS',14))],
          [sg.MLine(size=(30,5),key='-Message-',font=('Comic Sans MS',14))],
          [sg.Button('Pretty Kool', key='-random-', font=('Comic Sans MS',14)),
           sg.Button('Show Message', key='-show-', font=('Comic Sans MS',14)),
           sg.Button('Quit', font=('Comic Sans MS',14))],
          [sg.Image(r'C:\Python\bee.png')],
          [sg.Text('Which Enterprise captain is better?',font=('Comic Sans MS',14))],
          [sg.Combo(['Jonathan Archer','Christopher Pike','James T. Kirk','Jean-Luc Picard'], size=(30,30))]]

# Create the instance of a window
window = sg.Window('My Comical Window',layout,grab_anywhere=True,disable_close=True,disable_minimize=True,no_titlebar=True)

#start the while loop
while True:
    event, values = window.read()
    print(event,values)

#Peak Comedy, an unclosable popup that is in a loop, can't ALT+F4 it
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        sg.popup('Are you sure you want to leave?',font=('Comic Sans MS',14))
        while C < 1:
            sg.popup_annoying('Are you really sure?',font=('Comic Sans MS',14),keep_on_top=True)
            
#An even that creates 2 funny popups, a loading bar, then PERISH(Took away the titlebar and the okay button, you can ALT+F4 it)
    elif event == '-random-':
        sg.popup_ok('That was Kool',font=('Comic Sans MS',14))
        sg.popup_error('By all known laws of aviation a bee should not be able to fly',
                       text_color='yellow',
                       title='Bee movie',
                       font=('Comic Sans MS',14))
        for i in range(1,10000):
            sg.one_line_progress_meter('My Meter', i+1, 10000, 'key','LMAO')
        sg.popup_annoying('Perish', button_type=5, text_color='red', font=('Comic Sans MS',26,'bold'))

#Shows what you typed
    elif event == '-show-':
        TypedText = values['-Message-']
        sg.popup_scrolled(TypedText,title="What you typed",font=('Comic Sans MS',14))
    else:
        print(event,values)

