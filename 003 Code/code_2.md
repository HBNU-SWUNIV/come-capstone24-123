캡스톤디자인2 코드
=================


1. AP 환경 구성
---------------

> /etc/dnsmasq.conf 
>
> ```bash
> 
> 
> ```


> /etc/dhcpcd.conf
>
> ```bash
> 
> 
> ```


> /etc/hostapd/hostapd.conf
>
> ```bash
> 
> 
> ```


> /etc/default/hostapd.conf
>
> ```bash
> 
> 
> ```


> /etc/sysctl.conf
>
> 다음 줄의 주석을 제거
> ```bash
> net.ipv4.ip_forward=1
> ```


> AP 호스트 서비스 시작
>
> ```bash
> sudo systemctl start dnsmasq
> sudo systemctl start dhcpcd
> sudo systemctl start hostapd
> ```


> NAT 설정 추가
>
> ```bash
> sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
> ```





2. mac ~~ 실행
---------------

AP 구성을 완료한 기기에서 사용자 인증을 실행


> ```bash
> sudo python3 -m pip install scapy
> sudo git clone https://github.com/this_github_link_code_files
> cd file_folders
> sudo python3 python_file_name
> ```







[scapy](https://github.com/secdev/scapy)
