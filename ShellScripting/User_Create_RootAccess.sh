#!/bin/bash

# Read username and password from the user
read -p "Enter username: " username
read -s -p "Enter password: " password
echo    # Add a newline after password input for better formatting

# Create the user
sudo useradd -m "$username"

# Check if user creation was successful
if [ $? -eq 0 ]; then
  echo "User '$username' created successfully."
else
  echo "Failed to create user '$username'."
  exit 1
fi

# Set the password for the user
echo "$username:$password" | sudo chpasswd

# Check if password setting was successful
if [ $? -eq 0 ]; then
  echo "Password set successfully for user '$username'."
else
  echo "Failed to set password for user '$username'."
  exit 1
fi

# Optionally, force the user to change password on first login
sudo passwd -e "$username"

echo "$username    ALL=(ALL)    NOPASSWD: ALL" | sudo tee -a /etc/sudoers
sudo chage -I -1 -m 0 -M 99999 -E -1 $username
sudo echo "$password" | passwd  --stdin $username
echo "User '$username' setup complete with sudo permissions."
