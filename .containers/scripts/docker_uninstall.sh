#!/bin/bash
set -e

echo "==== Stopping Docker processes ===="

# Stop Docker service if present (WSL2 may not support this)
sudo service docker stop >/dev/null 2>&1 || true

# Kill dockerd and containerd if running
for proc in dockerd containerd; do
    pids=$(pgrep -f "$proc" 2>/dev/null || true)
    for pid in $pids; do
        echo "Stopping $proc (PID $pid)"
        sudo kill "$pid" 2>/dev/null || true
        sleep 1
        sudo kill -9 "$pid" 2>/dev/null || true
    done
done

echo "==== Removing Docker packages ===="

sudo apt purge -y                   \
        docker.io                   \
        docker-ce                   \
        docker-ce-cli               \
        docker-buildx-plugin        \
        docker-compose-plugin       \
        docker-ce-rootless-extras   \
        containerd.io               \
        containerd                  \
        runc || true

sudo apt autoremove -y

echo "==== Cleaning up Docker files and directories ===="

DIRS=(
    /var/lib/docker
    /var/lib/containerd
    /var/run/docker
    /run/docker
    /run/containerd
    /etc/docker
    /etc/containerd
    /etc/apt/keyrings/docker.gpg
    /usr/share/keyrings/docker-archive-keyring.gpg
    /etc/apt/trusted.gpg.d/docker.gpg
    /etc/apt/sources.list.d/docker.list
)

for dir in "${DIRS[@]}"; do
    if [ -e "$dir" ]; then
        echo "Removing $dir"
        sudo rm -rf "$dir"
    fi
done

echo "==== Removing Docker group if it exists ===="
if getent group docker >/dev/null; then
    sudo groupdel docker || true
fi

echo "==== Docker uninstallation complete! ===="
