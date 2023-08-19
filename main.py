from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

with open(".\\testes\\KeySecrets.key", "bw") as file_key:
    file_key.write(key)

msg = input()

crypt = fernet.encrypt(msg.encode())

with open(".\\testes\\crypt.txt", "bw") as file_crypt:
    file_crypt.write(crypt)
    
if __name__ == "__main__":
    print(crypt)