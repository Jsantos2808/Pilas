# Nodo individual de la pila
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Clase Stack (Pila) sin usar estructuras predefinidas
class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop desde pila vacía")
        value = self.top.value
        self.top = self.top.next
        self.count -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek desde pila vacía")
        return self.top.value

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.count

# -----------------------------------------
# Validación de paréntesis
def parentesis_balanceados(expresion):
    pila = Stack()
    for caracter in expresion:
        if caracter == '(':
            pila.push(caracter)
        elif caracter == ')':
            if pila.is_empty():
                return False
            pila.pop()
    return pila.is_empty()

# -----------------------------------------
# Conversión de infijo a postfijo
def prioridad(op):
    prioridades = {'+': 1, '-': 1, '*': 2, '/': 2}
    return prioridades.get(op, 0)

def infijo_a_postfijo(expresion):
    pila = Stack()
    salida = []
    tokens = expresion.split()

    for token in tokens:
        if token.isnumeric():
            salida.append(token)
        elif token == '(':
            pila.push(token)
        elif token == ')':
            while not pila.is_empty() and pila.peek() != '(':
                salida.append(pila.pop())
            if not pila.is_empty():
                pila.pop()  # eliminar el '('
        else:  # operador
            while not pila.is_empty() and prioridad(pila.peek()) >= prioridad(token):
                salida.append(pila.pop())
            pila.push(token)

    while not pila.is_empty():
        salida.append(pila.pop())

    return ' '.join(salida)

# -----------------------------------------
# Interfaz interactiva
def menu():
    print("\n=== MANEJO DE EXPRESIONES MATEMÁTICAS ===")
    print("1. Validar paréntesis")
    print("2. Convertir expresión infija a postfija")
    print("3. Salir")

def main():
    while True:
        menu()
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == '1':
            expr = input("Ingresa la expresión matemática: ")
            if parentesis_balanceados(expr):
                print("✅ Los paréntesis están balanceados.")
            else:
                print("❌ Los paréntesis NO están balanceados.")
        
        elif opcion == '2':
            expr = input("Ingresa la expresión en notación infija (usa espacios entre los elementos):\nEjemplo: 3 + 5 * ( 2 - 8 )\n> ")
            postfijo = infijo_a_postfijo(expr)
            print("Expresión postfija:", postfijo)

        elif opcion == '3':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar programa
if __name__ == "__main__":
    main()
