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
window = sg.Window('Calculator', layout)
line = [''] #init calc line

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read() 
    if event == sg.WIN_CLOSED: break #close when close

    if event == 'C': line = ['0'] #clear button
    else:
        try:
            int(event)                                          #try to make the clicked button be integer
            if event == '0' and line[-1] == '': line[-1] = '0.' #clicking '0' in the beggining makes '0.'
            else: line[-1] += event                             #place the digit to the line
        except ValueError:                                      #button is not a digit
            if event == '.' and '.' not in line[-1]:            #don't add '.' 
                if line[-1] == '': line[-1] = '0.'  
                else: line[-1] += event                         #if it doesn't exist, place it
            elif event == '.' and '.' in line[-1]: pass         #if it exists, pass
            
            else: 
                if line[-1] == '':
                    try:
                        line.pop(-2)
                        line.pop(-1)
                    except IndexError: pass
                line.extend([event, ''])

    values['line'] = ''.join(line)
    window['line'].update(values['line'])

    print(values)
    print(line)

window.close()