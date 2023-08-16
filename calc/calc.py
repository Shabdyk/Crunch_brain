import PySimpleGUI as sg
import src

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  
            [sg.Text('', key = 'line')],
            # [sg.InputText(key = 'line', default_text= '0')],
            [sg.Button('1', k = '1'), sg.Button('2'), sg.Button('3')],
            [sg.Button('4'), sg.Button('5'), sg.Button('6')],
            [sg.Button('7'), sg.Button('8'), sg.Button('9')],
            [sg.Button('+'), sg.Button('0'), sg.Button('.')],
            [sg.Button('-'), sg.Button('='), sg.Button('C')],
            [sg.Button('*'), sg.Button('/'), sg.Button('CE')] ]

# Create the Window
window = sg.Window('Calculator', layout, finalize=True)
# window['1'].bind("<Return>", "Enter")
# window['1'].bind('<1>', '')
line = [''] #init calc line

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read() 
    if event == sg.WIN_CLOSED: break #close when close

    if event == 'C': line = [''] #clear button

    elif event == 'CE':
        if line[-1] == '' and len(line) != 1: line.pop()
        line[-1] = ''


    elif event == '=':
        # list not in line

        stage_1 = src.plus_minus(line)
        stage_2 = src.mult_div(stage_1)

        eq = sum(stage_2)
        line = [str(eq)]
                

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
                if line[-1] == '':              #if there is already some operator, then there is ''
                    try:                        #this part removes that sign and a '' next to it
                        line.pop(-2)
                        line.pop(-1)
                    except IndexError: pass
                line.extend([event, ''])

    values['line'] = ''.join(line)              #sync line list with the line on the UI
    window['line'].update(values['line'])       #

    # print(values)
    print(line)

window.close()