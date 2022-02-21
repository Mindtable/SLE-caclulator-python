import PySimpleGUI as sg
import test
from funnyerror import funnyerror

# def oshibka_vvoda():
#     layout = [[sg.Text('Некорректные данные!')],
#               [sg.Button('Решить еще?'), sg.Button('Все.', bind_return_key = True)]]
#     window = sg.Window('Ошибка', layout)
#     event, values = window.Read()

#     if event == 'Решить еще?':
#         check = False
#         window.close()
#     elif event == 'Все.':
#         check = True
#         window.close()
#     elif event is None:
#         check = True
#         window.close()
#     else:
#         funnyerror()
#     return check


def main():
    while True:
        layout = [[sg.Text('Выберите метод решения СЛАУ',)],
                [sg.Button('Гаусса'), sg.Button('Крамера'),
                sg.Button('Матричный')]]

        window = sg.Window('Решить СЛАУ').Layout(layout)

        events, values = window.Read()

        if events is None:
            break

        if events == 'Гаусса':
            window.close()
            check = test.Gauss_methodwithGUI()
        elif events == 'Крамера':
            window.close()
            check = test.Kramer_methodwithGUI()
        elif events == 'Матричный':
            window.close()
            check = test.Obr_matrixwithGUI()
        else:
            window.close()
            break
        if check:
            break


if __name__ == '__main__':
    main()

