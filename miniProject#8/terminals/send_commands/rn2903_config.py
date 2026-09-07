import serial
import time

# Modifier ici si ton port est différent
PORT = "COM5"
BAUDRATE = 57600
DELAY = 1  # secondes entre chaque commande

# Commandes à envoyer
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
    ser.write((cmd + "\r").encode())  # RN2903 attend CR
    time.sleep(DELAY)
    while ser.in_waiting:
        response = ser.readline().decode(errors='ignore').strip()
        if response:
            print(f"<<< {response}")

def main():
    try:
        with serial.Serial(PORT, BAUDRATE, timeout=2) as ser:
            time.sleep(2)  # attendre l'initialisation du port
            for cmd in commands:
                send_command(ser, cmd)
    except serial.SerialException as e:
        print(f"Erreur ouverture du port série : {e}")

if __name__ == "__main__":
    main()