import machine
from config.board import Pico

machine.freq(Pico.MCU_FREQUENCY)
machine.RTC().datetime(Pico.RTC_DATETIME)  # sync internal RTC
