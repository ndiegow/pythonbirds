class Pessoa:
    olhos = 2
    pernas = 2
    bracos = 2

    def __init__(self, *filhos, nome = None, idade = None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        print("olá")

    def _acenar():
        pass

    @staticmethod
    def metodo_estatico(a,b):
        return a+b
    
    @classmethod
    def metodo_de_classe(cls):
        return cls.olhos + cls.pernas 


if __name__ == "__main__":
    print("oi")
    renzo = Pessoa(nome = "Renzo")
    lucas = Pessoa(nome = "Lucas")
    luciano = Pessoa(renzo,lucas,nome = "Luciano")
    print(luciano.metodo_estatico(1,2))
    print(luciano.metodo_de_classe())
    print(Pessoa.metodo_de_classe())


    for filho in luciano.filhos:
        print(filho.nome)
        print(filho.olhos)


class Opcao:
    def __init__(self):
        self.premio = premio
        self.vencimento = vencimento
        self.ativo = None
        self.vencimento = None






