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
