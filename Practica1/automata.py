#-*-encoding:utf8-*-

class Analizador_Texto:

    def __init__(self):
        self.letra_actual = ''
        self.estado_actual = 0
        self.valor_lexema = ''
        self.operadores = ['+','-','E','.']
        self.aceptacion = True
        self.reserv = ['Teorema', 'teorema', 'Matemático', 'Matemática', 'matemático', 'matemática',
        'Hilbert', 'Turing', 'análisis', 'Análisis', 'Euler', 'Fermat', 'Pitágoras', 'autóata', 'Boole', 'Cantor',
        'Experimentación', 'experimentación', 'Físico', 'Física', 'físico', 'física', 'Astronomía', 'astronomía',
        'mecánica', 'Mecánica', 'Newton', 'Einstein', 'Galileo', 'modelo', 'Modelo', 'Tesla', 'Dinámica', 'dinámica']

    def switch(self, estado):
        self.estados = {
        0: self.estado_0,
        1: self.estado_1,
        2: self.estado_2,
        3: self.estado_3,
        4: self.estado_4,
        5: self.estado_5,
        6: self.estado_6,
        7: self.estado_7,
        8: self.estado_8,
        9: self.estado_9,
        10: self.estado_10,
        11: self.estado_11,
        }
        func = self.estados.get(estado, lambda: 'No es un caracter válido')
        return func()

    def valuar_dato(self, dato):
        try:
            int(dato)
            return True
        except ValueError:
            return False

    def estado_0(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[0] or str(self.letra_actual) == self.operadores[1]:
                self.estado_actual = 1
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            if int(self.letra_actual) > 0:
                self.estado_actual = 3
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif int(self.letra_actual) == 0:
                self.estado_actual = 4
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print 'Cadena no aceptada'

    def estado_1(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) > 0:
                self.estado_actual = 3
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif int(self.letra_actual) == 0:
                self.estado_actual = 2
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print 'Cadena no aceptada'
        else:
            self.estado_actual = 10
            self.valor_lexema = self.valor_lexema + self.letra_actual

    def estado_2(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[3]:
                self.estado_actual = 5
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.aceptacion = False
            print 'Cadena no aceptada'

    def estado_3(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[2]:
                self.estado_actual = 6
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == self.operadores[3]:
                self.estado_actual = 5
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == ' ':
                print 'Esto es un numero entero ', self.valor_lexema
                self.aceptacion = False
            else:
                self.estado_actual = 3
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.estado_actual = 11
            self.valor_lexema = self.valor_lexema + self.letra_actual
            self.aceptacion = True

    def estado_4(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[3]:
                self.estado_actual = 5
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == ' ':
                print 'Esto es un numero entero ', self.valor_lexema
                self.aceptacion = False
            else:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.aceptacion = False
            print 'Cadena no aceptada'

    def estado_5(self):
        if self.valuar_dato(self.letra_actual) == False:
            self.estado_actual = 10
            self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.estado_actual = 11
            self.valor_lexema = self.valor_lexema + self.letra_actual

    def estado_6(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[0] or str(self.letra_actual) == self.operadores[1]:
                self.estado_actual = 7
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            if int(self.letra_actual) > 0:
                self.estado_actual = 8
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif int(self.letra_actual) == 0:
                self.estado_actual = 9
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print 'Cadena no aceptada'

    def estado_7(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) > 0:
                self.estado_actual = 8
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print 'Cadena no aceptada'
        else:
            self.estado_actual = 10
            self.valor_lexema = self.valor_lexema + self.letra_actual

    def estado_8(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == ' ':
                print 'Esto es un numero en notacion cientifica ', self.valor_lexema
                self.aceptacion = False
            else:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.estado_actual = 8
            self.valor_lexema = self.valor_lexema + self.letra_actual
            self.aceptacion = True

    def estado_9(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == ' ':
                print 'Esto es un numero en notacion cientifica ', self.valor_lexema
                self.aceptacion = False
            else:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.aceptacion = False
            print 'Cadena no aceptada'

    def estado_10(self):
        if str(self.letra_actual) == ' ':
            if self.valor_lexema in self.reserv:
                print 'Esto es una palabra reservada', self.valor_lexema
                self.actpacion = False
            else:
                print 'Esto es una cadena ', self.valor_lexema
                self.aceptacion = False
        else:
            self.estado_actual = 10
            self.valor_lexema = self.valor_lexema + self.letra_actual
            self.aceptacion = True

    def estado_11(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[2]:
                self.estado_actual = 6
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == ' ':
                print 'Esto es un numero real ', self.valor_lexema
                self.aceptacion = False
            else:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.estado_actual = 11
            self.valor_lexema = self.valor_lexema + self.letra_actual
            self.aceptacion = True

    def analizar(self, cadena):
        cadena = str(cadena)
        palabras = cadena.split()
        for i in palabras:
            self.aceptacion = True
            self.valor_lexema = ""
            self.estado_actual = 0
            i = i + ' '
            for x in i:
                if self.aceptacion == True:
                    self.letra_actual = x
                    self.switch(self.estado_actual)

Analizador_Texto().analizar(raw_input('Escriba la cadena: '))
