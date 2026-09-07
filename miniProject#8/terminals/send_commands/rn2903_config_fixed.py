import serial
import time

PORT = "COM5"
BAUDRATE = 57600
DELAY = 1.0  # secondes entre les commandes

# Commandes à envoyer
commands = [
    "sys get ver",
    "mac pause",
    "",  # petite pause après mac pause
    "radio set freq 923300000",
    "radio set sf sf7",
    "radio set bw 125",
    "radio set crc on",
    "radio rx 0"
]

def send_command(ser, cmd):
    if not cmd:
        print("⏸ Pause...")
        time.sleep(2)
        return

    print(f">>> {cmd}")
    ser.write((cmd + "\r").encode())
    time.sleep(DELAY)

    responses = []
    start = time.time()
    while time.time() - start < 2:
        if ser.in_waiting:
            line = ser.readline().decode(errors='ignore').strip()
            if line:
                responses.append(line)
                print(f"<<< {line}")
        else:
            time.sleep(0.1)

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