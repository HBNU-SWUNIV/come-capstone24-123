캡스톤디자인2 코드
=================


1. 서버 AP 환경 구성
---------------

> sh 파일들을 실행해 필요한 패키지들을 설치하고, 시스템 설정을 변경한다.
>
> ```bash
> sh ./install_packages.sh
> sh ./AP_set.sh
> ```


> 라우터 설정에 변경이 필요하지 않으면 라우터 설정이 없는 sh 파일을 실행한다.
>
> ```bash
> sh ./AP_set_no_router.sh
> ```


> 이더넷과 무선랜 간의 포트포워딩이 필요하다면 설정한다.
>
> ```bash
> sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
> ```





2. 서버와 클라이언트 실행
---------------

AP 구성을 완료한 서버와 각각의 클라이언트 기기에서 실행한다.


> 서버
> 
> ```bash
> sudo python3 Server.py
> ```


> 클라이언트
> 
> ```bash
> sudo python3 Client.py
> ```


ip와 포트 구성이 다르다면 각 실행 파일들을 수정해 설정한다.  
연결이 해제된 클라이언트들의 MAC 주소는 서버 기기의 client_mac_addresses.txt 파일에 저장된다.




[scapy](https://github.com/secdev/scapy)
[cryptography](https://cryptography.io/en/latest/)
