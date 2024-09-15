# 🚀 Asteroids in Pygame 🌠

A classic Asteroids-style game implemented in Python using Pygame, showcasing Object-Oriented Programming principles! 🎮

Project by Cello ([@laztaxon](https://github.com/laztaxon)) as part of an Object Oriented Programming course.

**Note: This is version 1.0 of the game. Visuals and mechanics may change in future updates.**

![Asteroids Gameplay](assets/trailer.gif)

## 🕹️ Controls

- **W**: Move forward
- **S**: Move backward
- **A**: Rotate left
- **D**: Rotate right
- **Spacebar**: Shoot

Shoot asteroids to split them into smaller pieces. Be careful not to collide with them!

## 🛠️ Setup and Installation

1. Ensure you have Python 3.10 or later installed on your system. 🐍
   You can download it from [python.org](https://www.python.org/downloads/).

2. Clone this repository:
   ```
   git clone https://github.com/laztaxon/asteroids_py.git
   cd asteroids_py
   ```

3. Run the setup script:
   - On Windows:
     ```
     setup.bat
     ```
   - On macOS and Linux:
     ```
     chmod +x setup.sh  # Make the script executable (first time only)
     ./setup.sh
     ```

   This script will create a virtual environment, install the required packages, and set up the game to run globally.

## 🎮 Running the Game

After running the setup script, you can start your space adventure from anywhere by simply typing:

- On Windows:
  ```
  run_asteroids.bat
  ```
- On macOS and Linux:
  ```
  asteroids
  ```

You may need to restart your terminal or command prompt for the changes to take effect.

## 🔄 Updating the Game

To update the game to the latest version:

1. Navigate to the game directory:
   ```
   cd path/to/asteroids_py
   ```

2. Pull the latest changes:
   ```
   git pull origin main
   ```

3. Run the setup script again to ensure all dependencies are up to date:
   - On Windows: `setup.bat`
   - On macOS and Linux: `./setup.sh`

After updating, you may need to restart your terminal or command prompt for any changes to take effect.

## 🔧 Troubleshooting

If you encounter any issues running the game, try the following:

1. Ensure you're using Python 3.10 or later.
2. Make sure you've run the setup script as described in the Setup and Installation section.
3. If you're on macOS or Linux and the `asteroids` command isn't found, try running:
   ```
   sudo ln -sf /path/to/your/asteroids_py/asteroids /usr/local/bin/asteroids
   ```
   Replace `/path/to/your/asteroids_py` with the actual path to your game directory.
4. If you encounter permission issues, you may need to run:
   ```
   sudo chmod +x /usr/local/bin/asteroids
   ```
5. If you're still having issues, please open an issue on the GitHub repository with details about the error you're encountering.
