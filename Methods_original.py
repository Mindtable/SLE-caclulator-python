from numpy import ones, around
import numpy as np
import copy

def right_matrix(matrix, count_of_unknown):
    for bulduga in range(count_of_unknown-1):
        temp_bulduga = bulduga
        maincoef = matrix[bulduga][bulduga] 
        for i in range(bulduga, count_of_unknown-1):
            if abs(maincoef) < abs(matrix[i+1][bulduga]):
                maincoef = matrix[i+1][bulduga]
                temp_bulduga = i + 1
        a = list(matrix[bulduga])
        b = list(matrix[temp_bulduga])
        matrix[bulduga] = b
        matrix[temp_bulduga] = a
    return matrix
    
def cool_matr(matrix, count_of_unknown):
    copy_matrix = copy(matrix)
    for i in range(count_of_unknown):
        for z in range(count_of_unknown+1):
            copy_matrix[i][z] = around(copy_matrix[i][z], 3)
    return copy_matrix
    
def build_matrix():
    '''
    Эта функция организует ввод коэффициентов
    и строит на их основе матрицу коэффициентов
    '''
    # global count_of_unknown, matrix
    count_of_unknown = int(input("Введите количество переменных в системе - "))
    matrix = ones((count_of_unknown, count_of_unknown+1))
    for i in range(count_of_unknown):
        vvod = input("Введите коэфициэнты при х{0} - ".format(i+1))
        neizv = list(map(float, vvod.split()))
        for number_x in range(count_of_unknown):
            matrix[number_x][i] = neizv[number_x]
    free_coef = list(map(float, input("Введите свободные коэфициэнты - ").split()))
    for number_free in range(count_of_unknown):
        matrix[number_free][count_of_unknown] = free_coef[number_free]
    matrix = right_matrix(matrix, count_of_unknown)
    print("\n Изначальная матрица")
    print(matrix)
    return matrix, count_of_unknown

def make_matrix_to_triangle(matrix, count_of_unknown:int):
    """Данная функция выполняет прямой ход Гаусса
       Сначала она находит максимальный коэффициент
       ниже главной диагонали, ставит строку с этим коэффициентом
       так, чтобы он находился на главной диагонали, а потом
       зануляет все коэффициенты ниже главного. И так для всех
       неизвестных на главной диагонали.
    """
    for bulduga in range(count_of_unknown-1):
        maincoef = matrix[bulduga][bulduga] 
        for p in range(bulduga, count_of_unknown-1):
            koef = -(matrix[p+1][bulduga] / maincoef)
            xstring = matrix[bulduga] * koef
            matrix[p+1] = matrix[p+1] + xstring
    cool_matrix = cool_matr(matrix, count_of_unknown)
    print("\n Приведенная матрица")
    print(cool_matrix)
    return matrix

def found_korni(matrix, count_of_unknown):
    '''
    Эта функция выполняет обратный ход гаусса - 
    находит корни уравнения.
    '''
    list_korney = [0,]*count_of_unknown
    for i in range(count_of_unknown-1, -1, -1):
        summa = 0
        for z in range(i+1, count_of_unknown):
            summa += matrix[i][z]*list_korney[z]
        na_chto_delit = matrix[i][count_of_unknown] - summa
        list_korney[i] = na_chto_delit/matrix[i][i]
    return list_korney

def cool_vivod_korney(list_korney):
    '''
    Данная функция выводит корни с точностью до
    3 знака после запятой(сами корни при этом не меняются).
    '''
    vivod_korney = list(list_korney)
    for i in range(len(vivod_korney)):
        vivod_korney[i] = around(vivod_korney[i], 6)
    print("\n Найденные корни")
    print(vivod_korney)

def found_pogreshnost(matrix, list_korney, count_of_unknown):
    '''
    Эта функция находит погрешность вычисления,
    посредством вычитания из свободного коэффициента
    суммы произведения неизвестного на его коэффициент.
    '''
    pogreshnost =[0, ]*count_of_unknown
    for i in range(count_of_unknown):
        summa = 0
        for z in range(count_of_unknown):
            summa += matrix[i][z]*list_korney[z]
        pogreshnost[i] = matrix[i][count_of_unknown] - summa
    print("\n Погрешность при вычислении")
    print(pogreshnost)

def reed_cof():
    '''Эта функция создаёт список с коэффициентам уравнений в линейном порядке запрашивая их у пользователя
    '''
    kol_yr = int(input("Сколько уравнений в системе? "))
    Matrix_cof = []
    print("Введите коэффициенты")
    for i in range(kol_yr):
        r = input()
        Matrix_cof.append(list(map(int, r.split())))
    return Matrix_cof, kol_yr


def reed_vec():
    '''Эта функция создаёт список со свободными членами уравнений запрашивая их у пользователя
    '''
    print("Введите вектор свободных членов")
    Matrix_vec = []
    r = input()
    Matrix_vec.append(list(map(float, r.split())))
    return Matrix_vec

def det_cof(Matrix_cof):
    D = np.linalg.det(Matrix_cof)
    return D

def kramer(Matrix_cof, Matrix_vec, D, kol_yr):
    '''Этот 
    '''
    X=[]
    for i in range(kol_yr):
        Matrix = copy.deepcopy(Matrix_cof)
        for j in range(kol_yr): 
            
            Matrix[j][i]=Matrix_vec[0][j]
                
        Di = np.linalg.det(Matrix) 
        X.append(Di/D)
    return X
def proverka(Matrix_cof, Matrix_vec, X, kol_yr):
    for i in range(kol_yr):
        Summ=0
        for j in range(kol_yr):
            Summ += X[j]*Matrix_cof[i][j]
        Razn = Matrix_vec[0][i]-Summ
        print("Разница в ", i+1, "уравнении = ", Razn, sep="")

def cool_print(X):
    cool_X = list(X)
    for i in range(len(cool_X)):
        cool_X[i] = np.around(cool_X[i], 3)
    print(cool_X)

def inv_matrix(Matrix_cof):
    invers_matrix = np.linalg.inv(Matrix_cof)
    return invers_matrix

def Obr_matrix(invers_matrix, Matrix_vec, kol_yr):
    X=[]
    n=kol_yr
    st=0
    while n!=0:
        n-=1
        el=0
        x=0
        while el!=kol_yr:
            x += invers_matrix[st][el]*Matrix_vec[0][el]
            el+=1
        X.append(x)
        st+=1 
    return X 

def Obr_matrix_method():
    Matrix_cof=[]
    Matrix_vec=[]
    X=[]
    Matrix_cof, a = reed_cof()
    Matrix_vec = reed_vec()    
    invers_matrix = inv_matrix(Matrix_cof)
    X = Obr_matrix(invers_matrix, Matrix_vec, a)
    cool_print(X)
    proverka(Matrix_cof, Matrix_vec, X, a)

def Kramer_method():
    Matrix_cof=[]
    Matrix_vec=[]
    X=[]
    D=0
    X=0
    Matrix_cof, a = reed_cof()
    Matrix_vec = reed_vec()
    D = det_cof(Matrix_cof)
    if D == 0:
        print("Так как D=0 систему невозможно решить методом крамера")
    else:
        X = kramer(Matrix_cof, Matrix_vec, D, a)
        cool_print(X)
        proverka(Matrix_cof, Matrix_vec, X, a)

def Gauss_method():
    '''
    Собственно, сам метод Гаусса
    '''
    matrix, count_of_unknown = build_matrix()
    matrix_changed = make_matrix_to_triangle(matrix, count_of_unknown)
    list_korney = found_korni(matrix_changed, count_of_unknown)
    cool_vivod_korney(list_korney)
    found_pogreshnost(matrix, list_korney, count_of_unknown)