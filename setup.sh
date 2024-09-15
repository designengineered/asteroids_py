#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
chmod +x asteroids

# Get the absolute path of the current directory
GAME_DIR=$(pwd)

# Create a symbolic link in /usr/local/bin
sudo ln -s "$GAME_DIR/asteroids" /usr/local/bin/asteroids

echo "Setup complete! You can now run the game by typing 'asteroids' in any terminal."
echo "Running the game for the first time..."
asteroids