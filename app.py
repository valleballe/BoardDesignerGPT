import os
import argparse

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.abspath(__file__), 'utils'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'utils/Serial_Monitor'))

from utils.llm import GPT4
from utils.Serial_Monitor.monitor import monitor

from settings import port
from settings import board_fqbn
from settings import project_directory


# Initialize classes
code_writer = GPT4("Write the C code to compile in arduino, and only return the raw code. Never include '```c' nor '```':")




def compile_and_upload(code: str, board_fqbn: str, port: str, project_directory: str):
    os.makedirs(project_directory, exist_ok=True)

    with open(f"{project_directory}/test.ino", "w") as f:
        f.write(code)

    # Build and compile the code
    compilation_command = f"arduino-cli compile --fqbn {board_fqbn} {project_directory}"
    print(f"Compiling code: {compilation_command}")
    os.system(compilation_command)

    # Upload the compiled code to the board
    upload_command = f"arduino-cli upload --fqbn {board_fqbn} -p {port} {project_directory}"
    print(f"Uploading code: {upload_command}")
    os.system(upload_command)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Main script")
    parser.add_argument('-g','--goal', type=str, default="Goal: I have a water sensor hooked up to D2. Print its output.", help='Prompt to generate image. Leave empty if image is prefered.')
    args = parser.parse_args()
    
    # Specify goal and components 
    goal = args.goal
    components = f"Components: {board_fqbn}"
    prompt = '\n\n'.join((components,goal))

    # Generate C code
    print("Generating code...")
    code_string = code_writer.generate_response(prompt)
    print(code_string)


    # Upload code to board
    print("Uploading code...")
    compile_and_upload(code_string, board_fqbn, port, project_directory)
    print("Done...")

    # Run serial monitor
    print("Running serial monitor")
    monitor(port)