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
            [sg.Button('-'), sg.Button('='), sg.Button('C')],
            [sg.Button('*'), sg.Button('\\'), sg.Button('CE')] ]

# Create the Window
window = sg.Window('Calculator', layout)
line = [''] #init calc line

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read() 
    if event == sg.WIN_CLOSED: break #close when close

    if event == 'C': line = [''] #clear button

    elif event == '=':

        # multiplication

        for i in range(0, len(line)):
            # i = line.index(i)
            if line[i] == '*':
                eq = float(line[i-1]) * float(line[i+1])
                line[i-1] = str(eq)
                line[i+1] = '0'
                line.pop(i)
        
        # addition and substraction
        end = 0
        while len(line) != 1:
            end += 1
            # print('AAA')
            if line[1] == '+': #addition
                eq = float(line[0]) + float(line[2])
                line[1] = str(eq)
                line.pop(2)
                line.pop(0)
            elif line[1] == '-': #substraction
                eq = float(line[0]) - float(line[2])
                line[1] = str(eq)
                line.pop(2)
                line.pop(0)
            elif end == 20:
                print("END")
                break
            # try:
            #     line.remove('0') 
            #     print('0 clear: ')
            #     print(line)
            # except ValueError:
            #     break
                

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