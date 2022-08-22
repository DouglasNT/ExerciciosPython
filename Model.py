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
        self.totalReajuste = 0
        self.totalSalario = 0
        self.percDistri = 0
        self.percImp = 0
        self.totalConsum = 0
        self.totalNota = 0
        self.totalMacas = 0
        self.comissao = 0
        self.comissao1 = 0
        self.comissao2 = 0
        self.totalComissao = 0
        self.saldoAtual = 0
        self.contador = 0
        self.soma = 0
        self.arit = 0
        self.vetor = [] #Está variável é um Array

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

    def getSalario(self):
        return self.salario

    def setSalario(self, salario):
        self.salario = salario

    def getReajuste(self):
        return self.reajuste

    def setReajuste(self, reajuste):
        self.reajuste = reajuste

    def getValorCusto(self):
        return self.valorCusto

    def setValorCusto(self, valorCusto):
        self.valorCusto = valorCusto

    def getNota1(self):
        return self.nota1

    def setNota1(self, nota1):
        self.nota1 = nota1

    def getNota2(self):
        return self.nota2

    def setNota2(self, nota2):
        self.nota2 = nota2

    def getNota3(self):
        return self.nota3

    def setNota3(self, nota3):
        self.nota3 = nota3

    def getMacas(self):
        return self.macas

    def setMacas(self, macas):
        self.macas = macas

    def getSalarioFixo(self):
        return self.salarioFixo

    def setSalarioFixo(self, salarioFixo):
        self.salarioFixo = salarioFixo

    def getVendas(self):
        return self.vendas

    def setVendas(self, vendas):
        self.vendas = vendas

    def getSaldo(self):
        return self.saldo

    def setSaldo(self, saldo):
        self.saldo = saldo

    def getDebito(self):
        return self.debito

    def setDebito(self, debito):
        self.debito = debito

    def getCredito(self):
        return self.credito

    def setCredito(self, credito):
        self.credito = credito

    def getNum(self):
        return self.num

    def setNum(self, num):
        self.num = num

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
    def exercicio6(self, salario, reajuste):
        self.setSalario(salario)
        self.setReajuste(reajuste)

        self.totalReajuste = (self.getSalario() / 100 ) * self.getReajuste()
        self.totalSalario = self.getSalario() + self.totalReajuste

        return self.totalSalario

#Exercicio 7:
    def exercicio7(self, valorCusto):
        self.setValorCusto(valorCusto)

        self.percDistri = (self.getValorCusto() / 100) * 28
        self.percImp = (self.getValorCusto() / 100) * 45
        self.totalConsum = self.getValorCusto() + self.percDistri + self.percImp

        return self.totalConsum

#Exercicio 8:
    def exercicio8(self, nota1, nota2, nota3):
        self.setNota1(nota1)
        self.setNota2(nota2)
        self.setNota3(nota3)

        self.totalNota = (self.getNota1() + self.getNota2() + self.getNota3()) / 3

        return self.totalNota

#Exercicio 9:
    def exercicio9(self, macas):
        self.setMacas(macas)

        if self.getMacas() > 11:
            self.totalMacas = self.getMacas() * 1

        else:
            self.totalMacas = self.getMacas() * 1.3

        return self.totalMacas

#Exercicio 10:
    def preencherVetor(self, num):
        self.vetor.append(num) #incluindo dados no Vetor

    def visualizarVetor(self):
        for i in range(len(self.vetor)):
            print("{}º número: {}\n".format(i+1,self.vetor[i]))

    def ordenar(self):
        self.vetor.sort() #O elemento "sort" ira ordenar em ordem crescente o vetor
        self.visualizarVetor()

    def excluir(self, posicao):
        self.vetor.pop(posicao)
        self.visualizarVetor()

    def incluir(self, posicao, num):
        self.vetor[posicao].append(num)


#Exercicio 11:
    def exercicio11(self, salarioFixo,vendas):
        self.setSalarioFixo(salarioFixo)
        self.setVendas(vendas)

        if self.getVendas() > 1500:
            self.comissao = (1500 / 100) * 3
            self.comissao1 = self.getVendas() - 1500
            self.comissao2 = (self.comissao1 / 100) * 5

            self.totalComissao = self.getSalarioFixo() + self.comissao + self.comissao2

        else:
            self.totalComissao = (self.getVendas() / 100) * 3

        return self.totalComissao

#Exercicio 12
    def exercicio12(self, conta, saldo, debito,credito):
        self.setSaldo(saldo)
        self.setDebito(debito)
        self.setCredito(credito)

        self.saldoAtual = self.getSaldo() - self.getDebito() + self.getCredito()

        if self.saldoAtual > 0:
            return "R$ {} - Saldo Positivo".format(self.saldoAtual)

        else:
            return "R$ {} - Saldo Negativo".format(self.saldoAtual)

#Exercicio 13
    def exercicio13(self, num):
        self.setNum(num)

        while self.contador < 11:
            print(self.getNum(), "X", self.contador, "=", self.getNum() * self.contador)
            self.contador = self.contador + 1

#Exercicio 14
    def exercicio14(self, num):
        self.setNum(num)
        self.contador = 1
        while (self.contador < self.getNum()) or (self.contador == self.getNum()):
            print(self.contador)
            self.contador = self.contador + 1

#Exercicio 15
    def exercicio15(self, num):
        self.setNum(num)

        if self.getNum() < 0:
            self.contador = self.contador + 1
        return "\nQuantidade de numeros negativos: {}".format(self.contador)

#Exercicio 16
    def exercicio16(self, num):
        self.setNum(num)

        if self.getNum() < 40:
            self.soma = self.soma + self.getNum()
        return "\nO valor do valores inferiores a 40 somados é de: {}".format(self.soma)

#Exercicio 17
    def exercicio17(self):
        self.contador = 15
        self.soma = 0
        while (self.contador < 100) or (self.contador == 100):
            self.soma = self.soma + self.contador
            self.contador = self.contador + 1
        self.arit = self.soma / 85
        return "\nO valor da média aritmétrica é: {}".format(self.arit)

#Exercicio 18
    def exercicio18(self, num):
        self.setNum(num)

        self.arit = self.arit + self.getNum()
        if self.soma < self.getNum():
            self.soma = self.getNum()

        self.aux = self.arit / 10



        return "\nO maior numero digitado foi: {}\nE a média ficou: {}".format(self.soma, self.aux)