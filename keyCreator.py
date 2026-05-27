from cryptography.fernet import Fernet


def geradorDeChave():
    chave_usuario = Fernet.generate_key()
    with open('chave.key', 'wb') as f:
        f.write(chave_usuario)
    return chave_usuario

def leitorDeChave():
    try:
        with open('chave.key', 'rb') as f:
            chave_usuario = f.read()
        return chave_usuario
    except FileNotFoundError:
        print("Chave não encontrada")