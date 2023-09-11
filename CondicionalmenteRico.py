saldo_total = int(input())
valor_saque = int(input())

if valor_saque <= saldo_total:
    saldo_total -= valor_saque
    print("Saque realizado com sucesso. Novo saldo:", saldo_total)
else:
    print("Saldo insuficiente. Saque nao realizado!")