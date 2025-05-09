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
        self.labels = regreg.iloc[:,1:].index

        self.__reg_reg = regreg
        self.__reg_ren = regren
        self.__ren_ren = renren
        self.__ren_reg = renreg

        self.__reg_reg_block = pd.DataFrame(regreg.values,index=self.labels)
        self.__reg_ren_block = pd.DataFrame(regren.values,index=self.labels)
        self.__ren_ren_block = pd.DataFrame(renren.values,index=self.labels)
        self.__ren_reg_block = pd.DataFrame(renreg.values,index=self.labels)

        self.__reg_real = pd.Series([None]*len(self.labels),index=self.labels)
        self.__ren_real = pd.Series([None]*len(self.labels),index=self.labels)

        self.__reg_disp = pd.Series([0]*len(self.labels),index=self.labels)
        self.__reg_disp_df = pd.DataFrame(np.zeros((len(self.labels),len(self.labels))),index=self.labels)
        self.__reg_disp_df.insert(0,'Materias',regreg['Materias'])
        self.__ren_disp = pd.Series([0]*len(self.labels),index=self.labels)   
        self.__ren_disp_df = pd.DataFrame(np.zeros((len(self.labels),len(self.labels))),index=self.labels)
        self.__ren_disp_df.insert(0,'Materias',regreg['Materias'])
    #===============================================#
    #           Métodos input                       #
    #===============================================#
    def reg_real(self,vector):
        import numpy as np
        self.__reg_real.iloc[:] = vector 
        self.__reg_disp.iloc[:] = vector
        self.__reg_disp_df.iloc[:,1:] = np.diag(vector)
    
    def ren_real(self,vector):
        import numpy as np
        self.__ren_real.iloc[:] = vector 
        self.__ren_disp.iloc[:] = vector
        self.__ren_disp_df.iloc[:,1:] = np.diag(vector)

    def disponibles(self,*blocked):
        '''
        Recibe:
            - blocked:  materias que queremos negar, para ver
                        qué se nos bloquea
        '''
        for materia in blocked:
            indice = self.__reg_reg.columns.get_loc(materia)
            print(f'indice:\n{indice}')
            self.__reg_reg_block.iloc[indice-1,indice] = 1
            self.__reg_ren_block.iloc[indice-1,indice] = 1
            self.__ren_ren_block.iloc[indice-1,indice] = 1
            self.__ren_reg_block.iloc[indice-1,indice] = 1
        print(self.__reg_reg_block)
        print(self.__reg_ren_block)
        print(self.__ren_ren_block)
        print(self.__ren_reg_block)
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
        #print(f'reg_reg:\n {self.__reg_reg_block.values[:,1:]}')
        test_new = self.__reg_reg_block.values[:,1:]@self.__reg_disp_df.values[:,1:]

        while True:
            print(f'reg_disp_df:\n{self.__reg_disp_df.values[:,1:]}\n') ###
            print(f'test_new:\n{test_new}\n')   ###

            for i in range(len(self.labels)):
                print('###')
                print(f'reg_reg_block[i]:\n{self.__reg_reg_block.values[i,1:]}\n')
                print('###')
                if (test_new[i,:] == self.__reg_reg_block.values[i,1:]).all():

                    self.__reg_disp_df.iloc[i,i+1] = 1

            test_old = test_new
            test_new = self.__reg_reg_block.values[:,1:]@self.__reg_disp_df.values[:,1:]
            print(f'reg_disp_df_new:\n {self.__reg_disp_df.values[:,1:]}\n')
            print(f'test_old:\n{test_old}\n')
            print(f'test_old==test_new:\n{test_old==test_new}\n')
            print(f'(test_old==test_new).all():\n{(test_old==test_new).all()}')
            print('------------------------------')
            if (test_old == test_new).all():
                break
        print('===========================')
        print(f'last test:\n{test_new}\n')
        print('===========================')
        return test_new
    
    def __reg_ren_calc(self):
        '''
        Calcula reg_ren@reg_disp_df; esto actualiza ren_disp_df una sóla vez
        '''
        import pandas as pd
        import numpy as np

        test = self.__reg_ren_block.values[:,1:]@self.__reg_disp_df.values[:,1:]
        print('------------')
        print(f'test:\n {test}\n')

        for i in range(len(self.labels)):
            print(f'reg_ren_block[i]:\n{self.__reg_ren_block.values[i,1:]}')    ###
            if (test[i,:] == self.__reg_ren_block.values[i,1:]).all():
                self.__ren_disp_df.iloc[i,i+1] = 1
        
        return test
    
    def __ren_ren_calc(self):
        '''
        Calcula ren_ren@ren_disp_df de forma iterativa
        Esto actualiza ren_disp_df hasta que no se puede actualizar más
        '''
        import pandas as pd
        import numpy as np

        test_new = self.__ren_ren_block.values[:,1:]@self.__ren_disp_df.values[:,1:]
        while True:

            for i in range(len(self.labels)):
                if (test_new[i,:] == self.__ren_ren_block.values[i,1:]).all():
                    self.__ren_disp_df.iloc[i,i+1] = 1

            test_old = test_new
            test_new = self.__ren_ren_block.values[:,1:]@self.__ren_disp_df.values[:,1:]
            if (test_old == test_new).all():
                break

        return test_new

    def __ren_reg_calc(self):
        '''
        Calcula reg_ren@reg_disp_df; esto actualiza ren_disp_df una sóla vez
        '''
        import pandas as pd
        import numpy as np
        print(f'ren_disp_df:\n{self.__ren_disp_df}\n')  ###
        print(f'reg_disp_df:\n{self.__reg_disp_df}\n')
        print(f'ren_reg_block:\n{self.__ren_reg_block.values[:,1:]}\n')
        test = self.__ren_reg_block.values[:,1:]@self.__ren_disp_df.values[:,1:]
        print(f'test:\n{test}\n')   ###
        for i in range(len(self.labels)):
            print(f'ren_reg_block[i]:\n{self.__ren_reg_block.values[i,1:]}')    ###
            if (test[i,:] == self.__ren_reg_block.values[i,1:]).all():
                self.__reg_disp_df.iloc[i,i+1] = 1
        
        return test

    def __calc(self):
        '''
        Relaciona los distintos cálculos.

        Estos se van actualizando entre sí
        hasta que se llega a un equilibrio.

        Estas serán las matrices/vectores
        finales.
        '''
        import numpy as np
        test_new = self.__reg_ren_calc()
        while True:
            self.__ren_ren_calc()
            self.__ren_reg_calc()
            self.__reg_reg_calc()
            test_old = test_new
            test_new = self.__reg_ren_calc()
            if (test_new == test_old).all():
                break

        
        self.__reg_disp.iloc[:] = np.diag(self.__reg_disp_df.values[:,1:])
        self.__ren_disp.iloc[:] = np.diag(self.__ren_disp_df.values[:,1:])

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

test = Correlativas(reg_reg,reg_ren,ren_ren,ren_reg)
test.reg_real([0,0,0,0])
disp = test.disponibles('Álgebra I')
print(f'cursar:\n{disp["cursar"]}\n')
print(f'rendir:\n{disp["rendir"]}\n')