from unittest import TestCase
from unittest.mock import patch, Mock

from mdc import exceptions, Mdc


class TestMdc(TestCase):

    @patch('socket.socket')
    def setUp(self, socket_mock):
        self.mdc = Mdc("test.local", 4242)

    def test_power_on(self):
        self.mdc.send_command = Mock()
        self.mdc.power_on()
        self.mdc.send_command.assert_called_with(0x11, 1)

    def test_power_off(self):
        self.mdc.send_command = Mock()
        self.mdc.power_off()
        self.mdc.send_command.assert_called_with(0x11, 0)

    def test_video_wall_on(self):
        self.mdc.send_command = Mock()
        self.mdc.video_wall_on()
        self.mdc.send_command.assert_called_with(0x84, 1)

    def test_video_wall_off(self):
        self.mdc.send_command = Mock()
        self.mdc.video_wall_off()
        self.mdc.send_command.assert_called_with(0x84, 0)

    def test_set_video_wall(self):
        self.mdc.send_command = Mock()
        self.mdc.set_video_wall(2, 1, 1)
        self.mdc.send_command.assert_called_with(0x89, 0x21, 1)

    def test_set_video_wall_disable(self):
        self.mdc.send_command = Mock()
        self.mdc.set_video_wall(0, 1, 1)
        self.mdc.send_command.assert_called_with(0x89, 0x00, 1)

    def test_set_video_wall_pos_over(self):
        with self.assertRaises(exceptions.VideoWallNotSupported):
            self.mdc.set_video_wall(2, 1, 42)

    def test_set_video_wall_pos_under(self):
        with self.assertRaises(exceptions.VideoWallNotSupported):
            self.mdc.set_video_wall(2, 1, 0)

    def test_set_video_wall_row_over(self):
        with self.assertRaises(exceptions.VideoWallNotSupported):
            self.mdc.set_video_wall(6, 1, 1)

    def test_set_video_wall_row_under(self):
        with self.assertRaises(exceptions.VideoWallNotSupported):
            self.mdc.set_video_wall(-1, 1, 1)

    def test_set_video_wall_col_over(self):
        with self.assertRaises(exceptions.VideoWallNotSupported):
            self.mdc.set_video_wall(1, 6, 1)

    def test_set_video_wall_col_under(self):
        with self.assertRaises(exceptions.VideoWallNotSupported):
            self.mdc.set_video_wall(1, 0, 1)

    def test_set_volume(self):
        self.mdc.send_command = Mock()
        self.mdc.set_volume(42)
        self.mdc.send_command.assert_called_with(0x12, 42)

    def test_set_volume_over(self):
        with self.assertRaises(exceptions.InvalidVolume):
            self.mdc.set_volume(101)

    def test_set_volume_under(self):
        with self.assertRaises(exceptions.InvalidVolume):
            self.mdc.set_volume(-1)

    def test_mute_on(self):
        self.mdc.send_command = Mock()
        self.mdc.mute_on()
        self.mdc.send_command.assert_called_with(0x13, 1)

    def test_mute_off(self):
        self.mdc.send_command = Mock()
        self.mdc.mute_off()
        self.mdc.send_command.assert_called_with(0x13, 0)

    def test_set_source(self):
        self.mdc.send_command = Mock()
        self.mdc.set_source(0x25)
        self.mdc.send_command.assert_called_with(0x14, 0x25)

    def test_set_source_invalid(self):
        with self.assertRaises(exceptions.SourceNotExist):
            self.mdc.set_source(0x42)

    def test_send_command(self):
        self.mdc.send_command(0x42, 0x01, 0x02, 0x03)
        self.mdc._socket.send.assert_called_with(
            bytes([0xAA, 0x42, 0xFE, 3, 0x01, 0x02, 0x03, 73])
        )

    def test_connect(self):
        self.mdc.connect()
        self.mdc._socket.connect.assert_called_with(("test.local", 4242))
