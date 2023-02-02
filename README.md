## pico-led-indicator

A Pico W webserver which has been set up to toggle an LED based on the state of some endpoint

See [pico-fi](https://github.com/cfreshman/pico-fi) for more information on the underlying framework

For example, sync the LED state to https://freshman.dev/switches:
```python
import time, urequests
import pico_fi
from lib import LED
from lib.logging import log


led = LED(17, .1)
app = pico_fi.App(id='w-pico', password='pico1234', indicator='LED')

@app.connected
def connected():
  # replace this with your preferred endpoint
  method = 'GET'
  url = 'https://freshman.dev/api/switch/default/default'
  log.info('attempting to', method, url)
  state = None
  while True:
    try:
      response = urequests.request(method, url)
      # parse the truthiness of your endpoint response here
      newState = response.json()['item']['state']
      if state != newState:
        log.info('new LED state:', newState)
        led.set(newState)
        state = newState
      response.close()
    except Exception as e:
      log.exception(e)
    time.sleep(.5)

app.run()
```

### Prerequisites

1. A Pico W loaded with [MicroPython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython)
1. [rshell](https://github.com/dhylands/rshell)

### Install

1. Open your Unix shell
1. Download pico-led-indicator
   ```
   git clone https://github.com/cfreshman/pico-led-indicator; cd pico-led-indicator/src
   ```
1. Connect to the board & copy files
   ```
   rshell
   ```
   ```
   rsync . /pyboard; repl
   ```
1. Soft-reboot with `CTRL+D`

You should see a new `w-pico` wireless network appear (password: `pico1234`). Connect to this network with your computer or smartphone. If the portal doesn't open automatically, try opening an arbitrary website.

Notes:
* After setup, the board name (`pyboard`) will be re-assigned to the network ID as specified in main.py (`w-pico` by default) if you restart rshell:  
  `CTRL-X` to exit repl  
  `CTRL-C` to exit rshell  
  ```
  rshell
  ```
  ```
  rsync . /w-pico; repl
  ```
* Edit the SSID/password or add additional routes in `main.py`
* Edit `index.html` to serve a single static site
* If rshell fails to connect (**after** installing MicroPython), try unplugging the Pico to reset
* If the rshell repl connects but something else isn't working, try restarting the Pico:  
  `CTRL-D` within the repl to stop execution
  ```
  import machine
  machine.reset()
  ```
  `CTRL-C` `CTRL-C` to exit repl & rshell
  ```
  rshell
  ```  
  In my experience with iOS, if something goes wrong while trying to connect, this might be necessary to reset the wireless network  
  But try opening the capture portal (`http://192.128.4.1/portal`) in a web browser first
