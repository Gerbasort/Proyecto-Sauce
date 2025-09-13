import pandas as pd

reg_reg = pd.DataFrame()    #   necesita regular para regularizar?
reg_ren = pd.DataFrame()    #   necesita regular para rendir?
ren_reg = pd.DataFrame()    #   necesita rendida para regularizar?
ren_ren = pd.DataFrame()    #   necesita rendida para rendir?

reg_real = pd.Series()      #   regulares reales  # input usuario
ren_real = pd.Series()      #   rendidas reales   # input usuario

reg_disp = pd.Series()      #   posibles de regularizar
ren_disp = pd.Series()      #   posibles de rendir

#   Las matrices se ven como su transpuesta, puesto que cargamos las columnas una por una
#   ESTA ESTÁ BIEN ✅                           #5       #10       #15       #20
reg_reg['Álgebra'] =                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Matemática Básica'] =          [0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Ciencia de Datos I'] =         [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Álgebra Lineal'] =             [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Cálculo I'] =                  [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Ciencia de Datos II'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Matemática Discreta'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Cálculo II'] =                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
reg_reg['Análisis Matricial'] =         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Ciencia de Datos III'] =       [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Física'] =                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Modelos y Métodos de Programación Lineal'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Probabilidad'] =               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
reg_reg['Estructuras Lineales y Topológicas'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Ecuaciones Diferenciales Ordinarias'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Estadística'] =                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Estructuras Algebráicas'] =    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Medida e Integración'] =       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
reg_reg['Métodos Numéricos I'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
reg_reg['Optimizacipn Matemática y Toma de Decisiones'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Métodos Numéricos II'] =       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Análisis Complejo'] =          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Principios del Análisis Funcional'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_reg['Ecuaciones Diferenciales Parciales'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#   CARGADA (CHEQUEAR)                          #5        #10       #15       #20
reg_ren['Álgebra'] =                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Matemática Básica'] =          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Ciencia de Datos I'] =         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Álgebra Lineal'] =             [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Cálculo I'] =                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Ciencia de Datos II'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Matemática Discreta'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Cálculo II'] =                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
reg_ren['Análisis Matricial'] =         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Ciencia de Datos III'] =       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Física'] =                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Modelos y Métodos de Programación Lineal'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Probabilidad'] =               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Estructuras Lineales y Topológicas'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Ecuaciones Diferenciales Ordinarias'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Estadística'] =                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Estructuras Algebráicas'] =    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Medida e Integración'] =       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
reg_ren['Métodos Numéricos I'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Optimizacipn Matemática y Toma de Decisiones'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Métodos Numéricos II'] =       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Análisis Complejo'] =          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Principios del Análisis Funcional'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reg_ren['Ecuaciones Diferenciales Parciales'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#   CARGADA (CHEQUEAR)                          #5        #10       #15       #20     
ren_ren['Álgebra'] =                    [0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Matemática Básica'] =          [0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Ciencia de Datos I'] =         [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Álgebra Lineal'] =             [0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0]
ren_ren['Cálculo I'] =                  [0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0]
ren_ren['Ciencia de Datos II'] =        [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0]
ren_ren['Matemática Discreta'] =        [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0]
ren_ren['Cálculo II'] =                 [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,0,0]
ren_ren['Análisis Matricial'] =         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
ren_ren['Ciencia de Datos III'] =       [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0]
ren_ren['Física'] =                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
ren_ren['Modelos y Métodos de Programación Lineal'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
ren_ren['Probabilidad'] =               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
ren_ren['Estructuras Lineales y Topológicas'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0]
ren_ren['Ecuaciones Diferenciales Ordinarias'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
ren_ren['Estadística'] =                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Estructuras Algebráicas'] =    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Medida e Integración'] =       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Métodos Numéricos I'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
ren_ren['Optimizacipn Matemática y Toma de Decisiones'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Métodos Numéricos II'] =       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Análisis Complejo'] =          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Principios del Análisis Funcional'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_ren['Ecuaciones Diferenciales Parciales'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#   CARGADA (CHEQUEAR)                          #5        #10       #15       #20       
ren_reg['Álgebra'] =                    [0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Matemática Básica'] =          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Ciencia de Datos I'] =         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Álgebra Lineal'] =             [0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,1,0,0,0,0,0,0]
ren_reg['Cálculo I'] =                  [0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Ciencia de Datos II'] =        [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0]
ren_reg['Matemática Discreta'] =        [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0]
ren_reg['Cálculo II'] =                 [0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0]
ren_reg['Análisis Matricial'] =         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
ren_reg['Ciencia de Datos III'] =       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
ren_reg['Física'] =                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
ren_reg['Modelos y Métodos de Programación Lineal'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
ren_reg['Probabilidad'] =               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Estructuras Lineales y Topológicas'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0]
ren_reg['Ecuaciones Diferenciales Ordinarias'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
ren_reg['Estadística'] =                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Estructuras Algebráicas'] =    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Medida e Integración'] =       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Métodos Numéricos I'] =        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Optimizacipn Matemática y Toma de Decisiones'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Métodos Numéricos II'] =       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Análisis Complejo'] =          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Principios del Análisis Funcional'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ren_reg['Ecuaciones Diferenciales Parciales'] =\
                                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
