from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('DarkGreen1')
layout  = [ 
    [sg.Text('Usuário'), sg.Input(key='usuario',size=(20,1))],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*',size=(25,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')],
    [sg.Text(key=('Obrigado!'),size=(40,1))]
]
# Janela
janela = sg.Window('Login', layout)
# Ler os Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Walker25' and valores['senha'] == 'MinduinSalgado':
            print('Seja Bem-vindo!')
        elif valores['usuario'] != 'Edgar':
            print('Usuário incorreto!')
        elif valores['senha'] != '270722':
             print('Senha incorreta!')
        janela['Obrigado!'].update('Olá ' + valores['usuario'] + ' Obrigado por utilizar PySimplesGUI!')