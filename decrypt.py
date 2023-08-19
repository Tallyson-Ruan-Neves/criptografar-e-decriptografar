from cryptography.fernet import Fernet

with open(".\\testes\\KeySecrets.key", "br") as file_key:
    key = file_key.read()

with open(".\\testes\\crypt.txt", "br") as file_crypt:
    crypt = file_crypt.read()

fernet = Fernet(key)
msg = fernet.decrypt(crypt.decode())
if __name__ == "__main__":
    print(msg)