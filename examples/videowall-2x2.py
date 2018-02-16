"""Power off a Samung TV with MDC protocol."""
import sys

from mdc import Mdc


def main():
    """Enable video wall by 2 x 2."""
    if len(sys.argv) < 4:
        print("usage: %s <address 1> <address 2> <address 3> <address 4>" % (
            sys.argv[0]
        ))
        return 1
    tv1 = Mdc(sys.argv[1])
    tv2 = Mdc(sys.argv[2])
    tv3 = Mdc(sys.argv[3])
    tv4 = Mdc(sys.argv[4])
    tv1.connect()
    tv2.connect()
    tv3.connect()
    tv4.connect()
    tv1.video_wall_on()
    tv2.set_source(0x25)
    tv3.set_source(0x25)
    tv4.set_source(0x25)
    tv2.video_wall_on()
    tv1.set_video_wall(2, 2, 4)
    tv2.set_video_wall(2, 2, 2)
    tv3.set_video_wall(2, 2, 1)
    tv4.set_video_wall(2, 2, 3)
    return 0


if __name__ == "__main__":
    sys.exit(main())
