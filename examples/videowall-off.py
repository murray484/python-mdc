"""Disable video wall on a Samung TV with MDC protocol."""
import sys

from mdc import Mdc


def main():
    """Disable video wall."""
    if len(sys.argv) < 1:
        print("usage: %s [address]" % sys.argv[0])
        return 1
    for address in sys.argv[1:]:
        tv = Mdc(address)
        tv.connect()
        tv.video_wall_off()
    return 0


if __name__ == "__main__":
    sys.exit(main())
