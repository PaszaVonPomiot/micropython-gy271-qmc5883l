from machine import RTC


class Clock:
    def __init__(self) -> None:
        self._rtc = RTC()  # already synchronized in boot.py

    def now(self) -> str:
        """Return the current date and time in the format 'YYYY-MM-DD HH:MM:SS'."""
        dt = self._rtc.datetime()
        return (
            f"{dt[0]:04d}-{dt[1]:02d}-{dt[2]:02d} {dt[4]:02d}:{dt[5]:02d}:{dt[6]:02d}"
        )


clock = Clock()
