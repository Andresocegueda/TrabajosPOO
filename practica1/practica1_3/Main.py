import Calculadora

def main():
    print("""Esto es una calculadora
Escriba un número""")
    num1 = int(input())
    print("Escriba otro número")
    num2 = int(input())
    calc = Calculadora.calculadora(num1, num2)
    print(f"""La suma de {num1} y {num2} es {calc.suma()}
La resta de {num1} y {num2} es {calc.resta()}
La multiplicación de {num1} y {num2} es {calc.multiplicacion()}
La división de {num1} y {num2} es {calc.division()}""")
    
if __name__ == "__main__":
   main()