class ArrayList:
    def __init__(self):
        self.LEN = 5
        self.arrayList = [None] * self.LEN
        self.insertPosition = 0
        
    def insert(self, data):
        if self.isMemoryFull():
            self.increaseMemory()
        self.arrayList[self.insertPosition] = data
        self.insertPosition += 1
            
    def remove(self):
        if self.isEmpty():
            print("Erro: A lista está vazia.")
            return None
        self.insertPosition -= 1
        removido = self.arrayList[self.insertPosition]
        self.arrayList[self.insertPosition] = None 
        return removido

    def isEmpty(self):
        return self.insertPosition == 0
        
    def isMemoryFull(self):
        return self.insertPosition == len(self.arrayList)
    
    def increaseMemory(self):
        newArray = [None] * ( 2 * len(self.arrayList) )
        self.copyElements(newArray, self.arrayList)
        self.arrayList = newArray
        
    def copyElements(self, newArray, oldArray):
        for position in range(self.insertPosition):
            newArray[position] = oldArray[position]
            
    def print(self):
        if self.isEmpty():
            print("A fila está vazia.")
            return
        for position in range(self.insertPosition):
            print(f"{position + 1}º da fila: {self.arrayList[position]}")
    
    def insertAt(self, data, position):
        if position < 0 or position > self.insertPosition:
            print("Erro, posição não existe")
            return
        if self.isMemoryFull():
            self.increaseMemory()
        
        for i in range(self.insertPosition, position, -1):
            self.arrayList[i] = self.arrayList[i - 1]
            
        self.arrayList[position] = data
        self.insertPosition += 1
        
    def removeAt(self, position):
        if position < 0 or position >= self.insertPosition:
            print("Erro, posição não existe")
            return None
        
        removido = self.arrayList[position]
        
        for i in range(position, self.insertPosition - 1):
            self.arrayList[i] = self.arrayList[i + 1]
            
        self.insertPosition -= 1
        self.arrayList[self.insertPosition] = None
        return removido

def sistema_fila():
    fila = ArrayList()
    
    while True:
        print("FILA DE ATENDIMENTO ")
        print("1. Cadastrar paciente normal")
        print("2. Cadastrar paciente PRIORITÁRIO")
        print("3. Chamar próximo paciente")
        print("4. Mostrar fila de espera")

        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == '1':
            nome = input("Nome do paciente: ")
            fila.insert(nome)
            print(f" {nome} entrou no final da fila.")
            
        elif opcao == '2':
            nome = input("Nome do paciente prioritário: ")
            fila.insertAt(f"[PRIORIDADE] {nome}", 0)
            print(f" {nome} foi colocado no início da fila!")
            
        elif opcao == '3':
            if fila.isEmpty():
                print(" Não há ninguém na fila no momento.")
            else:
                proximo = fila.removeAt(0)
                print(f" CHAMANDO PARA O CONSULTÓRIO: {proximo}")
                
        elif opcao == '4':
            print("\n FILA ATUAL:")
            fila.print()
            
        else:
            print("ERRO. Tente novamente.")

sistema_fila()