#!/bin/bash

# Set the image name
IMAGE_NAME="nginx"

# Set the base container name
BASE_CONTAINER_NAME="nginx_container"

# Specify the network interface you want to get the IP address for, e.g. enp0s3
NETWORK_INTERFACE="enp0s31f6"

# Detect the host machine's IP address for the specified network interface
HOST_IP=$(ip -4 addr show $NETWORK_INTERFACE | grep -oP '(?<=inet\s)\d+(\.\d+){3}')

# Function to check if a port is available
is_port_free() {
    netstat -tuln | awk '{print $4}' | grep -q ":$1$"
    return $?
}

# Find the first available port in the specified range (e.g., 8000-8100)
START_PORT=8080
END_PORT=8100
HOST_PORT=""

for port in $(seq $START_PORT $END_PORT); do
    if ! is_port_free $port; then
        HOST_PORT=$port
        break
    fi
done

if [ -z "$HOST_PORT" ]; then
    echo "No available ports in the range $START_PORT-$END_PORT"
    exit 1
fi

# Find an unused container name with an incremented number suffix
CONTAINER_NUMBER=1
while docker ps -a --format "{{.Names}}" | grep -q "${BASE_CONTAINER_NAME}${CONTAINER_NUMBER}"; do
    CONTAINER_NUMBER=$((CONTAINER_NUMBER + 1))
done
CONTAINER_NAME="${BASE_CONTAINER_NAME}${CONTAINER_NUMBER}"

# Run the Docker container and map the port to host, e.g. map container's port 80 to the first available host port
docker run -d --name "$CONTAINER_NAME" -p "$HOST_PORT":80 "$IMAGE_NAME"

# Print the IP address and port number
echo "Access the Nginx web service at: http://$HOST_IP:$HOST_PORT"
