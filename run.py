import time
from keyCreator import geradorDeChave, leitorDeChave
from encryption import encryptorFunction, decryptorFunction


def main():
    chave_usuario = inputUsuarioChave()
    if chave_usuario:
        inputUsuarioEncryption(chave_usuario)


def inputUsuarioChave():
    while True:
        escolha = input("Gerar nova chave? (s/n) \n" "Atenção, criar uma nova chave irá sobrepor a última.\n" ).lower()

        if escolha == 's':
            print("Criando chave")
            time.sleep(0.5)
            chave_usuario = geradorDeChave()
            return chave_usuario

        if escolha == 'n':
            print("A chave não foi criada...")
            time.sleep(0.5)
            print("Procurando/lendo chave")
            time.sleep(0.5)
            chave_usuario = leitorDeChave()
            if chave_usuario:
                return chave_usuario
            continue

        print("Input incorreto")

def inputUsuarioEncryption(chave_usuario):
    while True:
        escolha = input("Você deseja encriptar (1) ou desencriptar (2) um arquivo? Se desejar sair digite 'sair': \n").lower()

        if escolha == '1':
            print("Encriptar arquivo...")
            time.sleep(0.5)
            encryptorFunction(chave_usuario)
            time.sleep(0.5)
            continue
        
        if escolha == '2':
            print("Desencriptar arquivo...")
            time.sleep(0.5)
            decryptorFunction(chave_usuario)
            time.sleep(0.5)
            continue

        if escolha == 'sair':
            print("Fechando o programa...")
            time.sleep(0.5)
            break
        
        print("Input incorreto")

if __name__ == "__main__":
    main()