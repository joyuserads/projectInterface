from funcionalidade import Televisor
from funcionalidade import ControleRemoto



tv = Televisor("Sony", "Sony-123")

controle= ControleRemoto(tv)

controle.sintonizaCanal("SBT")
controle.trocaCanal("SBT")

print(tv.canal_atual)

