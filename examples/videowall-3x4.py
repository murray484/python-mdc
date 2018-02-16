"""Setup video wall 3 x 4 on a Samung TV with MDC protocol."""
import sys

from mdc import Mdc


def main():
    """Enable video wall by 3 x 4."""
    if len(sys.argv) < 4:
        print("usage: %s [address]" % sys.argv[0])
        return 1
    pos = 12
    first_one = True
    for address in sys.argv[1:]:
        tv = Mdc(address)
        tv.connect()
        if not first_one:
            tv.set_source(0x25)
            first_one = False
        tv.video_wall_on()
        tv.set_video_wall(4, 3, pos)
        pos -= 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
