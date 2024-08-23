import os 
import sys
class encrypt_shift:
    def __init__(self):
        self.key = None
        self.plain_text = None
    def get_key(self,key_path):
        f = open(key_path,"r")
        self.key = f.read()
    def get_plain_text(self,plain_text_path):
        f = open(plain_text_path,"r")
        self.plain_text = f.read()
    def preprocess_data(self):
        fin_text = ""
        for x in self.plain_text:
            if(ord(x.lower()) >= ord('a') and ord(x.lower())<=ord('z')):
                fin_text+=x
            else:
                continue
        self.plain_text = fin_text
    def encrypt_data(self):
        encrypted_cipher = ""
        for x in self.plain_text:
            value = (ord(x.lower())-ord('a')+int(self.key))%(ord('Z')-ord('A')+1)
            # encrypted_cipther+=chr((ord(x.lower())-ord('a')+ord('A')+int(self.key)))
            encrypted_cipher += chr(ord('A')+value)
        return encrypted_cipher
    def write_to_path(self,final_file_path,cipher_text):
        encrypt_cipher_file = "cipher.txt"
        final_path = os.path.join(final_file_path,encrypt_cipher_file)
        f = open(final_path,'a')
        f.write(cipher_text)
        f.close()

if __name__ == "__main__":
    key_path = "/home/comrade/Crypto/shiftcipher/key_shift.txt"
    plain_text_path = "/home/comrade/Crypto/shiftcipher/plain_text.txt"
    final_path = "/home/comrade/Crypto/shiftcipher"
    encryptor = encrypt_shift()
    encryptor.get_plain_text(plain_text_path)
    encryptor.get_key(key_path)
    encryptor.preprocess_data()
    cipher_text = encryptor.encrypt_data()
    encryptor.write_to_path(final_path,cipher_text)
    # print(encryptor.plain_text)
    # print()
    # print(cipher_text)