#!/usr/bin/env python
"""
MIT License

Copyright (c) 2023 Raymond Oung

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

"""Lights up LEDs to MIDI keyboard input

"""
import mido
import rainbowhat as rh
import colorsys
import time

# Name of the MIDI device
# Hint: Use mido.get_input_names() to get a list of all connected MIDI devices
DEVICE_NAME = 'CASIO USB-MIDI MIDI 1'

# MIDI keyboard note limits
NOTE_LOW = 21.
NOTE_HIGH = 108.

# MIDI keyboard velocity limits
VELOCITY_LOW = 10.
VELOCITY_HIGH = 100.


def set_rainbow(note, velocity):
  """Set rainbow LEDs
  
  LED hue is a function of MIDI note number.
  LED brightness is a function of MIDI note velocity.
  
  References:
  - https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
  """
  rh.display.clear()

  hue = (note - NOTE_LOW) / (NOTE_HIGH - NOTE_LOW)
  r, g, b = [int(c * 255 * brightness) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
  brightness = (velocity - VELOCITY_LOW) / (VELOCITY_HIGH - VELOCITY_LOW)

  # Check the note value for each octave
  if note in [x for x in range(24, 127, 12)]:
    rh.rainbow.set_pixel(0, r, g, b)
    rh.display.print_str('C')
  elif note in [x for x in range(26, 127, 12)]:
    rh.rainbow.set_pixel(1, r, g, b)
    rh.display.print_str('D')
  elif note in [x for x in range(28, 127, 12)]:
    rh.rainbow.set_pixel(2, r, g, b)
    rh.display.print_str('E')
  elif note in [x for x in range(29, 127, 12)]:
    rh.rainbow.set_pixel(3, r, g, b)
    rh.display.print_str('F')
  elif note in [x for x in range(31, 127, 12)]:
    rh.rainbow.set_pixel(4, r, g, b)
    rh.display.print_str('G')
  elif note in [x for x in range(21, 127, 12)]:
    rh.rainbow.set_pixel(5, r, g, b)
    rh.display.print_str('A')
  elif note in [x for x in range(23, 127, 12)]:
    rh.rainbow.set_pixel(6, r, g, b)
    rh.display.print_str('B')

  rh.rainbow.show()
  rh.display.show()

def clr_rainbow(note):
  """Clear rainbow LEDs
  
  Zero the LED brightness of the selected note.
  """
  if note in [x for x in range(24, 127, 12)]:
    rh.rainbow.set_pixel(0, 0, 0, 0)
  elif note in [x for x in range(26, 127, 12)]:
    rh.rainbow.set_pixel(1, 0, 0, 0)
  elif note in [x for x in range(28, 127, 12)]:
    rh.rainbow.set_pixel(2, 0, 0, 0)
  elif note in [x for x in range(29, 127, 12)]:
    rh.rainbow.set_pixel(3, 0, 0, 0)
  elif note in [x for x in range(31, 127, 12)]:
    rh.rainbow.set_pixel(4, 0, 0, 0)
  elif note in [x for x in range(21, 127, 12)]:
    rh.rainbow.set_pixel(5, 0, 0, 0)
  elif note in [x for x in range(23, 127, 12)]:
    rh.rainbow.set_pixel(6, 0, 0, 0)

  rh.rainbow.show()

# Start of the script
try:
  rh.display.print_str("MIDI")
  rh.display.show()
  print("Waiting for input device")

  # Check for new MIDI devices every 1 second
  while len(mido.get_input_names()) <= 2:
    time.sleep(1)

  # Open the device
  with mido.open_input(DEVICE_NAME) as input_port:
    rh.display.clear()
    print("Opening " + input_port.name)

    # Poll input port for messages
    for msg in input_port:
      if msg.type == 'note_on':
        set_rainbow(msg.note, msg.velocity)
      elif msg.type == 'note_off':
        clr_rainbow(msg.note)
      else:
        pass

except KeyboardInterrupt:
  # Clear the rainbow and display
  rh.rainbow.clear()
  rh.display.clear()
  rh.rainbow.show()
  rh.display.show()
  pass
