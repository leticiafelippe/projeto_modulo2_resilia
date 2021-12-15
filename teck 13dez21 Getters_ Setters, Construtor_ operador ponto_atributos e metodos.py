
# FUNÇÃO ACENDER A LUZ
class Lampada:
    cor = "Amarela"
    acesa = False
    def acener(self):
        if not self.acesa:
            self.acesa = True

# FUNÇÃO APAGAR LUZ

# se if é igual a True ele vai entrar pq a condição é verdadeira.

lampada = Lampada() # estamos instanciando a classe atribuindo ela a uma variável.
print(lampada.acesa)
lampada.acender()
print(lampada.acesa)

# construtor: quando usamos o construtor nós passamos os argumentos bem no início.
class Carro:
    cor = " "
    # construtor
    def __init__(self, rodas, capacidadeTanque):
        self.rodas = rodas
        self.qtdLitrosTanque = capacidadeTanque

# instancia:
carro = Carro("aro 17", 65) # OBS: DEPOIS RETIRAR O VALOR 65 PRA VER O ERRO.
print(carro.qtdLitrosTanque)

# qual a importância de se ter um construtor? Ele é feito pra obrigar que algum dado seja enviado no início. Ex: tenho um sistema que consesrta rodas de carros, neste sistema a cor é um atributo opcional.

# GETTERS: o que é?


                    # ========= PESQUISAR DECORADORES DE MÉTODOS ================




