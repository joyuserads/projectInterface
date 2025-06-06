#imagine que você foi designado para criar um sistema que recebe dimensões de pisos de uma casa e 
# dimensões de azulejos que vão cobrir os pisos.
#Sua missão é mostrar a quantidade de azulejos necessária com base na área do piso e do azulejo escolhido.
#  É evidente que os testes das funcionalidades devem estar em um arquivo à parte.

class Retangulo:
    def _init_(self, lado_a, lado_b):
        self.a= lado_a
        self.b= lado_b

    def muda_valor(self, novo_a, novo_b):
        self.a= novo_a
        self.b= novo_b

    def retorna_lado(self):
        print(f'O retangulo possui dimensões {self.a} m x {self.b}m')

    def area(self):
        return self.a* self.b
    
#Em seguida, é possível fazer um teste simples, com um looping que manterá a janela do executável .py aberta 
# para você testar indefinidamente, observe:
import math 
from area import Retangulo 


while True:
    piso_a= float(input("Digite um lado do piso: "))
    piso_b= float(input ("Digite o outro lado do piso: "))

    piso= Retangulo(piso_a, piso_b)

    az_a= float(input("Digite o lado do azulejo: "))
    az_b= float(input("Digite o outro lado do azulejo"))

    azulejo= Retangulo(az_a, az_b)

    area_piso= piso.area()
    area_az= azulejo.area()

    quantidade_az= area_piso / area_az

    if area_piso% area_az== 0:
        print(f'A quantidade exata de azulejos para preencher o piso é de {quantidade_az}')

    else:
        print(f'A quantidade mínima de azulejos para preencher o piso é de {math .ceil(quantidade_az)}')

   