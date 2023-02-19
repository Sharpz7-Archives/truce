# RandPine - A Random Forest Classifier for EMG Data

## Installation

- Go the the [Releases](https://github.com/Sharpz7/rand-pine/releases) Page and download the latest release.

- Copy the libraries file to "My Documents/Arduino/libraries" (Note: You may need to create the libraries folder)

- Copy the "rand-pine" folder to "My Documents/Arduino/libraries"

- Open the Arduino IDE and open the "rand-pine" example.

## Libraries
- [Ardiuno Threads](https://github.com/ivanseidel/ArduinoThread)

## Output

Digital Output Pins 2-4 are used.

|  State  | Pin 2 | Pin 3 | Pin 4 |
|---------|-------|-------|-------|
| RELAXED | 0     | 0     | 1     |
| GRIPPED | 0     | 1     | 0     |
| NONE    | 0     | 0     | 0     |

## TODO

- [ ] Correctly implement threading
- [ ] Improve Classification
- [ ] Add continuous integration

