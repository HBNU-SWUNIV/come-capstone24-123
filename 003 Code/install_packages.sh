#!/bin/bash

# 시스템 패키지 업데이트 및 설치
echo "Updating system and installing required packages..."

# 패키지 목록 업데이트
sudo apt update

# 필수 패키지 설치
sudo apt install -y systemd-networkd dnsmasq dhcpcd5 net-tools tcpdump python3-pip python3

# Python 패키지 설치
echo "Installing Python packages from requirements.txt..."
pip3 install -r requirements.txt

echo "All packages installed successfully."
