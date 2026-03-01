def pedir_alfabeto() -> str:
    return input("Introduce el alfabeto en el que basaras la encriptación\n").lower()
def crear_diccionario(alfabeto:str) -> dict[str,str]:
    diccionario = {" ":" "}
    for i in range(len(alfabeto)):
        diccionario.setdefault(alfabeto[i], alfabeto[len(alfabeto)-1-i])
    return diccionario
def pedir_textos(diccionario: dict[str,str]) -> None:
    entrada = ""
    while entrada != "X":
        entrada = input("Introduce el texto a encriptar (X para salir)\n").lower()
        texto_encriptado = ""
        for c in entrada:
            texto_encriptado += diccionario[c].upper()
        mostrar_encriptación(entrada,texto_encriptado)

def mostrar_encriptación(original:str,encriptado:str) -> None:
    print(f"Texto original: {original}\nTexto encriptado: {encriptado}")

def main():
 alfabeto = pedir_alfabeto()
 diccionario = crear_diccionario(alfabeto)
 pedir_textos(diccionario)



if __name__ == "__main__":
    main()