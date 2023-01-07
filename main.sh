#!/bin/bash

IMAGE_DIR="images"

check_dir() {
    if [ -d $1 ]; then
        echo "Directory exists. Resetting images folder"
        return 0
    else
        echo "Directory does not exist. Creating images folder"
        return 1
    fi
}


if ! check_dir $IMAGE_DIR; then
    python3 src/scripts/create_images_folder.py
else
    python3 src/scripts/reset_images.py
fi