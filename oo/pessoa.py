class Pessoa:
    olhos = 2
    pernas = 2
    bracos = 2

    def __init__(self, *filhos, nome = None, idade = None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        return "olá, sou uma pessoa"

    def _acenar(self):
        pass

    @staticmethod
    def metodo_estatico(a,b):
        return a+b
    
    @classmethod
    def metodo_de_classe(cls):
        return cls.olhos + cls.pernas 

class Homem(Pessoa):

    def cumprimentar(self):
        return f'{super().cumprimentar()} do sexo masculino' #Uso o super quando quero usar um comportamento da classe Pai sem alterá-lo


if __name__ == "__main__":
    print("oi")
    renzo = Pessoa(nome = "Renzo")
    lucas = Pessoa(nome = "Lucas")
    luciano = Pessoa(renzo,lucas,nome = "Luciano")
    print(luciano.metodo_estatico(1,2))
    print(luciano.metodo_de_classe())
    print(Pessoa.metodo_de_classe())
    Diego = Homem()
    print(Diego.cumprimentar())
