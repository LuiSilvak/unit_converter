# Conversor de Unidades

def conversor_de_unidades():
    print("=== Conversor de Unidades de Medida ===")
    print("Escolha o tipo de conversão: ")
    print("1. Metros para Quilômetros")
    print("2. Quilômetros para Metros")
    print("3. Gramas para Quilogramas")
    print("4. Quilogramas para Gramas")
    print("5. Celsius para Fahrenheit")
    print("6. Fahrenheit para Celsius")

    escolha = input("Digite o número da conversão desejada (1-6): ")

    if escolha not in {"1", "2", "3", "4", "5", "6"}:
        print("Opção inválida. Tente novamente. ")
        return
    
    try:
        valor = float(input("Digite o valor a ser convertido: "))
    except ValueError:
        print("Entrada inválida. Insira um número válido.")
        return
    
    if escolha == "1":
        resultado = valor / 1000
        print(f"{valor} metros equivalem a {resultado:.2f} quilômetros.")
    elif escolha == "2":
        resultado = valor * 1000
        print(f"{valor} quilômetros equivalem a {resultado:.2f} metros.")
    elif escolha == "3":
        resultado = valor / 1000
        print(f"{valor} gramas equivalem a {resultado:.2f} quilogramas.")
    elif escolha == "4":
        resultado = valor * 1000
        print(f"{valor} quilogramas equivalem a {resultado:.2f} gramas.")
    elif escolha == "5":
        resultado = (valor * 9/5) + 32
        print(f"{valor} graus Celsius equivalem a {resultado:.2f} graus Fahrenheit.")
    elif escolha == "6":
        resultado = (valor - 32) * 5/9
        print(f"{valor} graus Fahrenheit equivalem a {resultado:.2f} graus Celsius.")

if __name__ == "__main__":
    conversor_de_unidades()