import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  
            [sg.Text('', key = 'line')],
            # [sg.InputText(key = 'line', default_text= '0')],
            [sg.Button('1'), sg.Button('2'), sg.Button('3')],
            [sg.Button('4'), sg.Button('5'), sg.Button('6')],
            [sg.Button('7'), sg.Button('8'), sg.Button('9')],
            [sg.Button('+'), sg.Button('0'), sg.Button('.')],
            [sg.Button('-'), sg.Button('C'), sg.Button('=')] ]

# Create the Window
window = sg.Window('Window Title', layout)
line = ['']

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: break

    if event == 'C': line = ['0']
    else:
        try:
            int(event)
            if event == '0' and line[-1] == '': line[-1] = '0.'
            else: line[-1] += event
        except ValueError:
            if event == '.' and '.' not in line[-1]: 
                if line[-1] == '': line[-1] = '0.'
                else: line[-1] += event
            elif event == '.' and '.' in line[-1]: pass
            
            else: line.extend([event, ''])
            
    values['line'] = ''.join(line)
    window['line'].update(values['line'])

    print(values)
    print(line)

window.close()