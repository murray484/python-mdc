"""Provide a class to send command to TV."""
import socket

from . import exceptions


class Mdc():
    """Implement the MDC protocol."""

    def __init__(self, ip=None, port=1515, mdc_id=0xFE):
        """Initialize class with ip, port and mdc ID.

        By default, MDC protocol listen on port 1515.
        We can use MDC ID 0xFE for globing.
        """
        self._id = mdc_id
        self._ip = ip
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """Connect the socket to the remote TV."""
        self._socket.connect((self._ip, self._port))

    def send_command(self, command_id, *args):
        """Send a command to the remote TV."""
        command = [0xAA, command_id, self._id, len(args)] + list(args)
        checksum = sum(command[1:]) % 256
        command.append(checksum)
        self._socket.send(bytes(command))

    def power_off(self):
        """Power off the remote TV."""
        self.send_command(0x11, 0x0)

    def power_on(self):
        """Power on the remote TV."""
        self.send_command(0x11, 0x1)

    def set_source(self, source_id):
        """Set the source of the remote TV."""
        available_sources = [
            0x14, 0x1E, 0x18, 0x0C, 0x04, 0x08,
            0x20, 0x30, 0x40, 0x21, 0x23, 0x25
        ]
        if source_id not in available_sources:
            raise exceptions.SourceNotExist()
        self.send_command(0x14, source_id)

    def set_volume(self, volume):
        """Set the volume of the remote TV."""
        if 0 < volume > 100:
            raise exceptions.InvalidVolume()
        self.send_command(0x12, volume)

    def mute_on(self):
        """Mute the remote TV."""
        self.send_command(0x13, 0x1)

    def mute_off(self):
        """Unmute the remote TV."""
        self.send_command(0x13, 0x0)
