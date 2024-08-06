import logging
from .BaseClient import BaseClient
from .Utils import bytes_to_int, parse_temperature


class SmartShuntClient(BaseClient):
    def __init__(self, config, on_data_callback=None):
        super().__init__(config)
        self.on_data_callback = on_data_callback
        self.data = {
            'function': 'READ',
        }
        self.sections = [
            {'register': 0, 'words': 0, 'parser': self.parse_shunt_data},
        ]
    
    def create_generic_read_request(self, device_id, function, regAddr, readWrd):
        return [0xe9, 0xfc, 0x02, 0x37, 0x02]

    def on_data_received(self, response):
        self.read_timer.cancel()
        logging.info(f"on_data_received: response for read operation {response.hex()}")

    def parse_shunt_data(self, bs):
        pass