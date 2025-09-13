import NetworkX as nx

#################################################
#       |Correlatividades|                      #
#################################################
#Se necesita key aprobada para rendir value
correlativa_rendir = {  1:(7,11),
                        2:(4,5),
                        3:(6),
                        4:(9,11,12,14,15,17),
                        5:(8,11,12),
                        6:(10,12),
                        7:(12,13,16),
                        8:(13,14,15,21),
                        9:(16),
                        10:(13,21),
                        11:(15),
                        12:(20),
                        13:(16),
                        14:(18,23),
                        15:(25),
                        16:(),
                        17:(),
                        18:(),
                        19:(21),
                        20:(),
                        21:(),
                        22:(),
                        23:(),
                        24:(),}

#################################################
#           |lógica|                            #
#################################################
def bloqueo(plan,*bloqueadas):
    '''
    Qué materias se pueden hacer si se bloquean "bloqueadas"
    -------------------------------------------------------
    -plan: diccionario
    '''
    materias = plan.keys()
    ya_bloqueadas = bloqueadas
    for materia in materias:
        if materia in bloqueadas:



#################################################
#           |Input|                             #
#################################################