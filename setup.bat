@echo off
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt

:: Get the absolute path of the current directory
for %%I in ("%CD%") do set "GAME_DIR=%%~fI"

:: Add the game directory to the system PATH
setx PATH "%PATH%;%GAME_DIR%"

echo Setup complete! You can now run the game by typing 'run_asteroids.bat' in any command prompt.
echo You may need to restart your command prompt for the changes to take effect.
echo Running the game for the first time...
run_asteroids.bat