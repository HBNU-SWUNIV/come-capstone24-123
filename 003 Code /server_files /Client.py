import socket
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# AES 암호화 함수
def encrypt_data(key, plaintext):
    iv = os.urandom(16)  # 16바이트 IV (초기화 벡터) 생성
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return iv + ciphertext  # IV를 함께 전송해야 복호화할 때 사용할 수 있음

# AES 복호화 함수
def decrypt_data(key, ciphertext):
    iv = ciphertext[:16]  # 처음 16바이트는 IV
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext[16:]) + decryptor.finalize()
    return plaintext.decode()

# 서버에 연결
server_ip = '192.168.4.1'
server_port = 5656

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# 클라이언트에서 키 입력
password = input("Enter encryption key for client: ")
key = hashlib.sha256(password.encode()).digest()  # 고정된 32바이트 길이의 키 생성

try:
    while True:
        # 사용자 입력을 받아서 암호화한 후 전송
        message = input("Enter message to send (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break

        # 메시지를 AES로 암호화하고 서버로 전송
        encrypted_message = encrypt_data(key, message)
        client_socket.send(encrypted_message)

        # 서버로부터 암호화된 응답을 수신
        response = client_socket.recv(1024)

        # 응답 복호화
        decrypted_response = decrypt_data(key, response)
        print(f"Server response: {decrypted_response}")

finally:
    client_socket.close()
