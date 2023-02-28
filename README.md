**This has been moved under [pico-fi](https://freshman.dev/git:pico-fi) → [packs/led-indicator](https://freshman.dev/git:pico-fi/tree/master/src/packs/led-indicator/__init__.py)**


## pico-led-indicator

Sync an LED (or other component) to an endpoint. Press BOOTSEL to turn off  

For example, use as a physical notification system or daily reminder  

See [pico-fi](https://github.com/cfreshman/pico-fi) for more information on the underlying webserver  
See [pico-bootsel](https://github.com/cfreshman/pico-bootsel) for the BOOTSEL script  


### Setup

1. Follow steps & review notes for [pico-fi](https://github.com/cfreshman/pico-fi/blob/master/README.md#prerequisites)  
You should see a new `w-pico` wireless network appear (password: `pico1234`). Connect to this network with your computer or smartphone. If the portal doesn't open automatically, try opening an arbitrary website.
1. (Optional) Connect an LED between GP17 and GND  
1. Go to [freshman.dev/switches](https://freshman.dev/switches) and turn on `default/default`  
1. If the LED doesn't turn on but you can see new messages in the console, trying flipping the LED
1. If the LED does turn on:
   - Press BOOTSEL to turn it off
   - Confirm `default/default` updates after a few seconds
   - Edit [main.py](./src/main.py) to your own endpoint
