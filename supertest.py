import PySimpleGUI as sg
lst = ['Расширенная матрица коэффициентов', 1,
           'Приведенная к треугольному виду матрица', 1,
            'Корни', 1,
            'Погрешность', 1]

temp = [[sg.Text(i)] for i in lst]
# print(temp)


layout = [[sg.Text('Расширенная матрица коэффициентов')],
              [sg.Text(1)],
              [sg.Text('Приведенная к треугольному виду матрица')],
              [sg.Text(1)],
              [sg.Text('Корни')],
              [sg.Text(1)],
              [sg.Text('Погрешность')],
              [sg.Text(1)]]
print(layout)