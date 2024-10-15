import pyfiglet
import subprocess

# Display ASCII art
ascii_text = pyfiglet.figlet_format("dionabazi")
print(ascii_text)

# Run your banner script
subprocess.run(["python3", "banner_generator.py"])
