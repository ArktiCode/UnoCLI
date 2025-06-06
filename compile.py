import PyInstaller.__main__
import platform
import shutil
import os

# Determine the operating system
current_os = platform.system()

# Common PyInstaller options
common_options = [
    'main.py',               # Your main entry file
    '--onefile',             # Single executable
    '--windowed',            # For console apps, keeps the terminal open
    '--name=UnoCLI',         # Name of the executable
    '--add-data=game:game',  # Include your game package
    '--clean',               # Clean build
]

# OS-specific adjustments
if current_os == "Windows":
    common_options.append('--console')  # Explicitly keep the console for Windows CMD
elif current_os == "Linux":
    common_options.append('--strip')    # Optimize binary for Linux

# Run PyInstaller
PyInstaller.__main__.run(common_options)

# Clean up temporary files
shutil.rmtree('build', ignore_errors=True)
os.remove('UnoCLI.spec')