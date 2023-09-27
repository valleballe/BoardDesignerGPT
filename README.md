# BoardDesignerGPT
Generates code using OpenAI's GPT-4 or GPT-3.5 and uploads it to board based on specified goal and components.

## Getting started

### Installing packages
1. Clone the repository
```
git clone https://github.com/valleballe/BoardDesignerGPT/
```
2. Install the Arduino-CLI follow [these intructions](https://arduino.github.io/arduino-cli/0.33/installation/).
3. Install the required packages by running `setup.py`
```
python setup.py
```
### Setting up your board and API keys
Set your project variables and board specifications in the settings. You can get an OpenAI API key [here](https://platform.openai.com/account/api-keys).
```
OPENAI_API_KEY = "YOUR_API_KEY"

port = "/dev/cu.usbserial-110"  # Replace with your Arduino Nano's port (e.g., COM3 for Windows)
board_fqbn = "arduino:avr:nano:cpu=atmega328" # Fully Qualified Board Name (FQBN). Replace with whatever board you are using.
project_directory = "test" # Replace with the name for your project (where you want your code files stored).
```
### Identifying Your Board Configuration

To correctly set your Arduino board, you need to identify the **port** and **Fully Qualified Board Name (FQBN)**.

**Finding the Port:**
- For **Windows**, open the device manager and locate "Ports (COM & LPT)". Your Arduino board should be listed there (like "USB-SERIAL CH340 (COM3)"). Use the COM value as your port.
- For **macOS**, open Terminal and type `ls /dev/cu.*`. This returns a list of all devices, find your Arduino device on the list (it usually appears like  "/dev/cu.usbserial-XXXX").

**Identifying the FQBN:**
- The FQBN consists of the package name (e.g. "arduino"), the architecture (e.g. "avr"), the board ID (e.g. "nano"), and finally the board version (e.g. "cpu=atmega328").
- You can find your FQBN using the Arduino command line interface (CLI) with the command `arduino-cli board list`.
- If you're unsure, use the Arduino IDE. Connect your Arduino board, select the correct option in the Tools > Board menu, and use the Tools > Get Board Info command to get the exact FQBN.
Having identified these, you should update the `port` and `board_fqbn` variables in your settings


## Usage
You run BoardDesignerGPT with the following command.
```
python app.py --goal "Your goal and connected pins"
```
Be aware that you might have to run the script a few times if the code does not compile.

##  Contribute

BoardDesignerGPT is under active development and contributors are welcome. If you have any suggestions, feature requests, or bug reports, please open new [issues](https://github.com/valleballe/BoardDesignerGPT/issues) on GitHub. 


## BibTeX Citation

If you use BoardDesignerGPT in a scientific publication or installation, we would appreciate using the following citations:

```
@software{danry2023board,
  author = {Danry, Valdemar},
  month = {9},
  title = {{BoardDesignerGPT}},
  url = {https://github.com/valleballe/BoardDesignerGPT},
  year = {2023}
}
