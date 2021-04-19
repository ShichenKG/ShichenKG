######################################
# Opening Comments
# Author Shane Donivan
# 12/15/20
# Collection Window
# This window compiles Yu-Gi-Oh Cards
#######################################
import PySimpleGUI as sg

# My custom Themes for the cards
sg.LOOK_AND_FEEL_TABLE['Normal'] = {'BACKGROUND': '#8a5c3a',
                                        'TEXT': 'black',
                                        'INPUT': '#bf986f',
                                        'TEXT_INPUT': '#000000',
                                        'SCROLL': '#c7e78b',
                                        'BUTTON': ('black', '#c47f23'),
                                        'PROGRESS': ('#01826B', '#127025'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        }
sg.LOOK_AND_FEEL_TABLE['Fusion'] = {'BACKGROUND': '#41165e',
                                        'TEXT': 'black',
                                        'INPUT': '#7a5e8c',
                                        'TEXT_INPUT': '#000000',
                                        'SCROLL': '#c7e78b',
                                        'BUTTON': ('black', '#8817d1'),
                                        'PROGRESS': ('#01826B', '#127025'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        }
sg.LOOK_AND_FEEL_TABLE['Synchro'] = {'BACKGROUND': '#a6a6a6',
                                        'TEXT': 'black',
                                        'INPUT': '#d4d4d4',
                                        'TEXT_INPUT': '#000000',
                                        'SCROLL': '#c7e78b',
                                        'BUTTON': ('black', '#fafafa'),
                                        'PROGRESS': ('#01826B', '#127025'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        }

# Takes you to 4 different window's based on Card Types
def cardtype():
    sg.theme('Dark')
    L2 = [[sg.Text('CardType',font=('Comic Sans MS',20),justification='center',size=(100,1))],
          [sg.Button('Normal',enable_events=True,key='-Normal-',font=('Comic Sans MS',16)), sg.Button('Fusion',enable_events=True,key='Fusion',font=('Comic Sans MS',16))],
          [sg.Button('Synchro',enable_events=True,key='-Synchro-',font=('Comic Sans MS',16)), sg.Button('XYZ',enable_events=True,key='-XYZ-',font=('Comic Sans MS',16))]]

    ctype = sg.Window('Card Type', L2, size=(200, 180),font=('Comic Sans MS',14))
    while True:
        event, values = ctype.read()
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        elif event == '-Normal-':
            normaltype()
        elif event == 'Fusion':
            fusiontype()
        elif event == '-Synchro-':
            synchrotype()
        elif event == '-XYZ-':
            xyztype()

# Chooses it's Effect because Yu-Gi-Oh Cards of Normal by default
def normaltype():
    sg.theme('Normal')
    NL3 = [[sg.Text('Normal Effect Type',font=('Comic Sans MS',18),justification='center',size=(100,1))],
          [sg.Button('Non-Effect',enable_events=True,key='-NonEffect-',font=('Comic Sans MS',14)), sg.Button('Effect',enable_events=True,key='-Effect-',font=('Comic Sans MS',14)),
           sg.Button('Flip',enable_events=True,key='-Flip-',font=('Comic Sans MS',14))],
          [sg.Button('Toon',enable_events=True,key='-Toon-',font=('Comic Sans MS',14)), sg.Button('Spirit',enable_events=True,key='-Spirit-',font=('Comic Sans MS',14)),
           sg.Button('Gemini',enable_events=True,key='-Gemini-',font=('Comic Sans MS',14))],
           [sg.Button('Effect-Tuner',enable_events=True,key='-EffectTuner-',font=('Comic Sans MS',14))]]

    ntype = sg.Window('Normal Effect Type', NL3, size=(300, 200))
    while True:
        event, values = ntype.read()
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        elif event == '-NonEffect-':
            Effect = 'Non-Effect'
            Type = ''
            Tuner = ''
            window['-Effect-'].update(Effect)
            window['-Type-'].update(Type)
            window['-Tuner-'].update(Tuner)

        elif event == '-Effect-':
            Effect = 'Effect'
            Type = ''
            Tuner = ''
            window['-Effect-'].update(Effect)
            window['-Type-'].update(Type)
            window['-Tuner-'].update(Tuner)

        elif event == '-Flip-':
            Effect = 'Flip'
            Type = ''
            Tuner = ''
            window['-Effect-'].update(Effect)
            window['-Type-'].update(Type)
            window['-Tuner-'].update(Tuner)

        elif event == '-Toon-':
            Effect = 'Toon'
            Type = ''
            Tuner = ''
            window['-Effect-'].update(Effect)
            window['-Type-'].update(Type)
            window['-Tuner-'].update(Tuner)

        elif event == '-Spirit-':
            Effect = 'Spirit'
            Type = ''
            Tuner = ''
            window['-Effect-'].update(Effect)
            window['-Type-'].update(Type)
            window['-Tuner-'].update(Tuner)

        elif event == '-Gemini-':
            Effect = 'Gemini'
            Type = ''
            Tuner = ''
            window['-Type-'].update(Type)
            window['-Effect-'].update(Effect)
            window['-Tuner-'].update(Tuner)

        elif event == '-EffectTuner-':
            Effect = 'Effect'
            Tuner = 'Tuner'
            Type = ''
            window['-Effect-'].update(Effect)
            window['-Type-'].update(Tuner)
            window['-Tuner-'].update(Type)

# Adds Fusion Type, and Effect Type
def fusiontype():
    sg.theme('Fusion')
    FL3 = [[sg.Text('Fusion Effect Type',font=('Comic Sans MS',18),justification='center',size=(100,1))],
          [sg.Button('Non-Effect',enable_events=True,key='-NonEffect-',font=('Comic Sans MS',14)), sg.Button('Effect',enable_events=True,key='-Effect-',font=('Comic Sans MS',14)),
           sg.Button('Tuner',enable_events=True,key='-Tuner-',font=('Comic Sans MS',14))]]

    ftype = sg.Window('Fusion Effect Type', FL3, size=(310, 100))
    while True:
        event, values = ftype.read()
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        elif event == '-NonEffect-':
            Effect = 'Non-Effect'
            Tuner = ''
            global Type
            Type = 'Fusion'
            window['-Effect-'].update(Effect)
            window['-Tuner-'].update(Tuner)
            window['-Type-'].update(Type)
            return Type

        elif event == '-Effect-':
            Effect = 'Effect'
            Tuner = ''
            window['-Effect-'].update(Effect)
            window['-Tuner-'].update(Tuner)
            window['-Type-'].update(Type)

        elif event == '-Tuner-':
            Tuner = 'Tuner'
            Effect = 'Effect'
            Type = 'Fusion'
            window['-Tuner-'].update(Tuner)
            window['-Type-'].update(Type)
            window['-Effect-'].update(Effect)

# Adds Synchro Type and Effect Type
def synchrotype():
    sg.theme('Synchro')
    SL3 = [[sg.Text('Synchro Effect Type',font=('Comic Sans MS',18),justification='center',size=(100,1))],
          [sg.Button('Non-Effect',enable_events=True,key='-NonEffect-',font=('Comic Sans MS',14)), sg.Button('Effect',enable_events=True,key='-Effect-',font=('Comic Sans MS',14)),
           sg.Button('Effect-Tuner',enable_events=True,key='-EffectTuner-',font=('Comic Sans MS',14))]]

    stype = sg.Window('Synchro Effect Type', SL3, size=(380, 100))
    while True:
        event, values = stype.read()
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        elif event == '-NonEffect-':
            Effect = 'Non-Effect'
            Type = 'Synchro'
            Tuner = ''
            window['-Effect-'].update(Effect)
            window['-Type-'].update(Type)
            window['-Tuner-'].update(Tuner)

        elif event == '-Effect-':
            Effect = 'Effect'
            Type = 'Synchro'
            Tuner = ''
            window['-Effect-'].update(Effect)
            window['-Type-'].update(Type)
            window['-Tuner-'].update(Tuner)

        elif event == '-EffectTuner-':
            Effect = 'Effect'
            Tuner = 'Tuner'
            Type = 'Synchro'
            window['-Effect-'].update(Effect)
            window['-Type-'].update(Type)
            window['-Tuner-'].update(Tuner)

# Adds XYZ Type and Effect Type
def xyztype():
    sg.theme('DarkAmber')
    XYZL3 = [[sg.Text('XYZ Effect Type',font=('Comic Sans MS',20),justification='center',size=(100,1))],
          [sg.Button('Non-Effect',enable_events=True,key='-NonEffect-',font=('Comic Sans MS',16)), sg.Button('Effect',enable_events=True,key='-Effect-',font=('Comic Sans MS',16))]]

    xyztype = sg.Window('Fusion Effect Type', XYZL3, size=(260, 100),font=('Comic Sans MS',14))
    while True:
        event, values = xyztype.read()
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        elif event == '-NonEffect-':
            Effect = 'Non-Effect'
            Type = 'XYZ'
            Tuner = ''
            window['-Effect-'].update(Effect)
            window['-Type-'].update(Type)
            window['-Tuner-'].update(Tuner)
        elif event == '-Effect-':
            Effect = 'Effect'
            Type = 'XYZ'
            Tuner = ''
            window['-Effect-'].update(Effect)
            window['-Type-'].update(Type)
            window['-Tuner-'].update(Tuner)

#
global Effect
Effect = ''
global Type
Type = ''
global Species
Species = ''

# Variables and Functions for the Add/Subtract ATK and DEF Buttons
ATK = 0
DEF = 0

def add100ATK():
    global ATK
    ATK += 100
def sub100ATK():
    global ATK
    ATK -= 100
def add100DEF():
    global DEF
    DEF += 100
def sub100DEF():
    global DEF
    DEF -= 100

# Variables for dropdown menus
element = ['Dark', 'Divine', 'Earth', 'Fire', 'Light', 'Water', 'Wind']
species = ['Aqua', 'Beast', 'Beast Warrior', 'Dinosaur', 'Divine Beast', 'Dragon', 'Fairy', 'Friend', 'Fish', 'Zombie', 'Machine',
           'Plant', 'Psychic', 'Pyro', 'Reptile', 'Rock', 'Thunder', 'Sea Serpant', 'Warrior', 'Winged Beast']
stars = [1,2,3,4,5,6,7,8,9,10,11,12]

sg.theme('Normal')

#Create the layout for the Main window
L1 = [[sg.Image(r'.\Title.png')],
      [sg.Text('Card Name:',font=('Comic Sans MS',15)), sg.Input('',font=('Comic Sans MS',13),size=(30,1)), sg.Text('Element: ',font=('Comic Sans MS',14)), sg.DropDown(element,readonly=True,font=('Comic Sans MS',14))],
      [sg.Text('Number of',font=('Comic Sans MS',14)), sg.Image('.\Level.png'), sg.DropDown(stars, size=(5,1),font=('Comic Sans MS',14))],
      [sg.Text('Species:',font=('Comic Sans MS',14)), sg.Combo(species,default_value='None',enable_events=True,key='-DSpecies-',font=('Comic Sans MS',14))],
      [sg.Text('Monster Type:',font=('Comic Sans MS',14)), sg.Button('Type/Effect',enable_events=True,key='-CType-',font=('Comic Sans MS',14))],
      [sg.Input('',enable_events=True,key='-Species-',size=(13,1),font=('Comic Sans MS',13)),
       sg.Text('/',font=('Comic Sans MS',15)),sg.Input('',enable_events=True,key='-Effect-',size=(13,1),font=('Comic Sans MS',13)),
       sg.Text('/',font=('Comic Sans MS',15)),sg.Input('',enable_events=True,key='-Type-',size=(13,1),font=('Comic Sans MS',13)),
       sg.Text('/',font=('Comic Sans MS',15)),sg.Input('',enable_events=True,key='-Tuner-',size=(13,1),font=('Comic Sans MS',13))],
      [sg.Text('ATK',font=('Comic Sans MS',14)), sg.Input('0',size=(15,1),enable_events=True,key='-ATKBox-',font=('Comic Sans MS',13)),
       sg.Button('+100',enable_events=True,key='-addATK-',font=('Comic Sans MS',13)), sg.Button('-100',enable_events=True,key='-subATK-',font=('Comic Sans MS',13)),
       sg.Text('DEF',font=('Comic Sans MS',14)), sg.Input('0',size=(15,1),enable_events=True,key='-DEFBox-',font=('Comic Sans MS',13)),
       sg.Button('+100',enable_events=True,key='-addDEF-',font=('Comic Sans MS',13)), sg.Button('-100',enable_events=True,key='-subDEF-',font=('Comic Sans MS',13))],
      [sg.Button('Save',enable_events=True,key='-Save-',font=('Comic Sans MS',14)), sg.Button('Quit',font=('Comic Sans MS',14))]]

# Create the instance of a window
window = sg.Window('Yu-Gi-Oh',L1, size=(700,400))

# Start the while loops for Events
while True:
    event, values = window.read()
    print(event,values)
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        sg.popup_yes_no('Are you Sure you want to quit without Saving?', font=('Comic Sans MS',14))
        break

    elif event == '-CType-':
        cardtype()

    elif event == '-addATK-':
        add100ATK()
        window['-ATKBox-'].update(ATK)

    elif event == '-subATK-':
        sub100ATK()
        window['-ATKBox-'].update(ATK)

    elif event == '-addDEF-':
        add100DEF()
        window['-DEFBox-'].update(DEF)

    elif event == '-subDEF-':
        sub100DEF()
        window['-DEFBox-'].update(DEF)

    elif event == '-DSpecies-':
        window['-Species-'].update(values['-DSpecies-'])

    elif event == '-Save-':
        sg.popup('Saved!', font=('Comic Sans MS',14))

    else:
        print(event,values)