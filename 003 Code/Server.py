import socket
import threading
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

# 클라이언트의 IP 주소를 이용해 /proc/net/arp 파일에서 MAC 주소 받아오기
def get_mac_address(ip_address):
    try:
        with open('/proc/net/arp') as f:
            for line in f.readlines()[1:]:  # 첫 번째 줄은 헤더
                fields = line.split()
                if fields[0] == ip_address:  # IP 주소 확인
                    return fields[3]  # MAC 주소 반환
        return None
    except Exception as e:
        print(f"Error reading /proc/net/arp: {e}")
        return None

# MAC 주소를 파일로 저장하는 함수
def save_mac_address(mac_address):
    with open("banned_clients_mac.txt", "a") as file:
        file.write(f"{mac_address}\n")

# txt 파일에서 연결 해제된 MAC 주소 읽기
def get_key_by_mac(mac_address):
    try:
        with open("client_mac_addresses.txt", "r") as file:
             lines=file.readlines()
            for line in reversed(lines):
                mac, saved_key = line.strip().split()
                if mac == mac_address:
                    return int(saved_key)  # 숫자로 변환해서 반환
        return None
    except FileNotFoundError:
        return None

# 새로운 MAC 주소와 키를 파일에 저장하는 함수
def save_mac_and_key(mac_address, key):
    with open("client_mac_addresses.txt", "a") as file:
        file.write(f"{mac_address} {key}\n")  # 잘못된 괄호 수정

# 클라이언트와 통신하는 스레드 함수
def threaded(client_socket, addr, key):
    print(f'Connected by: {addr[0]}:{addr[1]}')

    # 클라이언트의 IP 주소를 이용해 MAC 주소를 받아옴
    client_ip = addr[0]
    client_mac = get_mac_address(client_ip)
    if client_mac:
        save_mac_address(client_mac)
        print(f"MAC address {client_mac} saved to file.")
    else:
        print(f"Could not retrieve MAC Address for IP: {client_ip}")
        client_socket.close()
        return  # MAC 주소가 없으면 함수 종료

    # 연결된 MAC 주소의 연결 해제 횟수가 3 이상이면 강제 연결 해제
    mac_count = get_key_by_mac(client_mac)
    if mac_count is not None and mac_count >= 3:  # mac_count가 3 이상이면 차단
        print(f'Banned MAC Address, Disconnect\n')
        client_socket.close()
        return  # 차단된 클라이언트는 함수 종료
    
    while True:
        try:
            # 클라이언트로부터 암호화된 데이터를 수신
            data = client_socket.recv(1024)
            if not data:
                print(f'\nDisconnected by {addr[0]}:{addr[1]}\n')
                break

            # 받은 데이터를 복호화
            try:
                decrypted_message = decrypt_data(key, data)
                print(f"Decrypted message from {addr[0]}:{addr[1]}: {decrypted_message}")
                
                # 응답도 암호화해서 전송
                response = "Message received successfully.".encode()
                encrypted_response = encrypt_data(key, response.decode())
                client_socket.send(encrypted_response)

            except Exception as e:
                print(f"\nDecryption failed: {e}.\n Disconnecting client {addr[0]}:{addr[1]}\n")
                save_mac_and_key(client_mac, mac_count + 1 if mac_count is not None else 1)
                client_socket.close()  # 복호화 실패 시 연결 끊기
                break

        except ConnectionResetError as e:
            print(f"\nDisconnected by {addr[0]}:{addr[1]}\n")
            print(f"\nError: {e}")
            break

# 서버 소켓 설정
ip = '192.168.4.1'
port = 5656

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((ip, port))
server_socket.listen()

# 서버에서 키 입력
password = input("Enter encryption key for server: ")
key = hashlib.sha256(password.encode()).digest()  # 고정된 32바이트 길이의 키 생성

print('Server started and listening')

while True:
    client_socket, addr = server_socket.accept()
    
    # 새로운 클라이언트를 위한 스레드 생성
    thread = threading.Thread(target=threaded, args=(client_socket, addr, key))
    thread.start()
