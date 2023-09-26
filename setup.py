import os

# Download the serial monitor repo
os.system("git clone https://github.com/PBahner/Serial-Monitor.git utils/Serial_Monitor")

# Create __init__.py if it doesn't exist
init_file = "utils/Serial_Monitor/__init__.py"
if not os.path.exists(init_file):
    open(init_file, 'a').close()

# Install packages
os.system("pip install openai pyserial")