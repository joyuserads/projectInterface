# Foi solicitado à você uma classe Funcionário, cujos atributos são: nome e e-mail.
# Deve-se guardar as horas trabalhadas em um dicionário, cujas chaves são o mês em questão e,
# em outro dicionário, guardar o salário por hora relativo ao mês em questão.

class Funcionario: 
    #Classe funcionario criada com atributos nome e email guardando as horas trabalhadas 
    def _init_(self,nome,email):
        self.nome= nome
        self.email= email
        self.horas= {}
        self.salario_hora= {}
    
    def cadastro_hora(self,mes,horas):
        if (mes not in self.horas):
            self.horas[mes] = horas

    def cadastro_salario_hora(self, mes, valor):
     if (mes not in self.salario_hora):
         self.salario_hora[mes] = valor

    def calcula_salario(self, mes):
        if(mes not in self.horas) or (mes not in self.salario_hora):
            print('Mês Inexistente!!')
        else:
            return self.horas[mes] * self.salario_hora[mes]
        
    def __repr__(self):
        return f'Funcionário:  {self.nome}, \nEmail: {self.email}, \nhoras/mês: {self.horas}, \nsalario-hora: {self.salario_hora}'
        