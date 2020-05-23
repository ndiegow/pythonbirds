class Pessoa:

    def __init__(self, *filhos, nome = None, idade = None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        print("olá")

if __name__ == "__main__":
    print("oi")
    renzo = Pessoa(nome = "Renzo")
    lucas = Pessoa(nome = "Lucas")
    luciano = Pessoa(renzo,lucas,nome = "Luciano")

    for filho in luciano.filhos:
        print(filho.nome)




