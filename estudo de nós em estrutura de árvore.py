class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        if (self.isEmpty()):
            self.root = newNode
            return
        self.insertRecursive(self.root, newNode)

    #retorna verdadeiro se a árvore estiver vazia, caso contrário, retorna falso
    def isEmpty(self):
        return self.root == None

    def insertRecursive(self, currentNode, newNode):
        #verifica se o novo nó é menor que o nó atual, se sim, insere à esquerda
        if newNode.data < currentNode.data:
            if currentNode.left is None:
                currentNode.left = newNode
            else:
                self.insertRecursive(currentNode.left, newNode)
        #verifica se o novo nó é maior que o nó atual, se sim, insere à direita
        if newNode.data > currentNode.data:
            if currentNode.right is None:
                currentNode.right = newNode
            else:
                self.insertRecursive(currentNode.right, newNode)

    def printPostOrder(self, node):
        if node:
            self.printPostOrder(node.left)
            self.printPostOrder(node.right)
            print(node.data)

    def printInOrder(self, node):
        if node:
            self.printInOrder(node.left)
            print(node.data)
            self.printInOrder(node.right)

    def printPreOrder(self, node):
        if node:
            print(node.data)
            self.printPreOrder(node.left)
            self.printPreOrder(node.right)

tree = BinaryTree()
tree.insert(10)
tree.insert(20)
tree.insert(5)
tree.insert(1)
print(tree.root.data)
print(tree.root.left.data)
print(tree.root.right.data)
print(tree.isEmpty())
print("Post-order:")
tree.printPostOrder(tree.root)
print("In-order:")
tree.printInOrder(tree.root)
print("Pre-order:")
tree.printPreOrder(tree.root)
