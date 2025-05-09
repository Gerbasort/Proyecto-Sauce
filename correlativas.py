import pandas as pd

reg_reg = pd.DataFrame()    #   necesita regular para regularizar?
reg_ren = pd.DataFrame()    #   necesita regular para rendir?
ren_reg = pd.DataFrame()    #   necesita rendida para regularizar?
ren_ren = pd.DataFrame()    #   necesita rendida para rendir?

reg_real = pd.Series()      #   regulares reales  # input usuario
ren_real = pd.Series()      #   rendidas reales   # input usuario

reg_disp = pd.Series()      #   posibles de regularizar
ren_disp = pd.Series()      #   posibles de rendir

reg_reg['materias'] = ['Álgebra I',
                       'Matemática Básica',
                       'Matemática Discreta I',
                       'Cálculo I',
                       'Programación',
                       'Álgebra Lineal',
                       'Análisis Matricial',
                       'Cálculo II',
                       'Física',
                       'EDO',
                       'Álgebra II',
                       'Programación Lineal',
                       'Análisis Real I',
                       'Probabilidad y Estadística',
                       'Cálculo Científico',
                       'Probabilidad',
                       'EDP',
                       'Análisis Numérico',
                       'Estadística',
                       'Análisis Complejo',
                       'Modelos Matemáticos',
                       'Análisis Real II',
                       'Geometría de curvas']

#   Las matrices se ven como su transpuesta, puesto que cargamos las columnas una por una
#   ESTA ESTÁ BIEN ✅
reg_reg['Álgebra I'] =                  [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Matemática Básica'] =          [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Matemática Discreta I'] =      [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Cálculo I'] =                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Programación'] =               [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
reg_reg['Álgebra Lineal'] =             [0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
reg_reg['Análisis Matricial'] =         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Cálculo II'] =                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
reg_reg['Física'] =                     [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['EDO'] =                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
reg_reg['Álgebra II'] =                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Programación Lineal'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Análisis Real I'] =            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Probabilidad y Estadística'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Cálculo Científico'] =         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Probabilidad'] =               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0]
reg_reg['EDP'] =                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0]
reg_reg['Análisis Numérico'] =          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Estadística'] =                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Análisis Complejo'] =          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Modelos Matemáticos'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Análisis Real II'] =           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Geometría de curvas'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#   CARGADA (CHEQUEAR)                          #5        #10       #15       #20
reg_ren['Álgebra I'] =                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Matemática Básica'] =          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Matemática Discreta I'] =      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Cálculo I'] =                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Programación'] =               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Álgebra Lineal'] =             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Análisis Matricial'] =         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Cálculo II'] =                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
reg_ren['Física'] =                     [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['EDO'] =                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
reg_ren['Álgebra II'] =                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Programación Lineal'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Análisis Real I'] =            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Probabilidad y Estadística'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Cálculo Científico'] =         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
reg_ren['Probabilidad'] =               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0]
reg_ren['EDP'] =                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Análisis Numérico'] =          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Estadística'] =                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Análisis Complejo'] =          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Modelos Matemáticos'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Análisis Real II'] =           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Geometría de curvas'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#   CARGADA (CHEQUEAR)                          #5        #10       #15       #20
ren_ren['Álgebra I'] =                  [0,0,0,0,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Matemática Básica'] =          [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Matemática Discreta I'] =      [0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0]
ren_ren['Cálculo I'] =                  [0,0,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0]
ren_ren['Programación'] =               [0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0]
ren_ren['Álgebra Lineal'] =             [0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0]
ren_ren['Análisis Matricial'] =         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0]
ren_ren['Cálculo II'] =                 [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1]
ren_ren['Física'] =                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
ren_ren['EDO'] =                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1]
ren_ren['Álgebra II'] =                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Programación Lineal'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
ren_ren['Análisis Real I'] =            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0]
ren_ren['Probabilidad y Estadística'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0]
ren_ren['Cálculo Científico'] =         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0]
ren_ren['Probabilidad'] =               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['EDP'] =                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Análisis Numérico'] =          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Estadística'] =                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Análisis Complejo'] =          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Modelos Matemáticos'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Análisis Real II'] =           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Geometría de curvas'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#   CARGADA (CHEQUEAR)                          #5        #10       #15       #20
ren_reg['Álgebra I'] =                  [0,0,1,0,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Matemática Básica'] =          [0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Matemática Discreta I'] =      [0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0]
ren_reg['Cálculo I'] =                  [0,0,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0]
ren_reg['Programación'] =               [0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0]
ren_reg['Álgebra Lineal'] =             [0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0]
ren_reg['Análisis Matricial'] =         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0]
ren_reg['Cálculo II'] =                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1]
ren_reg['Física'] =                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
ren_reg['EDO'] =                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1]
ren_reg['Álgebra II'] =                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Programación Lineal'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
ren_reg['Análisis Real I'] =            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0]
ren_reg['Probabilidad y Estadística'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0]
ren_reg['Cálculo Científico'] =         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0]
ren_reg['Probabilidad'] =               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
ren_reg['EDP'] =                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Análisis Numérico'] =          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Estadística'] =                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Análisis Complejo'] =          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Modelos Matemáticos'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Análisis Real II'] =           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Geometría de curvas'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
