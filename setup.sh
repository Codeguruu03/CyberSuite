#!/bin/bash

# Check for Python
if ! [ -x "$(command -v python3)" ]; then
  echo '\033[31m\nError: Python3 is not installed.' >&2
  exit 1

else
    echo -e "\033[35m\n"
    python3 --version
    echo ""

fi

# Check for pip
if ! [ -x "$(command -v pip3)" ]; then
  echo -e '\033[31m\nError: pip3 is not installed.' >&2
  exit 1

else
    pip3 --version
    echo -e "\033[0m"
fi

# Install Dependencies
pip3 install -r requirements.txt

# Installation Complete
echo -e "\033[32m\nAll dependencies have been installed successfully."
sleep 1
echo -e "\nYou can now run the command: \033[33m\npython main.py\033[0m"
sleep 1
echo -e "\033[34m\nPress Enter to exit...\033[0m"
read
