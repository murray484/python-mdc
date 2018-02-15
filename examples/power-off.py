"""Power off a Samung TV with MDC protocol."""
import sys

from mdc import Mdc


def main():
    """Send a power off command to the IP given from command line."""
    if len(sys.argv) < 2:
        print("usage: %s <address>" % sys.argv[0])
        return 1
    tv = Mdc(sys.argv[1])
    tv.connect()
    tv.power_off()


if __name__ == "__main__":
    sys.exit(main())
