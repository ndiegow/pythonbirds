class Pessoa:

    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade


    def cumprimentar(self):
        print("olá")

if __name__ == "__main__":
    p = Pessoa("Diego")
    p.cumprimentar()
    print(p.nome)


