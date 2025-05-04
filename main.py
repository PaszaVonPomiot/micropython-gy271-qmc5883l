from machine import I2C, Pin
from lib.qmc5883l import QMC5883L
from time import sleep


def main():
    i2c = I2C(0, scl=Pin(9), sda=Pin(8))
    qmc5883 = QMC5883L(i2c)

    while True:
        x, y, z, _ = qmc5883.read_scaled()
        print(f"X:{x:.1f}", f"Y:{y:.1f}", f"Z:{z:.1f}")
        sleep(0.2)


if __name__ == "__main__":
    main()
