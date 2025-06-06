#um segundo chamado teste_funcionario.py,
#  em que você deve aplicar testes e verificar a legitimidade do código anterior.

from funcionario import Funcionario

funcionario= Funcionario("Joyce, joyce@gmail.com")

funcionario.cadastro_hora('Janeiro', 300)
funcionario.cadastro_hora('Fev', 200)
funcionario.cadastro_salario_hora('Jan', 30)
funcionario.cadastro_salario_hora('Fev', 30)
print(funcionario)

print(funcionario.calcula_salario('Jan'))
print(funcionario.calcula_salario('Fev'))

#Exibe
#Funcionario: Joyce Email: joyce@gmail.com / horas/mes: 'Jan:300, Fev:200 / salario-hora: 'Jan: 30, Fev:30' 9000 e 6000

