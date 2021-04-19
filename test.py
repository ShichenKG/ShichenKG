import pygame as py
import PySimpleGUI as sg

def gui():
    sg.LOOK_AND_FEEL_TABLE['Test']= {'BACKGROUND': '#709053',
                    'TEXT': '#fff4c9',
                    'INPUT': '#c7e78b',
                    'TEXT_INPUT': '#000000',
                    'SCROLL': '#c7e78b',
                    'BUTTON': ('white', '#709053'),
                    'PROGRESS': ('#01826B', '#D0D0D0'),
                    'BORDER': 1,
                    'SLIDER_DEPTH': 0,
                    'PROGRESS_DEPTH': 0}
    sg.theme('Test')

    # Create the layout
    layout = [[sg.Text('Test Window', relief='groove', font=('Comic Sans MS', 18)),
               sg.Text('Powered by Jams Ramseys', font=('Comic Sans MS', 14))],
              [sg.MLine(size=(30, 5), key='-Message-', font=('Comic Sans MS', 14))],
              [sg.Button('Pretty Kool', key='-random-', font=('Comic Sans MS', 14)),
               sg.Button('Quit', font=('Comic Sans MS', 14))]]

    window = sg.Window('My Comical Window', layout,size=(1280, 720))
    while True:
        event, values = window.read()
        print(event, values)

        # Peak Comedy, an unclosable popup that is in a loop, can't ALT+F4 it
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            sg.popup('Are you sure you want to leave?', font=('Comic Sans MS', 14))
            break

        # An even that creates 2 funny popups, a loading bar, then PERISH(Took away the titlebar and the okay button, you can ALT+F4 it)
        elif event == '-random-':
            sg.popup_ok('That was Kool', font=('Comic Sans MS', 14))
            sg.popup_error('By all known laws of aviation a bee should not be able to fly',
                           text_color='yellow',
                           title='Bee movie',
                           font=('Comic Sans MS', 14))
        elif event == '--':
            pass

def pro():
    BAR_MAX = 100

    # layout the Window
    layout = [[sg.Text('A custom progress meter')],
              [sg.ProgressBar(BAR_MAX, orientation='h', size=(20, 20), key='-PROG-')],
              [sg.Cancel()]]

    # create the Window
    window = sg.Window('Custom Progress Meter', layout)
    # loop that would normally do something useful
    for i in range(1000):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = window.read(timeout=10)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
            # update bar with loop value +1 so that bar eventually reaches the maximum
        window['-PROG-'].update(i + 1)

def game():
    pass


def guigame():
    pass


gui()