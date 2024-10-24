#!/bin/bash

# 필수 패키지 설치
echo "Installing necessary packages: dnsmasq and hostapd..."
sudo apt install -y dnsmasq hostapd

# dnsmasq 및 hostapd 중지
echo "Stopping dnsmasq and hostapd services..."
sudo systemctl stop dnsmasq
sudo systemctl stop hostapd

# dhcpcd 설정 파일 편집
echo "Configuring dhcpcd.conf for static IP on wlan0..."
sudo bash -c 'cat >> /etc/dhcpcd.conf <<EOL
interface wlan0
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant
EOL'

# dhcpcd 서비스 재시작
echo "Restarting dhcpcd service..."
sudo service dhcpcd restart

# dnsmasq 구성 파일 백업 및 새 구성 파일 생성
echo "Backing up dnsmasq.conf and creating new configuration..."
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
sudo bash -c 'cat > /etc/dnsmasq.conf <<EOL
interface=wlan0
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
dhcp-otrhon=option:dns-sesrver,8.8.8.8
EOL'

# dnsmasq 서비스 시작
echo "Starting dnsmasq service..."
sudo systemctl start dnsmasq

# hostapd 구성 파일 생성
echo "Creating hostapd.conf..."
sudo bash -c 'cat > /etc/hostapd/hostapd.conf <<EOL
interface=wlan0
driver=nl80211
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
ssid=CAPSTONE
wpa_passphrase=00000000
country_code=DE
hw_mode=g
channel=6
ieee80211n=1
require_ht=1
EOL'

# hostapd 기본 설정에 구성 파일 경로 추가
echo "Updating /etc/default/hostapd to use the new configuration..."
sudo sed -i 's|#DAEMON_CONF="|DAEMON_CONF="/etc/hostapd/hostapd.conf|' /etc/default/hostapd

#!/bin/bash

# IP 포워딩 활성화
echo "Enabling IP forwarding..."
sudo sed -i '/net.ipv4.ip_forward/s/^#//g' /etc/sysctl.conf
sudo sed -i '/net.ipv4.ip_forward/s/0/1/' /etc/sysctl.conf

# 변경 사항 적용
sudo sysctl -p

# NAT 설정 추가 (eth0 인터페이스를 유선 연결로 가정)
echo "Setting up NAT for eth0..."
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# iptables 규칙을 저장하여 부팅 시 유지되도록 설정
echo "Saving iptables rules..."
sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"

# 부팅 시 iptables 규칙 복원 설정
echo "Configuring iptables to restore on boot..."
if ! grep -q "iptables-restore < /etc/iptables.ipv4.nat" /etc/rc.local; then
  sudo sed -i '$i iptables-restore < /etc/iptables.ipv4.nat\n' /etc/rc.local
fi

echo "IP forwarding and NAT setup complete."

# hostapd 서비스 시작
echo "Starting hostapd service..."
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl start hostapd
