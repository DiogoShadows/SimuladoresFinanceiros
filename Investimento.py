def main():
    print("Qual valor deseja alcançar: ")
    valorDesejado = float(input())

    print("Qual o valor mensal que irá depositar: ")
    valorMensal = float(input())

    print("Qual a taxa anual do investimento: ")
    taxaAnual = float(input())

    taxaMensal = taxaAnual / 12

    valorAtual = 0.0
    mes = 0
    ano = 0
    while valorAtual < valorDesejado:
        valorAtual += valorAtual * taxaMensal / 100
        valorAtual += valorMensal

        mes += 1

        if mes > 12:
            ano += 1
            mes = 0

    print("Chegará ao valor R$ {} em: {} anos e {} meses".format(valorDesejado, ano, mes))
    

if __name__ == "__main__":
    main()