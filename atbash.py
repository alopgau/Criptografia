def pedir_alfabeto() -> str:
    return input("Introduce el alfabeto en el que basaras la encriptación\n").lower()
def crear_diccionarios(alfabeto:str) -> dict[str,str]:
    diccionario_encriptación = {}
    diccionario_desencriptación = {}
    if " " not in alfabeto:
        diccionario_encriptación.setdefault(" ", " ")
        diccionario_desencriptación.setdefault(" ", " ")

    for i in range(len(alfabeto)):
        diccionario_encriptación.setdefault(alfabeto[i], alfabeto[len(alfabeto)-1-i])
        diccionario_desencriptación.setdefault(alfabeto[len(alfabeto)-1-i], alfabeto[i])
    return diccionario_encriptación
def pedir_textos() -> None:
    entrada = ""
    while entrada != "x":
        entrada = input("Introduce el texto a encriptar (X para salir)\n").lower()
        texto_encriptado = ""
        for c in entrada:
            texto_encriptado += diccionario_encriptación[c].upper()
        mostrar_encriptación(entrada,texto_encriptado)

def mostrar_encriptación(original:str,encriptado:str) -> None:
    print(f"Texto original: {original}\nTexto encriptado: {encriptado}")

def main():
 alfabeto = pedir_alfabeto()
 diccionario = crear_diccionario(alfabeto)
 pedir_textos()



if __name__ == "__main__":
    main()