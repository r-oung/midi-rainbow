# MIDI Rainbow
Simple example of lighting LEDs to MIDI keyboard input.

## Hardware
- [Raspberry Pi 3 Model B](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/)
- [Pimoroni Rainbow HAT](https://shop.pimoroni.com/products/rainbow-hat)

## Software
Install `mido` and `python-rtmidi` Python packages as root user:
```shell
sudo pip install mido
sudo pip install python-rtmidi
```

Install `libjack0`, which is needed for `rtmidi`:
```shell
sudo apt-get update
sudo apt-get install libjack0
```

## Start script on boot
Edit the `rc.local` file:
```shell
sudo nano /etc/rc.local
```

Add the following line. Be sure to keep the line "exit 0".
```shell
python /home/path/to/midi-rainbow.py &
```
