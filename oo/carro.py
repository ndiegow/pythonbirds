class Motor:
    def __init__(self):
        self.velocidade = 0
    
    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade-=1


class Direcao:
    
    def __init__(self):
        self.direcao = 'N'

    def girar_a_esquerda(self):
        if self.direcao == 'N': self.direcao = 'O'
        elif self.direcao == 'O': self.direcao = 'S'
        elif self.direcao == 'S': self.direcao = 'L'
        elif self.direcao == 'L': self.direcao = 'N'
        
    def girar_a_direita(self):
        if self.direcao == 'N': self.direcao = 'L'
        elif self.direcao == 'L': self.direcao = 'S'
        elif self.direcao == 'S': self.direcao = 'O'
        elif self.direcao == 'O': self.direcao = 'N'

class Carro:

    def __init__(self,direcao, motor):
        self.direcao = direcao
        self.motor = motor
    
    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()
    
    def frear(self):
        self.motor.frear()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()



if __name__ == "__main__":
    V8 = Motor()
    dir = Direcao()
    ferrari = Carro(dir,V8)
    ferrari.acelerar()
    print(ferrari.calcular_velocidade())
    ferrari.acelerar()
    print(ferrari.calcular_velocidade())
    




