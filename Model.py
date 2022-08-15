class Model:

    def __init__(self): #Método Construtor
        self.a = 10
        self.b = 20
        self.aux = 0
        self.num1 = 0
        self.totalAno = 0
        self.totalMes = 0
        self.total = 0
        self.porcBranco = 0
        self.porcNulos = 0
        self.porcValido = 0

    #Métodos de Acesso

    def getA(self):
        return self.a

    def setA(self, a):
        self.a = a

    def getB(self):
        return self.b

    def setB(self, b):
        self.b = b

    def getAux(self):
        return self.aux

    def setAux(self, aux):
        self.aux = aux

    def getNum1(self):
        return self.num1

    def setNum1(self, num1):
        self.num1 = num1

    def getAltura(self):
        return self.altura

    def setAltura(self, altura):
        self.altura = altura

    def getBase(self):
        return self.base

    def setBase(self, base):
        self.base = base

    def getAno(self):
        return self.ano

    def setAno(self, ano):
        self.ano = ano

    def getMes(self):
        return self.mes

    def setMes(self, mes):
        self.mes = mes

    def getDia(self):
        return self.dia

    def setDia(self, dia):
        self.dia = dia

    def getEleitores(self):
        return self.eleitores

    def setEleitores(self, eleitores):
        self.eleitores = eleitores

    def getBrancos(self):
        return self.brancos

    def setBrancos(self, brancos):
        self.brancos = brancos

    def getNulos(self):
        return self.nulos

    def setNulos(self, nulos):
        self.nulos = nulos

    def getValidos(self):
        return self.validos

    def setValidos(self, validos):
        self.validos = validos

#Exercício 1:
    def exercicio1(self):
        self.getAux = self.getA
        self.getA = self.getB
        self.getB = self.getAux
        return "Os valores trocados são: \nA: {}\nB: {}".format(self.getA(), self.getB())

#Exercício 2:
    def exercicio2(self, num1):
        self.setNum1(num1)
        return self.getNum1() - 1

#Exercício 3:
    def exercicio3(self, base, altura):
        self.setBase(base)
        self.setAltura(altura)
        return self.getBase() * self.getAltura()

#Exercício 4:
    def exercicio4(self, ano, mes, dia):
        self.setAno(ano)
        self.setMes(mes)
        self.setDia(dia)

        self.totalAno = self.getAno() * 365
        self.totalMes = self.getMes() * 30
        self.total = self.getDia() + self.totalAno + self.totalMes

        return self.total

#Exercício 5:
    def exercicio5(self, eleitores, brancos, nulos, validos):
        self.setEleitores(eleitores)
        self.setBrancos(brancos)
        self.setNulos(nulos)
        self.setValidos(validos)

        self.porcBranco = (100 / self.getEleitores()) * self.getBrancos()
        self.porcNulos = (100 /self.getEleitores()) * self.getNulos()
        self.porcValido = (100 / self.getEleitores()) * self.getValidos()

        return "O Porcentual ficou: \nBrancos: {}%\nNulos: {}%\nVálidos: {}%".format(self.porcBranco, self.porcNulos, self.porcValido)

#Exercício 6:
    def exercicio6(self):