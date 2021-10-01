"docstring"
from numero_natural import multiplos

class TesteNumeroNatural:
    """
    docstring
    """
    def setup(self):
        "docstring"

    def test_multiplos(self):
        "docstring"
        while True:
            try:
                natural = int(input(EVITAR_72_COLUNAS))
                if natural == 0:
                    natural = int("")
            except ValueError:
                print(EVITAR_72_COLUNAS_2)
                break
            resultados = multiplos(natural)
            assert resultados == natural
            break

EVITAR_72_COLUNAS = "Digite um número natural diferente de zero: "
EVITAR_72_COLUNAS_2 = """!!!Algo errado!!!
Você digitou um número zero, não natural ou uma string!!!"""
chama_classe = TesteNumeroNatural()
chama_classe.test_multiplos()
