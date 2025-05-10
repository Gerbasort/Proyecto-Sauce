import pandas as pd
class Correlativas:
    def __init__(self,regreg,regren,renren,renreg):
        '''
        Recibe:
            - reg_reg: X necesita Y regular para regularizar
            - reg_ren: X necesita Y regular para rendir
            - ren_ren: X necesita Y rendida (aprobada) para rendir
            - ren_reg: X necesita Y rendida (aprobada) para regularizar
        '''
        import pandas as pd
        import numpy as np
        self.labels = regreg.columns

        self.__reg_reg = regreg #   X necesita Y regular para regularizar
        self.__reg_ren = regren #   X necesita Y regular para rendir
        self.__ren_ren = renren #   X necesita Y rendida para rendir
        self.__ren_reg = renreg #   X necesita Y rendida para regularizar

        self.__reg_real = pd.Series([0]*len(self.labels),index=self.labels) #   materias actualmente regularizadas
        self.__ren_real = pd.Series([0]*len(self.labels),index=self.labels) #   materias actualmente rendidas

        self.__reg_disp = pd.Series([0]*len(self.labels),index=self.labels) #   materias actualmente disponibles para regularizar
        self.__reg_disp_df = pd.DataFrame(np.zeros((len(self.labels),len(self.labels))),index=self.labels)  #   matriz de regularizables para hacer cuentas
        self.__ren_disp = pd.Series([0]*len(self.labels),index=self.labels) #   materias actualmente disponibles para rendir
        self.__ren_disp_df = pd.DataFrame(np.zeros((len(self.labels),len(self.labels))),index=self.labels)  #   matriz de rendibles para hacer cuentas

        self.__consistencia()   #   forzamos consistencia

        #   matrices de restricciones reg_reg, reg_ren, ren_ren, ren_reg con bloqueos impuestos por el usuario
        #   los bloqueos del usuario se generan cuando llama a .disponible()
        self.__reg_reg_block = pd.DataFrame(self.__reg_reg.values,index=self.labels)
        self.__reg_ren_block = pd.DataFrame(self.__reg_ren.values,index=self.labels)
        self.__ren_ren_block = pd.DataFrame(self.__ren_ren.values,index=self.labels)
        self.__ren_reg_block = pd.DataFrame(self.__ren_reg.values,index=self.labels)

        #print(self.__reg_reg.values,'\n')
        #print(self.__reg_ren.values,'\n')
        #print(self.__ren_ren.values,'\n')
        #print(self.__ren_reg.values,'\n')
    #===============================================#
    #           Métodos input                       #
    #===============================================#
    def reg_real(self,vector):  #   HACER QUE SE PUEDA METER UN VECTOR DE NOMBRES DE MATERIAS, Y NO UN VECTOR EXPLÍCITO
        '''
        Cargar materias regularizadas actualmente
        '''
        import numpy as np
        self.__reg_real.iloc[:] = vector 
        self.__reg_disp.iloc[:] = vector
        self.__reg_disp_df = pd.DataFrame(np.diag(vector),index=self.labels)
    
    def ren_real(self,vector):  #   HACER QUE SE PUEDA METER UN VECTOR DE NOMBRES DE MATERIAS, Y NO UN VECTOR EXPLÍCITO
        '''
        Cargar materias rendidas (aprobadas) actualmente
        '''
        import numpy as np
        self.__ren_real.iloc[:] = vector 
        self.__ren_disp.iloc[:] = vector
        self.__reg_disp_df = pd.DataFrame(np.diag(vector),index=self.labels)


    def disponibles(self,*blocked):
        '''
        Recibe:
            - blocked:  materias que queremos negar, para ver
                        qué se nos bloquea
        '''
        for materia in blocked: #   genera los bloqueos
            indice = self.__reg_reg.columns.get_loc(materia)
            self.__reg_reg_block.iloc[indice,indice] = 1
            self.__reg_ren_block.iloc[indice,indice] = 1
            self.__ren_ren_block.iloc[indice,indice] = 1
            self.__ren_reg_block.iloc[indice,indice] = 1
        #print(self.__reg_reg_block)
        #print(self.__reg_ren_block)
        #print(self.__ren_ren_block)
        #print(self.__ren_reg_block)
        self.__calc_disponibles()
        return {'cursar':self.__reg_disp,'rendir':self.__ren_disp}

    def inmediatas(self,*blocked):
        '''
        Recibe:
            - blocked:  materia que queremos negar, para ver
                        qué se nos bloquea
        '''

        for materia in blocked: #   genera los bloqueos
            indice = self.__reg_reg.columns.get_loc(materia)
            self.__reg_reg_block.iloc[indice,indice] = 1
            self.__reg_ren_block.iloc[indice,indice] = 1
            self.__ren_ren_block.iloc[indice,indice] = 1
            self.__ren_reg_block.iloc[indice,indice] = 1
        
        reg_now,ren_now = self.__calc_inmediatas()
        return {'cursar':reg_now,'rendir':ren_now}
    
    def completar(self):
        '''
        Devuelve las matrices de correlatividades completas
        teniendo en cuenta las implicaciones (ver .__consistencia())
        '''
        import pandas as pd
        pd.set_option('display.width',200)
        regreg = self.__reg_reg.replace({0:'',1:11})
        renreg = self.__ren_reg.replace({0:'',1:11})
        regren = self.__reg_ren.replace({0:'',1:11})
        renren = self.__ren_ren.replace({0:'',1:11})
        print('--------------------------------------')
        print(f'Regularizar para Cursar:')
        print(regreg.values)
        print('--------------------------------------')
        print(f'Aprobar para Cursar:')
        print(renreg.values)
        print('--------------------------------------')
        print(f'Regularizar para Rendir:')
        print(regren.values)
        print('--------------------------------------')
        print(f'Aprobar para Rendir:')
        print(renren.values)

    def correlatividades(self):
        '''
        Calcula la cantidad de correlatividades de cada materia
        '''
        print('============================================')
        for i in range(len(self.labels)):
            print(f'        {self.labels[i]}        ')
            print(f'Regular para cursar: {sum(self.__reg_reg.iloc[:,i])}')
            print(f'Regular para rendir: {sum(self.__reg_ren.iloc[:,i])}')
            print(f'Aprobada para cursar: {sum(self.__ren_reg.iloc[:,i])}')
            print(f'Aprobada para rendir: {sum(self.__ren_ren.iloc[:,i])}')
            print('---------------------------------------------')
    
    def stats(self):
        '''
        Calcula la cantidad de materias únicas que la necesitan regular o aprobada,
        lo muestra en porcentaje de las materias totales y de las que le siguen.
        '''
        reg = self.__reg_ren + self.__reg_reg
        ren = self.__ren_ren + self.__ren_reg
        print('=============================================')
        for i in range(len(self.labels)):
            suma_reg = sum(1 for j in range(len(self.labels)) if reg.iloc[j,i] != 0)
            suma_ren = sum(1 for j in range(len(self.labels)) if ren.iloc[j,i] != 0)
            num_next = len(self.labels)-(i) # cantidad de materias que le siguen
            print(f'        {self.labels[i]}        ')
            print(f'Regular: {suma_reg} | {round((suma_reg/len(self.labels))*100,1)}% total | {round((suma_reg/num_next)*100,1)}% siguientes')
            print(f'Aprobada: {suma_ren} | {round((suma_ren/len(self.labels))*100,1)}% total | {round((suma_ren/num_next)*100,1)}% siguientes')
            print('---------------------------------------------')

    #================================================#
    #           Métodos cálculo                      #
    #================================================#
    def __reg_reg_calc(self):
        '''
        reg_reg@reg_disp

        Esto es equivalente a verificar qué materias puedo regularizar
        teniendo en cuenta los bloqueos y las materias regularizables
        '''
        import pandas as pd
        import numpy as np

        #print('-------------------------------------------------')
        #print(f'reg_reg_calc')
        #print(self.__reg_reg_block)
        #print(self.__reg_disp_df)
        #print('-------------------------------------------------')
        
        test = self.__reg_reg_block.values@self.__reg_disp_df
        return test
    
    def __reg_ren_calc(self):
        '''
        reg_ren@reg_disp

        Esto es equivalente a verificar qué materias puedo rendir
        teniendo en cuenta los bloqueos y las materias regularizables
        '''
        import pandas as pd
        import numpy as np

        #print('-------------------------------------------------')
        #print(f'reg_ren_calc')
        #print(self.__reg_ren_block)
        #print(self.__reg_disp_df)
        #print('-------------------------------------------------')
        test = self.__reg_ren_block.values@self.__reg_disp_df
        return test
    
    def __ren_ren_calc(self):
        '''
        ren_ren@ren_disp

        Esto es equivalente a verificar qué materias puedo rendir
        teniendo en cuenta los bloqueos y las materias rendibles
        '''
        import pandas as pd
        import numpy as np

        #print('-------------------------------------------------')
        #print(f'ren_ren_calc')
        #print(self.__ren_ren_block)
        #print(self.__ren_disp_df)
        #print('-------------------------------------------------')

        test = self.__ren_ren_block.values@self.__ren_disp_df
        return test

    def __ren_reg_calc(self):
        '''
        reg_reg@ren_disp

        Esto es equivalente a verificar qué materias puedo regularizar
        teniendo en cuenta bloqueos y las materias rendibles
        '''
        import pandas as pd
        import numpy as np

        #print('-------------------------------------------------')
        #print(f'ren_reg_calc')
        #print(self.__ren_reg_block)
        #print(self.__ren_disp_df)
        #print('-------------------------------------------------')
        test = self.__ren_reg_block.values@self.__ren_disp_df

        return test

    def __consistencia(self):
        '''
        Se asegura de que haya consistencia entre los datos

        Las implicaciones son de la siguiente naturaleza:
        
        -----------------------
         reg_reg    →   reg_ren
            ↑              ↑ 
         ren_reg    →   ren_ren
        ------------------------
        -------------------------------------------
         reg_real   →   reg_disp    →   reg_disp_df
            ↑              ↑                 ↑
         ren_real   →   ren_disp    →   ren_disp_df
        -------------------------------------------

        Ambos bloques están desacoplados, por lo que se pueden chequear a la vez
        '''
        n = len(self.__reg_real)
        
        #   ren_real -> (reg_real,ren_disp)
        for i in range(n):
            if (self.__ren_real.iloc[i] == 1).all():
                self.__reg_real.iloc[i] = 1 #   reg_real
                self.__ren_disp.iloc[i] = 1 #   ren_disp

            #   ren_reg -> (reg_reg y ren_ren)  # condiciones desacopladas
            for j in range(n):
                if (self.__ren_reg.iloc[i,j] == 1).all():
                    self.__reg_reg.iloc[i,j] = 1
                    self.__ren_ren.iloc[i,j] = 1
        
        #   [ ren_disp -> (reg_disp y ren_disp_df) ] y [reg_real -> ren_disp]
        for i in range(n):
            if (self.__ren_disp.iloc[i] == 1).all():
                self.__reg_disp.iloc[i] = 1
                self.__ren_disp_df.iloc[i,i] = 1
            elif (self.__reg_real.iloc[i] == 1).all():
                self.__reg_disp.iloc[i] = 1

            #   (reg_reg o ren_ren) -> reg_ren  #   condiciones desacopladas
            for j in range(n):
                if (self.__reg_reg.iloc[i,j] == 1).all() or (self.__ren_ren.iloc[i,j] == 1).all():
                    self.__reg_ren.iloc[i,j] = 1 
        
        #   [reg_disp o ren_disp_df] -> reg_disp_df
        for i in range(n):
            if (self.__reg_disp.iloc[i] == 1).all() or (self.__ren_disp_df.iloc[i,i] == 1).all():
                self.__reg_disp_df.iloc[i,i] = 1


    def __calc_disponibles(self):
        '''
        Desencadena:
          el efecto de las implicaciones
                      +
        la posibilidad de rendir/regularizar

        Hasta llegar a un equilibrio
        --------------------------------------------------
                        |Algoritmo|
                        
            1)  tomamos las dos condiciones de regularidad
        reg_reg y ren_reg

            2)  verificamos que se cumplan ambas para una
        materia dada

            3)  actualizamos la matriz de regularizables

            4)  hacemos lo mismo para las rendibles y las
        actualizamos

            5)  habiendo actualizado las regularizables y
        las rendibles, verificamos si se ha agrandado la
        posibilidad de regularizar materias

            6)  si se agrandó, repetimos desde (1)

            7)  sino, nos detenemos, y devolvemos las materias
        regularizables y las rendibles
        '''
        import numpy as np
        test_reg_reg_new = self.__reg_reg_calc()            #   posibilidades de regularización por materias regularizadas
        #print(f'test_reg_reg:\n{test_reg_reg_new}\n')       ###
        test_ren_reg_new = self.__ren_reg_calc()            #   posibilidades de regularización por materias aprobadas
        #print(f'test_ren_reg:\n{test_ren_reg_new}\n')       ###

        #print('\n',len(test_reg_reg_new))
        while True:
            for i in range(len(test_reg_reg_new)):
                if (test_reg_reg_new.iloc[i,:] == self.__reg_reg_block.values[i,:]).all() and (test_ren_reg_new.iloc[i,:] == self.__ren_reg_block.values[i,:]).all():
                    #print(f'test_reg_reg_new[i]:\n{test_reg_reg_new[i]}\n')
                    #print(f'test_ren_reg_new[i]:\n{test_ren_reg_new[i]}\n')
                    self.__reg_disp_df.iloc[i,i] = 1

            test_reg_ren = self.__reg_ren_calc()
            #print(f'test_reg_ren:\n{test_reg_ren}')
            test_ren_ren = self.__ren_ren_calc()
            #print(f'test_ren_ren:\n{test_ren_ren}')
            for i in range(len(test_reg_ren)):
                if (test_reg_ren.iloc[i,:] == self.__reg_ren_block.values[i,:]).all() and (test_ren_ren.iloc[i,:] == self.__ren_ren_block.values[i,:]).all():
                    self.__ren_disp_df.iloc[i,i] = 1

            test_reg_reg_old = test_reg_reg_new
            test_ren_reg_old = test_ren_reg_new
            test_reg_reg_new = self.__reg_reg_calc()
            #print(f'test_reg_reg:\n{test_reg_reg_new}\n') 
            test_ren_reg_new = self.__ren_reg_calc()
            #print(f'test_ren_reg:\n{test_ren_reg_new}\n') 
            if (test_reg_reg_old == test_reg_reg_new).all().all() and (test_ren_reg_old == test_ren_reg_new).all().all():
                break

        self.__reg_disp.iloc[:] = np.diag(self.__reg_disp_df.values)
        self.__ren_disp.iloc[:] = np.diag(self.__ren_disp_df.values)
    
    def __calc_inmediatas(self):
        '''
        Calcula las materias que se pueden
        regularizar/rendir, dadas las materias
        actuales reg_real, ren_real y los bloqueos.
        '''
        import numpy as np
        reg_real_df = pd.DataFrame(np.diag(self.__reg_real),index=self.labels)
        ren_real_df = pd.DataFrame(np.diag(self.__ren_real),index=self.labels)

        ren_now = pd.Series(self.__ren_real,index=self.labels)
        reg_now = pd.Series(self.__reg_real,index=self.labels)

        test_reg_reg = self.__reg_reg_block.values@reg_real_df
        test_ren_reg = self.__ren_reg_block.values@ren_real_df
        test_reg_ren = self.__reg_ren_block.values@reg_real_df
        test_ren_ren = self.__ren_ren_block.values@ren_real_df

        for i in range(len(test_reg_ren)):
            if (test_reg_reg.iloc[i,:]==self.__reg_reg_block.values[i,:]).all() and (test_ren_reg.iloc[i,:]==self.__ren_reg_block.values[i,:]).all():
                reg_now.iloc[i] = 1
            if (test_reg_ren.iloc[i,:]==self.__reg_ren_block.values[i,:]).all() and (test_ren_ren.iloc[i,:]==self.__ren_ren_block.values[i,:]).all():
                ren_now.iloc[i] = 1
        
        return reg_now,ren_now


#==============================================================================================#
#                                         ÁREA DE TESTEO                                       #
#==============================================================================================#

#   Materias de testeo; NO BORRAR
'''
reg_reg = pd.DataFrame()
reg_reg['Materias'] = ['Álgebra I','Matemática Básica','Matemática Discreta I','Cálculo I']
reg_reg['Álgebra I'] =              [0,0,1,0]
reg_reg['Matemática Básica'] =      [0,0,0,1]
reg_reg['Matemática Discreta I'] =  [0,0,0,0]
reg_reg['Cálculo I'] =              [0,0,0,0]

reg_ren = pd.DataFrame()
reg_ren['Materias'] = ['Álgebra I','Matemática Básica','Matemática Discreta I','Cálculo I']
reg_ren['Álgebra I'] =              [0,0,1,0]
reg_ren['Matemática Básica'] =      [0,0,0,1]
reg_ren['Matemática Discreta I'] =  [0,0,0,0]
reg_ren['Cálculo I'] =              [0,0,0,0]

ren_ren=pd.DataFrame()
ren_ren['Materias'] = ['Álgebra I','Matemática Básica','Matemática Discreta I','Cálculo I']
ren_ren['Álgebra I'] =              [0,0,1,0]
ren_ren['Matemática Básica'] =      [0,0,0,1]
ren_ren['Matemática Discreta I'] =  [0,0,0,0]
ren_ren['Cálculo I'] =              [0,0,0,0]

ren_reg=pd.DataFrame()
ren_reg['Materias'] = ['Álgebra I','Matemática Básica','Matemática Discreta I','Cálculo I']
ren_reg['Álgebra I'] =              [0,0,0,0]
ren_reg['Matemática Básica'] =      [0,0,0,0]
ren_reg['Matemática Discreta I'] =  [0,0,0,0]
ren_reg['Cálculo I'] =              [0,0,0,0]
'''

import correlativas as c
reg_reg = c.reg_reg
reg_ren = c.reg_ren
ren_ren = c.ren_ren
ren_reg = c.ren_reg

test = Correlativas(reg_reg,reg_ren,ren_ren,ren_reg)
#test.reg_real([1,1,1,1,1,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0])
#test.ren_real([1,1,1,1,1,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0])
#disp = test.inmediatas()
#print(f'\n cursar:\n{disp["cursar"]}\n')
#print(f'\n rendir:\n{disp["rendir"]}\n')
test.stats()

