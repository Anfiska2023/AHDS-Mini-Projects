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
            response = ser.readline().decode(errors='ignore').strip()
            if response:
                print(f"<<< {response}")
        else:
            time.sleep(0.1)
    print("-" * 30)

def listen_for_rx(ser):
    print("🟢 En écoute... (CTRL+C pour quitter)")
    while True:
        if ser.in_waiting:
            response = ser.readline().decode(errors='ignore').strip()
            if response:
                print(f"<<< {response}")
        else:
            time.sleep(0.1)

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
            send_command(ser, "radio rx 0")
            listen_for_rx(ser)
    except serial.SerialException as e:
        print(f"Erreur port série : {e}")
    except KeyboardInterrupt:
        print("🛑 Arrêté par l'utilisateur.")

if __name__ == "__main__":
    main()