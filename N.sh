#!/bin/bash


# Function to display heading
display_heading() {
        pyfiglet -f big "The Project N"
}



login() {
    read -p "Enter your Username: " username
    read -sp "Enter your Password: " password
    echo

    if [ "$username" =  "usename" ] && [ "$password" = "password" ]; then
        echo "Login successful!"
        start_phishing
    else
        echo "Invalid username or password. Please try again."
        login
    fi
}

# Function to start phishing
start_phishing() {
        echo "Starting your service..."
        sleep 3
        python3 main.py
        sleep 2
        echo "You are safe...safe with me"

}

display_heading
login
