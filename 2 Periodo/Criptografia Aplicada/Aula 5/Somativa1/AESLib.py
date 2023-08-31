
# Ver https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import b64encode, b64decode
import os

# Isso é a declaração de um tipo customizado
#base64: TypeAlias = bytes

# Cripografa com AES, assume que plaintext é uma string
def cifraMensagem(plaintext : str, key : bytes):
    cipher = Cipher(algorithms.AES(key), modes.ECB())     
    cifrador = cipher.encryptor()
    plainbytes = plaintext.encode()
    
    padder = padding.PKCS7(128).padder()
    plainbytes = padder.update(plainbytes) + padder.finalize()
    
    cipherbytes = cifrador.update(plainbytes) + cifrador.finalize()
    ciphertext = b64encode(cipherbytes)   
    return ciphertext

# Cripografa com AES, assume que ciphertext é uma base64 (bytes)
def decifraMensagem(ciphertext, key : bytes) -> str :    
    cipher = Cipher(algorithms.AES(key), modes.ECB()) 
    decifrador = cipher.decryptor()
    cipherbytes = b64decode(ciphertext)

    plainbytes = decifrador.update(cipherbytes) + decifrador.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plainbytes = unpadder.update(plainbytes) + unpadder.finalize()

    plaintext = plainbytes.decode()
    return plaintext

# Gera chave simétrica
def geraChave(tamanho : int):
    embytes = int(tamanho/8)
    chave = os.urandom(embytes)
    chavePEM = b64encode(chave)
    return chave, chavePEM


# Use essa porção do código para testar as funções da biblioteca

if __name__ == "__main__":
   
    # Gera a chave secreta randômica (chave de sessão)
    chavesecreta, chavePEM = geraChave(128)
    print(type(chavePEM), chavePEM)

    # Criptografa uma mensagem com a chave secreta
    plaintext = 'isto é um teste de qualquer tamanho'
    ciphertext = cifraMensagem(plaintext, chavesecreta)   
    print(type(ciphertext), ciphertext)

    # Descriptografa uma mensagem com a chave secreta
    plaintext2 = decifraMensagem(ciphertext, chavesecreta)
    print(type(plaintext2), plaintext2)
