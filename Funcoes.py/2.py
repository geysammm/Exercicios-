class ContaBancaria:
    def __init__(self, titular, numero_conta, tipo_conta):
        self.titular = titular
        self.saldo = 0.0  # Saldo inicial é 0
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
            self.verificar_saldo()
        else:
            print("Valor de depósito deve ser positivo!")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
            self.verificar_saldo()
        else:
            print("Saque inválido! Verifique o saldo ou o valor.")

    def transferir(self, valor, conta_destino):
        if 0 < valor <= self.saldo:
            self.sacar(valor)  # Chama o método sacar para retirar o valor da conta atual
            conta_destino.depositar(valor)  # Chama o método depositar na conta destino
            print(f"Transferência de R${valor:.2f} para a conta {conta_destino.numero_conta} realizada com sucesso!")
        else:
            print("Transferência inválida! Verifique o saldo ou o valor.")

    def verificar_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")

# Exemplo de uso da classe ContaBancaria
conta1 = ContaBancaria("Geysa", "12345-6", "Corrente")
conta2 = ContaBancaria("Lucas", "65432-1", "Poupança")

conta1.depositar(1000)
conta1.sacar(200)
conta1.transferir(300, conta2)