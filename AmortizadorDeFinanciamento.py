def main():
    print("Qual o valor imovel: ")
    valorImovel = float(input())

    print("Qual o valor mensal das parcelas: ")
    valorMensal = float(input())

    print("Qual o valor disponivel para amortização mensal: ")
    valorAmortizacaoMensal = float(input())

    print("Valor real sem juros: ")
    valorReal = float(input())
    mes = 0
    ano = 0

    valorGasto = 0
    while valorImovel > 0:
        valorImovel -= valorReal + valorAmortizacaoMensal
        valorGasto += valorMensal + valorAmortizacaoMensal
        mes += 1

        if mes > 12:
            ano += 1
            mes = 0

    print("Terminará o financiamento em: {} anos e {} meses".format(ano, mes))
    print("Gasto R$ {}".format(valorGasto))
    

if __name__ == "__main__":
    main()