import PySimpleGUI as sg
from numpy import ones
from Gauss_method import Gauss_method, right_matrix
import Methods
from funnyerror import funnyerror


def oshibka_vvoda():
    layout = [[sg.Text('Некорректные данные!')],
              [sg.Button('Решить еще?'), sg.Button('Все.', bind_return_key = True)]]
    window = sg.Window('Ошибка', layout)
    event, values = window.Read()

    if event == 'Решить еще?':
        check = False
        window.close()
    elif event == 'Все.':
        check = True
        window.close()
    elif event is None:
        check = True
        window.close()
    else:
        funnyerror()
    return check


def build_matrixwithGUI():
    text1 = 'Введите количество неизвестных'
    layout = [[sg.Text(text1,size=(35, 1), key='answer')],
            [sg.InputText(key='c_unknown')],
            [sg.Text('')],
            [sg.ReadButton('Ok', bind_return_key = True)]]

    window = sg.Window('Метод Гаусса').Layout(layout)
    clown = True
    while clown:
        button, values = window.Read()

        if button is None:
            break

        c_unknown = int(values['c_unknown'])
        window.FindElement('c_unknown').Update('')
        matrix = ones((c_unknown, c_unknown+1))
        for i in range(c_unknown):
            answer = 'Введите коэффициенты при Х{0}'.format(i+1)
            window.FindElement('answer').Update(answer)
            button, values = window.Read()
            neizv = list(values['c_unknown'].split())
            for number_x in range(c_unknown):
                matrix[number_x][i] = float(neizv[number_x])
            window.FindElement('c_unknown').Update('')
        answer = 'Введите свободные коэффициенты'
        window.FindElement('answer').Update(answer)
        button, values = window.Read()
        free_coef = list(values['c_unknown'].split())
        for number_free in range(c_unknown):
            matrix[number_free][c_unknown] = float(free_coef[number_free])
        window.close()
        clown = False
    matrix = right_matrix(matrix, c_unknown)
    check = not(clown)
    return matrix, c_unknown


def get_cof_and_vecwithGUI(name):
    '''
    return mtr_cof, mtr_vec, var
    '''
    text1 = 'Введите количество неизвестных'
    layout = [[sg.Text(text1,size=(35, 1), key='answer')],
            [sg.InputText(key='c_unknown')],
            [sg.Text('')],
            [sg.ReadButton('Ok', bind_return_key = True)]]

    window = sg.Window(name).Layout(layout)
    clown = True
    while clown:
        button, values = window.Read()

        if button is None:
            break

        var = int(values['c_unknown'])
        window.FindElement('c_unknown').Update('')
        mtr_cof = ones((var, var))
        for i in range(var):
            answer = 'Введите коэффициенты при Х{0}'.format(i+1)
            window.FindElement('answer').Update(answer)
            button, values = window.Read()
            neizv = list(values['c_unknown'].split())
            for number_x in range(var):
                mtr_cof[number_x][i] = float(neizv[number_x])
            window.FindElement('c_unknown').Update('')
        answer = 'Введите свободные коэффициенты'
        window.FindElement('answer').Update(answer)
        button, values = window.Read()
        mtr_vec = list(map(float,values['c_unknown'].split()))
        window.close()
        clown = False
    return mtr_cof, mtr_vec, var


def vivod_gwGUI_LOOP(matrix_copy, cool_matrix, cool_vivod, pogreshnost, check):
    if check:
        lst = ['Расширенная матрица коэффициентов', matrix_copy,
               'Приведенная к треугольному виду матрица', cool_matrix,
               'Корни', cool_vivod,
               'Погрешность', pogreshnost]
        temp = [[sg.Text(i)] for i in lst]
        buttons = [[sg.Button('Решить еще?'), sg.Button('Все.', bind_return_key = True)]]
        layout = temp + buttons

        window = sg.Window('Решение').Layout(layout)
    else:
        layout = [[sg.Text('ДАННУЮ СИСТЕМУ')],
                  [sg.Text('НЕЛЬЗЯ РЕШИТЬ')],
                  [sg.Text('МЕТОДОМ ГАУССА')],
                  [sg.Button('Решить еще?'), sg.Button('Все.', bind_return_key = True)]]
        window = sg.Window('Ошибка').Layout(layout)
    event, values = window.Read()

    if event == 'Решить еще?':
        check = False
        window.close()
    elif event == 'Все.':
        check = True
        window.close()
    elif event is None:
        check = True
        window.close()
    else:
        funnyerror()
    return check


def vivod_mmGUI_LOOP(mtr_cof, mtr_vec, razn, check, list_x, name):
    if check:
        lst = ['Матрица коэффициентов', mtr_cof,
                'Матрица свободных членов', mtr_vec,
                'Корни', list_x,
                'Погрешность', razn]

        temp = [[sg.Text(i)] for i in lst]
        buttons = [[sg.Button('Решить еще?'), sg.Button('Все.', bind_return_key = True)]]
        layout = temp + buttons

        window = sg.Window('Решение').Layout(layout)

    else:
        if name == 'Матричный метод':
            layout = [[sg.Text('ДАННУЮ СИСТЕМУ')],
                  [sg.Text('НЕЛЬЗЯ РЕШИТЬ')],
                  [sg.Text('МАТРИЧНЫМ МЕТОДОМ')],
                  [sg.Button('Решить еще?'), sg.Button('Все.', bind_return_key = True)]]
            window = sg.Window('Ошибка').Layout(layout)

        elif name == 'Метод Крамера':
            layout = [[sg.Text('ДАННУЮ СИСТЕМУ')],
                    [sg.Text('НЕЛЬЗЯ РЕШИТЬ')],
                    [sg.Text('МЕТОДОМ КРАМЕРА')],
                    [sg.Button('Решить еще?'), sg.Button('Все.', bind_return_key = True)]]
            window = sg.Window('Ошибка').Layout(layout)
        else:
            funnyerror()
            return False
    event, values = window.Read()

    if event == 'Решить еще?':
        check = False
        window.close()
    elif event == 'Все.':
        check = True
        window.close()
    elif event is None:
        check = True
        window.close()
    else:
        funnyerror()
    return check


def Obr_matrixwithGUI():
    name = 'Матричный метод'
    mtr_cof, mtr_vec, var = get_cof_and_vecwithGUI(name)
    mtr_cof, mtr_vec, var, razn, check, list_x = Methods.Obr_matrix_method(mtr_cof, mtr_vec, var)
    check = vivod_mmGUI_LOOP(mtr_cof, mtr_vec, razn, check, list_x, name)
    return check


def Kramer_methodwithGUI():
    name = 'Метод Крамера'
    mtr_cof, mtr_vec, var = get_cof_and_vecwithGUI(name)
    mtr_cof, mtr_vec, var, razn, check, list_x = Methods.Kramer_method(mtr_cof, mtr_vec, var)
    check = vivod_mmGUI_LOOP(mtr_cof, mtr_vec, razn, check, list_x, name)
    return check


def Gauss_methodwithGUI():
    '''
    return check
    '''
    matrix, c_unknown, = build_matrixwithGUI()
    matrix_copy, cool_matrix, cool_vivod, pogreshnost, check = Gauss_method(matrix, c_unknown)
    check = vivod_gwGUI_LOOP(matrix_copy, cool_matrix, cool_vivod, pogreshnost, check)
    return check

if __name__ == '__main__':
    pass
