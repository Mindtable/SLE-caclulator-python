from numpy import ones, around
import numpy as np
import copy


# def build_matrix():
#     '''
#     Эта функция организует ввод коэффициентов
#     и строит на их основе матрицу коэффициентов
#     '''
#     # global count_of_unknown, matrix
#     count_of_unknown = int(input("Введите количество переменных в системе - "))
#     matrix = ones((count_of_unknown, count_of_unknown+1))
#     for i in range(count_of_unknown):
#         vvod = input("Введите коэфициэнты при х{0} - ".format(i+1))
#         neizv = list(map(float, vvod.split()))
#         for number_x in range(count_of_unknown):
#             matrix[number_x][i] = neizv[number_x]
#     free_coef = list(map(float, input("Введите свободные коэфициэнты - ").split()))
#     for number_free in range(count_of_unknown):
#         matrix[number_free][count_of_unknown] = free_coef[number_free]
#     matrix = right_matrix(matrix, count_of_unknown)
#     print("\n Изначальная матрица")
#     print(matrix)
#     return matrix, count_of_unknown


def get_cof_and_vec():
    var = int(input('Введите количество неизвестных - '))
    mtr_cof = np.ones((var, var))
    for i in range(var):
        varlist = input('Введите коэффициенты при Х{0} - '.format(i+1))
        varlist = list(map(float, varlist.split()))
        for n_x in range(var):
            mtr_cof[n_x][i] = varlist[n_x]
    varlist = input('Введите свободные коэффициенты - ')
    mtr_vec = list(map(float, varlist.split()))
    return mtr_cof, mtr_vec, var


def kramer(mtr_cof, Matrix_vec, D, kol_yr):
    '''Этот
    '''
    X = []
    for i in range(kol_yr):
        Matrix = copy.deepcopy(mtr_cof)
        for j in range(kol_yr):
            Matrix[j][i] = Matrix_vec[j]
        Di = np.linalg.det(Matrix)
        X.append(Di/D)
    return X


def proverka(mtr_cof, mtr_vec, list_x, var):
    razn = [0]*var
    for i in range(var):
        Summ = 0
        for j in range(var):
            Summ += list_x[j]*mtr_cof[i][j]
        razn[i] = mtr_vec[i] - Summ
    return razn


def Obr_matrix(invers_matrix, Matrix_vec, kol_yr):
    X=[]
    n=kol_yr
    st=0
    while n!=0:
        n-=1
        el=0
        x=0
        while el!=kol_yr:
            x += invers_matrix[st][el]*Matrix_vec[el]
            el+=1
        X.append(x)
        st+=1
    return X


def cool_print(X):
    cool_X = list(X)
    for i in range(len(cool_X)):
        cool_X[i] = np.around(cool_X[i], 3)
    return cool_X


def Kramer_method(mtr_cof, mtr_vec, var):
    '''
    return mtr_cof, mtr_vec, var, razn, check, list_x
    '''
    det = np.linalg.det(mtr_cof)
    if det == 0:
        mtr_cof = mtr_vec = var = det = razn = list_x = 1
        check = False
    else:
        list_x = kramer(mtr_cof, mtr_vec, det, var)
        razn = proverka(mtr_cof, mtr_vec, list_x, var)
        list_x = cool_print(list_x)
        check = True
    return mtr_cof, mtr_vec, var, razn, check, list_x


def Obr_matrix_method(mtr_cof, mtr_vec, var):
    '''
    return mtr_cof, mtr_vec, var, razn, check, list_x
    '''
    det = np.linalg.det(mtr_cof)
    if det==0:
        mtr_cof = mtr_vec = var = det = razn = list_x = 1
        check = False 
    else:  
        inv_mtr = np.linalg.inv(mtr_cof)
        list_x = Obr_matrix(inv_mtr, mtr_vec, var)
        razn = proverka(mtr_cof, mtr_vec, list_x, var)
        list_x = cool_print(list_x)
        check = True
    return mtr_cof, mtr_vec, var, razn, check, list_x


def Test_number1():
    mtr_cof, mtr_vec, var = get_cof_and_vec()
    n = '\n'*2
    print(mtr_cof, n, mtr_vec, n, var)


def Test_number2():
    mtr_cof, mtr_vec, var = get_cof_and_vec()
    mtr_cof, mtr_vec, var, razn, check, list_x = Kramer_method(mtr_cof, mtr_vec, var)
    if check:
        n = '\n'*2
        print(mtr_cof, n, mtr_vec, n, var, n, razn, n, check, list_x)
    else:
        print('систему решить нельзя')


def Test_number3():
    mtr_cof, mtr_vec, var = get_cof_and_vec()
    mtr_cof, mtr_vec, var, razn, check, list_x = Obr_matrix_method(mtr_cof, mtr_vec, var)
    n = '\n'*2
    print(mtr_cof, mtr_vec, var, razn, check, list_x, sep=n)


if __name__ == '__main__':
    test = int(input('Выберите номер теста - '))
    if test == 1:
        Test_number1()
    elif test == 2:
        Test_number2()
    elif test == 3:
        Test_number3()
    pass