import os 
import sys
class decrypt_shift:
    def __init__(self):
        self.key = None
        self.cipher_text = None
    def get_key(self,key_path):
        f = open(key_path,"r")
        self.key = f.read()
    def get_cipher_text(self,cipher_text_path):
        f = open(cipher_text_path,"r")
        self.cipher_text = f.read()
    def decrypt_data(self):
        decrypted_message = ""
        for x in self.cipher_text:
            value = (ord(x)-ord('A')-int(self.key))%(26)
            decrypted_message+=chr(ord('a')+value)
        return decrypted_message
    def write_to_path(self,final_file,decrypted_message):
        decrypt_cipher_file = "decrypt.txt"
        final_path = os.path.join(final_file,decrypt_cipher_file)
        f = open(final_path,'a')
        f.write(decrypted_message)
        f.close()
if __name__ == "__main__":
    key_path = "/home/comrade/Crypto/shiftcipher/key_shift.txt"
    cipher_text_path = "/home/comrade/Crypto/shiftcipher/cipher.txt"
    final_path = "/home/comrade/Crypto/shiftcipher"
    decryptor = decrypt_shift()
    decryptor.get_cipher_text(cipher_text_path)
    decryptor.get_key(key_path)
    decrypted_message = decryptor.decrypt_data()
    decryptor.write_to_path(final_path,decrypted_message)
