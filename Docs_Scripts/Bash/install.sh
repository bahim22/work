#!/bin/bash

# bash script to download powershell for install in Ubuntu
file=a_packages-microsoft-prod.deb
url=https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb

sudo apt install -y wget apt-transport-https software-properties-common

curl --dns-servers 1.1.1.1 --compressed --output $file $url --progress-bar

sudo dpkg -i $file

sudo apt update

sudo apt install -y powershell

# functional og script

# file=packages-microsoft-prod.deb
# url=https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb

# curl --dns-servers 1.1.1.1 --compressed --output $file $url --progress-bar