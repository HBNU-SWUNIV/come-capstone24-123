# 한밭대학교 컴퓨터공학과 낚이지마팀
## 인증과 암호화 드론 통신 프로토콜, AES를 곁들인
## 팀 구성
- 20211870 김슬기 
- 20191759 홍준기
- 20201773 손성호

## <u>Teamate</u> Project Background
- ### 개요
  <div style="display: flex; gap: 10px;">
    <img src="https://github.com/user-attachments/assets/ac61d5a5-96ec-4b94-8fcf-86c141169574" width="30%">
    <img src="https://github.com/user-attachments/assets/131915d7-a370-45cf-a2b7-cd95da88f433" width="40%">
  </div>

  - 무선 네트워크는 전파를 통신매개로 이용한다는 특성이 있어 유선랜에 비해 보안이 취약함
  - 그 중, 와이파이는 위성통신이나 셀룰러 통신에 비해 보안성이 취약하다는 단점이 있음
  - 현재 와이파이 산업의 규모는 늘어나고 있고, 와이파이를 이용하는 드론 또한 늘어나는 추세임
  - 와이파이를 연결해서 운용하는 드론은 패킷 스니핑, 인증해제 공격과 더불어 하이재킹의 위험성이 있음
  - 따라서, 인증해제 공격과 GPS 스푸핑 공격을 진행하여 취약점을 분석하고 보안 통신 프로토콜을 제작함
- ### 기존 해결책의 문제점
  - Wi-Fi 기반 드론의 보안이 Wi-Fi의 비밀번호에 의존
  - 컨트롤러와 드론 간의 패킷에서 명령어 등이 쉽게 유출됨
  
## System Design
  - ### System Requirements
    ### 캡스톤디자인I
    - 무선 LAN카드가 탑재된 Kali Linux OS의 PC
    - Hack-RF One
   
    ### 캡스톤디자인II
    - ubuntu/Linux OS 기반 소형 PC를 탑재한 드론
    - Python 파일 실행, 문자열 입력이 가능한 드론 컨트롤러
    
## Case Study
  - ### Description

    ### - Deauth Attack
    <img src="https://github.com/user-attachments/assets/3ddb8596-0f8b-4047-a531-4c9264b34283" alt="Picture3" width="500px">
    
    - 공격자가 목표 드론의 AP에 연결되어있는 기기들에 대해 Deauth 패킷을 전송하면 해당 기기들의 AP 접속이 해제되고 공격자가 드론의 제어권을 탈취 가능하다.
    - 드론의 AP에서 임의의 접근에 대한 추가적인 방어책이 필요하다.
      
    ### - GPS Spoofing
    <img src="https://github.com/user-attachments/assets/be3dbc02-67f1-4167-973d-485074ae9499" alt="Picture4" width="500px">
    <div style="display: flex; justify-content: center; gap: 10px;">
        <img src="https://github.com/user-attachments/assets/ad8a9ac8-9e9b-43d2-a86a-b52d9f5c1f50" alt="Picture6" width="400px">
        <img src="https://github.com/user-attachments/assets/aa1d034f-834b-49bd-85b4-f17dede9cc35" alt="Picture7" width="400px">
    </div>

    - 위조된 경도, 위도 파일의 신호를 생성한다.
    - 생성된 파일을 HackRF로 위조된 신호를 생성하여 GPS 모듈에 전송하면 위조된 위치로 값이 변경된다.
            
    ### - Security Manager Protocol
    <img src="https://github.com/user-attachments/assets/13532ae0-e1b2-4468-b79c-b754dc3e1e9e" alt="Picture5" width="500px">
    <img src="https://github.com/user-attachments/assets/50672f87-b6ff-4905-bb1e-abcfacae5a70" alt="Picture8" width="500px">
    
    - 서버가 AP에 연결된 클라이언트의 명령어 정보를 받으며 암·복호화 KEY를 확인한다.
    - 이때, KEY가 같으면 정상적인 작동이 이루어지지만 KEY가 다를 경우 명령이 거부되고, 3번 이상 틀린 클라이언트 기기의 MAC 주소는 Ban-list에 추가되어 연결이 제한된다.
    - 서버의 KEY는 매 실행시에 새롭게 설정되어 드론의 소유주가 아니면 알 수 없다.
    - 위 과정에서 서버와 클라이언트 사이에 전송되는 명령은 AES 방식으로 암호화되어 패킷 유출에 대응한다.

  
## Conclusion
  - 인증해제, GPS 스푸핑 공격을 통해 무선 통신의 취약점을 분석한 뒤, 이를 보완한 통신 프로토콜을 만듬
  - 드론 사용자를 MAC 주소로 분류하고 2차 인증을 통해 악성 이용자 사전 차단 및 드론의 하이재킹을 방지함
  - 드론 구동시에 설정한 키를 통해 패킷을 암·복호화하여 패킷 스니핑을 사전에 방지함
  
## Project Outcome
- ### KICS 한국통신학회, 2024 하계종합학술발표회
  📗 사이버 보안 위협에 따른 해킹 기법과 대응 방안 조사
  
  📘 와이파이 기반 드론 네트워크에서 드론 제어장치 식별에 관한 연구
  
  📙 와이파이 기반 드론 네트워크의 보안 취약점 분석 및 대응방안
