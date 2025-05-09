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
        #print(regreg.shape)
        #print(self.labels)
        #print(len(self.labels))

        self.__reg_reg = regreg
        self.__reg_ren = regren
        self.__ren_ren = renren
        self.__ren_reg = renreg

        self.__reg_real = pd.Series([0]*len(self.labels),index=self.labels)
        self.__ren_real = pd.Series([0]*len(self.labels),index=self.labels)

        self.__reg_disp = pd.Series([0]*len(self.labels),index=self.labels)
        self.__reg_disp_df = pd.DataFrame(np.zeros((len(self.labels),len(self.labels))),index=self.labels)
        self.__ren_disp = pd.Series([0]*len(self.labels),index=self.labels)   
        self.__ren_disp_df = pd.DataFrame(np.zeros((len(self.labels),len(self.labels))),index=self.labels)

        self.__consistencia()

        self.__reg_reg_block = pd.DataFrame(self.__reg_reg.values,index=self.labels)
        self.__reg_ren_block = pd.DataFrame(self.__reg_ren.values,index=self.labels)
        self.__ren_ren_block = pd.DataFrame(self.__ren_ren.values,index=self.labels)
        self.__ren_reg_block = pd.DataFrame(self.__ren_reg.values,index=self.labels)

        print(self.__reg_reg.values,'\n')
        print(self.__reg_ren.values,'\n')
        print(self.__ren_ren.values,'\n')
        print(self.__ren_reg.values,'\n')
    #===============================================#
    #           Métodos input                       #
    #===============================================#
    def reg_real(self,vector):
        import numpy as np
        self.__reg_real.iloc[:] = vector 
        self.__reg_disp.iloc[:] = vector
        self.__reg_disp_df = np.diag(vector)
    
    def ren_real(self,vector):
        import numpy as np
        self.__ren_real.iloc[:] = vector 
        self.__ren_disp.iloc[:] = vector
        self.__reg_disp_df = np.diag(vector)


    def disponibles(self,*blocked):
        '''
        Recibe:
            - blocked:  materias que queremos negar, para ver
                        qué se nos bloquea
        '''
        for materia in blocked:
            indice = self.__reg_reg.columns.get_loc(materia)
            self.__reg_reg_block.iloc[indice,indice] = 1
            self.__reg_ren_block.iloc[indice,indice] = 1
            self.__ren_ren_block.iloc[indice,indice] = 1
            self.__ren_reg_block.iloc[indice,indice] = 1
        #print(self.__reg_reg_block)
        #print(self.__reg_ren_block)
        #print(self.__ren_ren_block)
        #print(self.__ren_reg_block)
        self.__calc()
        return {'cursar':self.__reg_disp,'rendir':self.__ren_disp}
    #================================================#
    #           Métodos cálculo                      #
    #================================================#
    def __reg_reg_calc(self):
        '''
        Calcula reg_reg@reg_disp_df de forma iterativa
        Esto actualiza reg_disp_df hasta que no se puede actualizar más
        '''
        import pandas as pd
        import numpy as np

        #print('-------------------------------------------------')
        #print(f'reg_reg_calc')
        #print(self.__reg_reg_block)
        #print(self.__reg_disp_df)
        #print('-------------------------------------------------')
        
        test = self.__reg_reg_block.values@self.__reg_disp_df.values
        return test
    
    def __reg_ren_calc(self):
        '''
        Calcula reg_ren@reg_disp_df; esto actualiza ren_disp_df una sóla vez
        '''
        import pandas as pd
        import numpy as np

        #print('-------------------------------------------------')
        #print(f'reg_ren_calc')
        #print(self.__reg_ren_block)
        #print(self.__reg_disp_df)
        #print('-------------------------------------------------')
        test = self.__reg_ren_block.values@self.__reg_disp_df.values
        return test
    
    def __ren_ren_calc(self):
        '''
        Calcula ren_ren@ren_disp_df de forma iterativa
        Esto actualiza ren_disp_df hasta que no se puede actualizar más
        '''
        import pandas as pd
        import numpy as np

        #print('-------------------------------------------------')
        #print(f'ren_ren_calc')
        #print(self.__ren_ren_block)
        #print(self.__ren_disp_df)
        #print('-------------------------------------------------')

        test = self.__ren_ren_block.values@self.__ren_disp_df.values
        return test

    def __ren_reg_calc(self):
        '''
        Calcula reg_ren@reg_disp_df; esto actualiza ren_disp_df una sóla vez
        '''
        import pandas as pd
        import numpy as np

        #print('-------------------------------------------------')
        #print(f'ren_reg_calc')
        #print(self.__ren_reg_block)
        #print(self.__ren_disp_df)
        #print('-------------------------------------------------')
        test = self.__ren_reg_block.values@self.__ren_disp_df.values

        return test

    def __consistencia(self):
        '''
        Se asegura de que haya consistencia entre los datos
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


    def __calc(self):
        '''
        Relaciona los distintos cálculos.

        Estos se van actualizando entre sí
        hasta que se llega a un equilibrio.

        Estas serán las matrices/vectores
        finales.
        '''
        import numpy as np
        test_reg_reg_new = self.__reg_reg_calc()            #   posibilidades de regularización por materias regularizadas
        #print(f'test_reg_reg:\n{test_reg_reg_new}\n')       ###
        test_ren_reg_new = self.__ren_reg_calc()            #   posibilidades de regularización por materias aprobadas
        #print(f'test_ren_reg:\n{test_ren_reg_new}\n')       ###

        while True:
            for i in range(len(test_reg_reg_new)):
                if (test_reg_reg_new[i] == self.__reg_reg_block.values[i,:]).all() and (test_ren_reg_new[i] == self.__ren_reg_block.values[i,:]).all():
                    #print(f'test_reg_reg_new[i]:\n{test_reg_reg_new[i]}\n')
                    #print(f'test_ren_reg_new[i]:\n{test_ren_reg_new[i]}\n')
                    self.__reg_disp_df.iloc[i,i] = 1

            test_reg_ren = self.__reg_ren_calc()
            test_ren_ren = self.__ren_ren_calc()
            for i in range(len(test_reg_ren)):
                if (test_reg_ren[i] == self.__reg_ren_block.values[i,:]).all() and (test_ren_ren[i] == self.__ren_ren_block.values[i,:]).all():
                    self.__ren_disp_df.iloc[i,i] = 1

            test_reg_reg_old = test_reg_reg_new
            test_ren_reg_old = test_ren_reg_new
            test_reg_reg_new = self.__reg_reg_calc()
            test_ren_reg_new = self.__ren_reg_calc()
            if (test_reg_reg_old == test_reg_reg_new).all() and (test_ren_reg_old == test_ren_reg_new).all():
                break
            

        self.__reg_disp.iloc[:] = np.diag(self.__reg_disp_df.values)
        self.__ren_disp.iloc[:] = np.diag(self.__ren_disp_df.values)

#==============================================================================================#
#                                         ÁREA DE TESTEO                                       #
#==============================================================================================#
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
disp = test.disponibles('Cálculo I')
print(f'cursar:\n{disp["cursar"]}\n')
print(f'rendir:\n{disp["rendir"]}\n')
