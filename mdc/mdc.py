"""Provide a class to send command to TV."""
import socket


class Mdc():

    def __init__(self, ip=None, port=1515, mdc_id=0xFE):
        self._id = mdc_id
        self._ip = ip
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self._socket.connect((self._ip, self._port))

    def send_command(self, command_id, *args):
        command = [0xAA, command_id, self._id, len(args)] + list(args)
        checksum = sum(command[1:]) % 256
        command.append(checksum)
        self._socket.send(bytes(command))

    def power_off(self):
        self.send_command(0x11, 0x0)

    def power_on(self):
        self.send_command(0x11, 0x1)
