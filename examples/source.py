"""Set source on a Samung TV with MDC protocol."""
import sys

from mdc import Mdc


def main():
    """Set source."""
    if len(sys.argv) < 2:
        print("usage: %s <source> [address]" % sys.argv[0])
        return 1
    for address in sys.argv[2:]:
        tv = Mdc(address)
        tv.connect()
        tv.set_source(int(sys.argv[1], 16))
    return 0


if __name__ == "__main__":
    sys.exit(main())
