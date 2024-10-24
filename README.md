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
  - <img src="https://github.com/user-attachments/assets/3ddb8596-0f8b-4047-a531-4c9264b34283" alt="Picture3" width="300px">


  
  
## Conclusion
  - 인증해제, GPS 스푸핑 공격을 통해 무선 통신의 취약점을 분석한 뒤, 이를 보완한 통신 프로토콜을 만듬
  - 드론 사용자를 MAC 주소로 분류하고 2차 인증을 통해 악성 이용자 사전 차단 및 드론의 하이재킹을 방지함
  - 드론 구동시에 설정한 키를 통해 패킷을 암·복호화하여 패킷 스니핑을 사전에 방지함
  
## Project Outcome
- ### KICS 한국통신학회, 2024 하계종합학술발표회
  📗 사이버 보안 위협에 따른 해킹 기법과 대응 방안 조사
  
  📘 와이파이 기반 드론 네트워크에서 드론 제어장치 식별에 관한 연구
  
  📙 와이파이 기반 드론 네트워크의 보안 취약점 분석 및 대응방안
