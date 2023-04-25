#CALCULADORA DE GORGETA

print("Bem Vindo a Calculadora de  Gorgeta!")
conta = float(input("Qual foi o valor da conta? R$"))
gorgeta = int(input("Quanto de Gorgeta você gostaria de dar? 10, 12 ou 15%?  "))
pessoas = int(input("Quantas pessoas dividirão a gorgeta?"))
gorgeta_como_porcentagem = gorgeta / 100
total_da_gorgeta = conta * gorgeta_como_porcentagem
total_conta = conta + total_da_gorgeta
conta_por_pessoa = total_conta / pessoas
conta_a_pagar = round(conta_por_pessoa, 2)
print(f"Cada pessoa deve pagar: R${conta_a_pagar}")
