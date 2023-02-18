## pico-led-indicator

Sync an LED (or other component) to the state of an API endpoint. Press BOOTSEL to turn off  
(You can use this as a physical notification system or daily reminder)  

See [pico-fi](https://github.com/cfreshman/pico-fi) for more information on the underlying webserver  
See [pico-bootsel](https://github.com/cfreshman/pico-bootsel) for the BOOTSEL script  

By default, the LED is synced to https://freshman.dev/switches

### Prerequisites

Hardware
1. Pico W
1. USB to Micro USB data cable
1. LED _(optional - defaults to on-board LED)_
> [I've created a starter kit with these items](https://freshman.dev/pico-starter)  

Software
1. [MicroPython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython)
1. [rshell](https://github.com/dhylands/rshell)
> Alternatively, make your edits and upload to [pico-repo.com](https://pico-repo.com)'s how-to section to generate a drag-n-drop .uf2. Then skip to `Connect to the internet`

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

### Connect to the internet
You should see a new `w-pico` wireless network appear (password: `pico1234`). Connect to this network with your computer or smartphone. If the portal doesn't open automatically, try opening an arbitrary website.


### Physical setup
1. Connect an LED between GP17 and GND  
1. Go to https://freshman.dev/switches and turn on `default/default`  
1. If the LED doesn't turn on but you can see new messages in the console, trying flipping the LED

### Notes
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
