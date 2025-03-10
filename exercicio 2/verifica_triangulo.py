def verificar_triangulo(lado1, lado2, lado3):
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        return True
    else:
        return False

def main():
    lado1 = float(input("Digite o valor do primeiro lado: "))
    lado2 = float(inp
