"""Board configuration and pin assignment."""

from micropython import const


class Pico:
    """Pico specific configuration."""

    MCU_FREQUENCY = const(48_000_000)  # 48 MHz
    RTC_DATETIME = (2025, 5, 3, 4, 12, 0, 0, 0)  # date after reset


class I2CConfig:
    """Inter-Integrated Circuit (I2C) configuration."""

    ID = const(0)
    SCL = const(9)
    SDA = const(8)
    FREQUENCY = const(400_000)
