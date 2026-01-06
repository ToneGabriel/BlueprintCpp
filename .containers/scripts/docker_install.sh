#!/bin/bash
set -e

WSL_USER=$(whoami)

echo "==== Updating system packages ===="
sudo apt update && sudo apt upgrade -y

echo "==== Installing prerequisites ===="
sudo apt install -y                 \
        apt-transport-https         \
        ca-certificates             \
        curl                        \
        software-properties-common  \
        lsb-release                 \
        gnupg

echo "==== Adding Docker GPG key and repository ===="
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

echo "==== Updating package index ===="
sudo apt update

echo "==== Installing Docker packages ===="
sudo apt install -y                 \
        docker-ce                   \
        docker-ce-cli               \
        containerd.io

echo "==== Adding $WSL_USER to docker group ===="
sudo usermod -aG docker "$WSL_USER"

echo "==== Notes for WSL2 ===="
echo "Docker service is not managed via systemd in WSL2."
echo "You can start Docker daemon manually with: sudo dockerd &"
echo "Or install Docker Desktop on Windows for seamless integration."

echo "==== Testing Docker installation ===="
if docker --version >/dev/null 2>&1; then
    echo "Docker installed successfully!"
    echo "Run 'docker run hello-world' after restarting your WSL session."
else
    echo "Docker installation may have issues."
fi
