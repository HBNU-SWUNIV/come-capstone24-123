#!/bin/bash

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

# hostapd 서비스 시작
echo "Starting hostapd service..."
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl start hostapd
