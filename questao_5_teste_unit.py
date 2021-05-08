#importação das bibliotecas
import unittest
from questao_5_arvore import BSTNode

#Gerar a árvore
tree = BSTNode(0)
for i in range(1, 50):
    tree.add(i)

#Módulo de teste
class MyTest(unittest.TestCase):

    'Testar se ao chamar a função get, passando o número 4 como parâmetro'
    'irá se ser retornado o mesmo valor'
    def test_1(self):
        self.assertEqual(tree.get(4).key, 4)
        
    'Testar se ao chamar a função _max() o maior da árvore será 49'    
    def test_2(self):
        self.assertEqual(tree._max().key, 49)
        
    'Testar se ao chamar a função search, ela não encontrará um nó com o valor de 80'    
    def test_3(self):
        self.assertEqual(tree.search(80),"Valor não encontrado")
        
if __name__ == '__main__':
    unittest.main()
