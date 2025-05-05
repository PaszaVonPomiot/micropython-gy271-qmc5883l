from machine import I2C, Pin
from lib.qmc5883l import QMC5883L
from time import sleep
from config.board import I2CConfig


def main():
    i2c = I2C(0, scl=I2CConfig.SCL, sda=I2CConfig.SDA, freq=I2CConfig.FREQUENCY)
    sensor = QMC5883L(i2c=i2c)

    while True:
        x, y, z, _ = sensor.read_scaled()
        print(f"X:{x:.1f}", f"Y:{y:.1f}", f"Z:{z:.1f}")
        sleep(0.2)


if __name__ == "__main__":
    main()
