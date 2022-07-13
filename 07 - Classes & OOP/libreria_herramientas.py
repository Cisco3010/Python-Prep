class herramientas:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros
        # if type(self.lista) != list:
        #     raise ValueError('Debe ingresar una lista de números enteros')
        # elif len(self.lista) == 0:
        #     raise ValueError('Debe ingresar al menos un número entero a la lista')
        # for i in self.lista:
        #     if type(i) != int:
        #         raise ValueError('Todos los números de la lista deben ser Enteros')
        #         break
    
    def es_primo(self):
        for i in self.lista:
            self.__es_primo(i)
    
    def convertidor_grados(self, de='Celsius', a='Farenheit'):
        for i in self.lista:
            self.__convertidor_grados(i, de, a)

    def factorial(self):
        for i in self.lista:
            self.__factorial(i)

    def __es_primo(self, num):
        dem = 2
        a = True
        while num > dem:
            if num%dem == 0:
                a = False
                break
            dem += 1
        if a == True:
            print(f'{num} es primo')
            return(num)
        else:
            print(f'{num} no es primo')
    
    def num_masmen_repe(self, mayor=True):
        unicos = []
        repeticiones = []
        for i,e in enumerate(self.lista):
                for j,l in enumerate(self.lista):
                    if i < j:
                        if e not in unicos:
                            if e == l:
                                unicos.append(e)
                                repeticiones.append(1)

        unicos_2 = []
        for i,e in enumerate(x):
                if e not in unicos_2:
                    for j,l in enumerate(x):
                        if e in unicos:
                            if i < j:
                                    if e == l:
                                        unicos_2.append(e)
                                        repeticiones[unicos.index(e)] = repeticiones[unicos.index(e)] + 1
        i_mas_repe = repeticiones.index(max(repeticiones))
        i_menos_repe = repeticiones.index(min(repeticiones))
        mas_repe = unicos[i_mas_repe]
        veces_mas_repe = repeticiones[i_mas_repe]
        min_repe = unicos[i_menos_repe]
        veces_menos_repe = repeticiones[i_menos_repe]

        if mayor == True:
            print(f'El número que más se repite es el {mas_repe} y se repite {veces_mas_repe} veces')
        else:
            print(f'El número que menos se repite es el {min_repe} y se repite {veces_menos_repe} veces')

    def __convertidor_grados(self, gi, de='Celsius',a='Farenheit'):
        if (a != 'Celsius') & (a != 'Farenheit') & (a != 'Kelvin'):
            print('Debe ingresar Celsius, Farenheit o Kelvin')
    ## De C a 
        elif de == 'Celsius':
            if a == 'Farenheit':
                g = (gi * 9/5) + 32
                
            else:
                g = gi+273.15
    ## De F a
        elif de == 'Farenheit':
            if a == 'Celsius':
                g = ((gi - 32)*5)/9
            else:
                g = ((gi - 32)*5)/9 + 273.15 

    # De K a
        elif de == 'Kelvin':
            if a == 'Celsius':
                g = gi - 273.15 
            else:
                g = ((gi - 273.15)* 9/5) + 32
        else:
            print('Debe ingresar un Número Entero, Celsius, Farenheit o Kelvin')
        print(f'{gi}° grados {de} son {g}° grados {a}')    
        return(g, gi, de, a)
        

    def __factorial(self, x):
        if (type(x) != int):
            return('Debe ingresar un numero entero y postivo')
        elif (x < 0):
            return('Debe ingresar un numero entero y postivo')
        elif x == 0:
            f = 1
        else:
            f = x
            while x > 1:
                f = f*(x-1)
                x -= 1
            return f
