import serial
import time

PORT = "COM5"
BAUDRATE = 57600
DELAY = 1.0  # seconds between commands

commands = [
    "sys get ver",
    "mac pause",
    "radio set freq 923300000",
    "radio set sf sf7",
    "radio set bw 125",
    "radio set crc on",
    "radio rx 0"
]

def send_command(ser, cmd):
    print(f">>> {cmd}")
    ser.write((cmd + "\r\n").encode())  # CRLF
    time.sleep(DELAY)
    end_time = time.time() + 2
    while time.time() < end_time:
        if ser.in_waiting:
            response = ser.readline().decode(errors='ignore').strip()
            if response:
                print(f"<<< {response}")
        else:
            time.sleep(0.1)
    print("-" * 30)

def main():
    try:
        with serial.Serial(PORT, BAUDRATE, timeout=2) as ser:
            time.sleep(2)
            for cmd in commands:
                send_command(ser, cmd)
    except serial.SerialException as e:
        print(f"Erreur port série : {e}")

if __name__ == "__main__":
    main()