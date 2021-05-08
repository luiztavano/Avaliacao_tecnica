class BSTNode(object):
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
    #método para verificar se um valor está presente na árvore
    def get(self, key):
        if self.key == key:
            return self
        node = self.left if key < self.key else self.right
        if node is not None:
            return node.get(key)
        
    #Método para adicionar um novo nó na árvore
    def add(self, key):
    
        side = 'left' if key < self.key else 'right'
        node = getattr(self, side)
        if node is None:
            setattr(self, side, BSTNode(key))
        else:
            node.add(key)
            
    #Método para retornar o menor valor de um nó presente na árvore
    def _min(self):
        if self.left is None:
            return self
        else:
            return self.left._min()
        
    #Método para retornar o maior valor de um nó presente na árvore 
    def _max(self):
        if self.right is None:
            return self
        else:
            return self.right._max()

    def search(self, key):
        found = tree.get(key)
        if found:
            return "Valor presente"
        else:
            return "Valor não encontrado"
        
        
tree = BSTNode(0)
for i in range(1, 10):
    tree.add(i)

found = tree.get(15)
if found:
    print(found.key)
else:
    print("não encontrado")
    
resultado = tree.search(9)
    
# min = tree._max()
# print(min.key)