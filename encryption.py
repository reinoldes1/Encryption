from cryptography.fernet import Fernet
import time


def encryptorFunction(chave_usuario):
    try:
        file = input("Nomeie o arquivo que deseja encriptar (aperte enter para continuar): ")
        if file != '':
            with open (file, 'rb') as f:
                data = f.read()
            fernet = Fernet(chave_usuario)
            encrypted = fernet.encrypt(data)
            new_file = file[:-4] + '_encrypted' + file[-4:]
            with open(new_file, 'wb') as f:
                f.write(encrypted)
    
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        time.sleep(0.5)
    
    except Exception as e:
        print("Erro ao encriptar o arquivo.")
        time.sleep(0.5)

def decryptorFunction(chave_usuario):
    try:
        file = input("Nomeie o arquivo que deseja desencriptar (aperte enter para continuar): ")
        if file != '':
            with open(file, 'rb') as f:
                data = f.read()
            fernet = Fernet(chave_usuario)
            decrypted = fernet.decrypt(data)
            new_file = file[:-4] + '_decrypted' + file[-4:]
            with open(new_file, 'wb') as f:
                f.write(decrypted)
    
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        time.sleep(0.5)

    except Exception as e:
        print("Erro ao desencriptar o arquivo.")
        time.sleep(0.5)