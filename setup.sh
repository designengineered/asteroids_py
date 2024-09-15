#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create the asteroids script
cat > asteroids << EOL
#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "$( readlink -f "${BASH_SOURCE[0]}" )" )" &> /dev/null && pwd )"
cd "\$SCRIPT_DIR"
source "\$SCRIPT_DIR/venv/bin/activate"
python "\$SCRIPT_DIR/main.py"
EOL

chmod +x asteroids

# Create a symbolic link in /usr/local/bin
sudo ln -sf "$SCRIPT_DIR/asteroids" /usr/local/bin/asteroids

echo "Setup complete! You can now run the game by typing 'asteroids' in any terminal."
echo "Running the game for the first time..."
./asteroids