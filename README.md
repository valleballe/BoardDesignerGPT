# BoardDesignerGPT
Generates code and uploads it to board based on specified goal and components.

## Getting started

1. Clone the repository
```
git clone https://github.com/valleballe/BoardDesignerGPT/
```
1. Install the Arduino-CLI follow [these intructions](https://arduino.github.io/arduino-cli/0.33/installation/).
2. Install the required packages by running `setup.py`
```
python setup.py
```
3. Set your project variables and board specifications in the settings. You can get an OpenAI API key [here](https://platform.openai.com/account/api-keys).
```
OPENAI_API_KEY = "YOUR_API_KEY"

port = "/dev/cu.usbserial-110"  # Replace with your Arduino Nano's port (e.g., COM3 for Windows)
board_fqbn = "arduino:avr:nano:cpu=atmega328" # Fully Qualified Board Name (FQBN). Replace with whatever board you are using.
project_directory = "test" # Replace with the name for your project (where you want your code files stored).
```

## Usage
You run BoardDesignerGPT with the following command.
```
python app.py --goal "Your goal"
```
Beware that you might have to rerun a few times until the code compiles.

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
