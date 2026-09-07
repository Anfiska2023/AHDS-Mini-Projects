import serial
import time

PORT = "COM5"
BAUDRATE = 57600
DELAY = 1.0

def send_command(ser, cmd):
    print(f">>> {cmd}")
    ser.write((cmd + "\r\n").encode())  # CRLF
    time.sleep(DELAY)
    end_time = time.time() + 2
    while time.time() < end_time:
        if ser.in_waiting:
            line = ser.readline().decode(errors='ignore').strip()
            if line:
                print(f"<<< {line}")
        else:
            time.sleep(0.1)
    print("-" * 30)

def wait_for_rx(ser):
    print("🟢 En écoute continue (CTRL+C pour arrêter)...")
    while True:
        send_command(ser, "radio rx 0")
        start = time.time()
        received = False
        while time.time() - start < 10:  # attendre jusqu’à 10 sec pour un message
            if ser.in_waiting:
                line = ser.readline().decode(errors='ignore').strip()
                if line:
                    print(f"<<< {line}")
                    if line.startswith("radio_rx"):
                        received = True
                        break
            else:
                time.sleep(0.1)
        if not received:
            print("⏳ Pas de message reçu — nouvelle tentative...")

def main():
    try:
        with serial.Serial(PORT, BAUDRATE, timeout=2) as ser:
            time.sleep(2)
            send_command(ser, "sys get ver")
            send_command(ser, "mac pause")
            send_command(ser, "radio set freq 923300000")
            send_command(ser, "radio set sf sf7")
            send_command(ser, "radio set bw 125")
            send_command(ser, "radio set crc on")
            wait_for_rx(ser)
    except serial.SerialException as e:
        print(f"Erreur port série : {e}")
    except KeyboardInterrupt:
        print("🛑 Arrêté par l'utilisateur.")

if __name__ == "__main__":
    main()