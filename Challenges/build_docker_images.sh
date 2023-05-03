#!/bin/bash

# Set the base directory to the current directory
base_dir="."

# Find all Dockerfiles within the base directory and its subdirectories
find "$base_dir" -type f -name 'Dockerfile' | while read -r dockerfile; do
  # Get the directory containing the Dockerfile
  dir=$(dirname "$dockerfile")

  # Get the directory name 
  dir_name=$(basename "$dir")

  # Replace any invalid characters or spaces with underscores
  sanitized_dir_name=$(echo "$dir_name" | sed 's/[^a-zA-Z0-9._-]/_/g')

  # Build the Docker image and tag it with the sanitized directory name
  docker build --no-cache -t "$sanitized_dir_name" "$dir"
done
