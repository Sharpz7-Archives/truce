# Truce - A Catboosted Classifier for EMG Data

## Installation

- Go the the [Releases](https://github.com/Sharpz7/truce/releases) Page and download the latest release.

- Copy the libraries file to "My Documents/Arduino/libraries" (Note: You may need to create the libraries folder)

- Copy the "truce" folder to "My Documents/Arduino/libraries"

- Open the Arduino IDE and open the "truce" example.

## Libraries
- [Ardiuno Threads](https://github.com/ivanseidel/ArduinoThread)

## Output

Digital Output Pins 2-4 are used.

|  State  | Pin 2 | Pin 3 | Pin 4 |
|---------|-------|-------|-------|
| RELAXED | 0     | 0     | 1     |
| GRIPPED | 0     | 1     | 0     |
| NONE    | 0     | 0     | 0     |


## Command Help

Most important commands are kept in `./sharpdev.yml`

## TODO

- [ ] Correctly implement threading
- [ ] Support Rust
- [ ] Create Catboost Model in Python
- [ ] Improve Classification
- [ ] Add continuous integration

