class ContaBancaria:
    def __init__(self, nome, numero_conta, saldo_inicial=0):
        self.nome = nome
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial
        self.extrato = [(saldo_inicial, "Saldo inicial")]
        self.limite_diario_saque = 500.0
        self.saldo_diario_saque = self.limite_diario_saque

    def deposito(self, valor):
        self.saldo += valor
        self.extrato.append((valor, "Depósito"))

    def saque(self, valor):
        if valor <= self.saldo_diario_saque:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saldo_diario_saque -= valor
                self.extrato.append((-valor, "Saque"))
                return True
            else:
                print("Saldo insuficiente para o saque.")
                return False
        else:
            print("Limite diário de saque excedido. O limite é R$ 500,00.")
            return False

    def obter_extrato(self):
        return self.extrato

    def __str__(self):
        return f"Conta: {self.numero_conta}, Nome: {self.nome}, Saldo: R$ {self.saldo:.2f}"


def menu():
    print("\n==== Menu ====")
    print("1. Nova conta")
    print("2. Depósito")
    print("3. Saque")
    print("4. Extrato")
    print("5. Investimento")
    print("6. Empréstimo")
    print("7. Sair")


contas = {}


def nova_conta():
    nome = input("Digite o nome do titular da conta: ")
    numero_conta = input("Digite o número da conta: ")
    saldo_inicial = float(input("Digite o saldo inicial: "))
    contas[numero_conta] = ContaBancaria(nome, numero_conta, saldo_inicial)
    print("Conta criada com sucesso!")


def deposito():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        valor = float(input("Digite o valor do depósito: "))
        contas[numero_conta].deposito(valor)
        print("Depósito realizado com sucesso!")
    else:
        print("Conta não encontrada.")


def saque():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        valor = float(input("Digite o valor do saque: "))
        if contas[numero_conta].saque(valor):
            print("Saque realizado com sucesso!")
        else:
            print("Saque não realizado.")
    else:
        print("Conta não encontrada.")


def extrato():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        print("\nExtrato:")
        for valor, descricao in contas[numero_conta].obter_extrato():
            print(f"{descricao}: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {contas[numero_conta].saldo:.2f}")
    else:
        print("Conta não encontrada.")


def investimento():
    print("Essa função ainda não foi implementada.")


def emprestimo():
    print("Essa função ainda não foi implementada.")


if __name__ == "__main__":
    while True:
        menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            nova_conta()
        elif opcao == "2":
            deposito()
        elif opcao == "3":
            saque()
        elif opcao == "4":
            extrato()
        elif opcao == "5":
            investimento()
        elif opcao == "6":
            emprestimo()
        elif opcao == "7":
            print("Saindo do sistema bancário...")
            break
        else:
            print("Opção inválida. Tente novamente.")
