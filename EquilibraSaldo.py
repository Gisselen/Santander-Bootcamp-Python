saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())


saldo = saldo_atual + valor_deposito - valor_retirada


print(f'Saldo atualizado na conta: {saldo:.1f}')