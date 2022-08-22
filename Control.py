from Model import Model

class Control:
    def __init__(self):
        self.metodo = Model() #Instanciando a Classe Model
        self.opcao = -1
        self.contador = 1


    def menu(self):
        print("\nEscolha umas das opções abaixo:  \n\n" +
              "0. Sair \n" +
              "1. Exercicio 1\n" +
              "2. Exercicio 2\n" +
              "3. Exercicio 3\n" +
              "4. Exercicio 4\n" +
              "5. Exercicio 5\n" +
              "6. Exercicio 6\n" +
              "7. Exercicio 7\n" +
              "8. Exercicio 8\n" +
              "9. Exercicio 9\n" +
              "10. Exercicio 10\n" +
              "11. Exercicio 11\n" +
              "12. Exercicio 12\n" +
              "13. Exercicio 13\n" +
              "14. Exercicio 14\n" +
              "15. Exercicio 15\n" +
              "16. Exercicio 16\n" +
              "17. Exercicio 17\n" +
              "18. Exercicio 18\n" +
              "19. Exercicio 19\n" +
              "20. Exercicio 20\n")

        self.opcao = int(input())

    def operacao(self):
        while(self.opcao != 0):
            self.menu() #Chamando o Menu

            if self.opcao == 0:
                print("Obrigado!")

            elif self.opcao == 1:
                print("A: 10\n"
                      "B: 20")
                print(self.metodo.exercicio1())

            elif self.opcao == 2:
                print("Digite um valor inteiro: \n")
                num1 = int(input())
                print("o Numero antecessor ao numero digitado é: ")
                print(self.metodo.exercicio2(num1))

            elif self.opcao == 3:
                print("Digite a Base do Retângulo: \n")
                base = float(input())
                print("Digite a Altura do Retângulo: \n")
                altura = float(input())
                print("A área do Retângulo é: ")
                print((self.metodo.exercicio3(base, altura)))

            elif self.opcao == 4:
                print("Digite a sua idade em Anos: \n")
                ano = int(input())
                print("Mes: \n")
                mes = int(input())
                print("Dias: \n")
                dia = int(input())
                print("Sua idade em dias é: ")
                print(self.metodo.exercicio4(ano, mes, dia))

            elif self.opcao == 5:
                print("Digite o numero total de eleitores: \n")
                eleitores = float(input())
                print("Digite o total de votos Brancos: \n")
                brancos = float(input())
                print("Digite o total de votos nulos: \n")
                nulos = float(input())
                print("Digite o total de votos válidos: \n")
                validos = float(input())
                print(self.metodo.exercicio5(eleitores, brancos, nulos, validos))

            elif self.opcao == 6:
                print("Digite o Salário atual: \n")
                salario = float(input())
                print("Digite o percentual de reajuste: \n")
                reajuste = int(input())
                print("O novo salario é: ")
                print(self.metodo.exercicio6(salario, reajuste))

            elif self.opcao == 7:
                print("Digite o valor de custo do carro: \n")
                valorCusto = float(input())
                print("O valor do Carro ao consumidor é de: ")
                print(self.metodo.exercicio7(valorCusto))

            elif self.opcao == 8:
                print("Digite a primeira nota: \n")
                nota1 = int(input())
                print("Digite a segunda nota: \n")
                nota2 = int(input())
                print("Digite a terceira nota: \n")
                nota3 = int(input())
                print("A média ficou: ")
                print(self.metodo.exercicio8(nota1, nota2, nota3))

            elif self.opcao == 9:
                print("Digite o total de maçãs: \n")
                macas = int(input())
                print("O valor total ficou: R$")
                print(self.metodo.exercicio9(macas))

            elif self.opcao == 10:
                i = 0
                for i in range(10):
                    print("Informe o {}º número: ".format(i+1))
                    self.metodo.preencherVetor(int(input()))
                print("\nSem ordenação!")
                self.metodo.visualizarVetor()

                print("\nCom ordenação!")
                self.metodo.ordenar()

            elif self.opcao == 11:
                print("Digite o salário fixo: \n")
                salarioFixo = float(input())
                print("Digite o valor das vendas do vendedor: \n")
                vendas = float(input())
                print("O salário atual ficou: R$")
                print(self.metodo.exercicio11(salarioFixo, vendas))

            elif self.opcao == 12:
                print("Digite a conta do cliente: \n")
                conta = int(input())
                print("Digite o saldo atual: \n")
                saldo = float(input())
                print("Digite o Débito: \n")
                debito = float(input())
                print("Digite o Crédito: \n")
                credito = float(input())
                print("O saldo ficou: \n")
                print(self.metodo.exercicio12(conta, saldo, debito,credito))

            elif self.opcao == 13:
                print("Digite um numero de 1 a 10: \n")
                num = int(input())
                while (num < 1) or (num > 10):
                    print("Valor incorreto!!!\nDigite Novamente: ")
                    num = int(input())
                print("A tabuada é: \n")
                print(self.metodo.exercicio13(num))

            elif self.opcao == 14:
                print("Digite um valor inteiro maior que Zero: \n")
                num = int(input())
                while num <= 0:
                    print("Valor Incorreto!!!\nDigite Novamente: ")
                    num = int(input())
                print("Os valores são: ")
                print(self.metodo.exercicio14(num))

            elif self.opcao == 15:
                while self.contador < 10:
                    print("\nDigite um numero: \n")
                    num = int(input())
                    self.contador = self.contador + 1
                    print(self.metodo.exercicio15(num))

            elif self.opcao == 16:
                while self.contador < 10:
                    print("\nDigite um numero: \n")
                    num = int(input())
                    self.contador = self.contador + 1
                    print(self.metodo.exercicio16(num))

            elif self.opcao == 17:
                print("A media aritmétrica de 15 a 100 é: \n")
                print(self.metodo.exercicio17())

            elif self.opcao == 18:
                self.contador = 0
                while self.contador < 10:
                    self.contador = self.contador + 1
                    print("Digite um numero: \n")
                    num = int(input())
                    print(num)
                    print(self.metodo.exercicio18(num))