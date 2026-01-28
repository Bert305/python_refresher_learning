
# Navigate to the project code directory first:
# cd /home/miamiedtech/Freenove_4WD_Smart_Car_kit_for_Raspberry_Pi/Code/Server
# --
# Activate .venv before running programs:
# source .venv/bin/activate
# --
# install required packages if not already done:
# pip install pandas scikit-learn joblib smbus2 rpi-lgpio
# --
# Run python file:
# sudo .venv/bin/python3 log_data_step1.py


# log_data.py
import csv, time
import random

# Try to use real hardware, fall back to simulation if unavailable
USE_SIMULATION = False
try:
    from ultrasonic import Ultrasonic
    from infrared import Infrared
    sonic = Ultrasonic()
    infrared = Infrared()
    print("Using real hardware sensors")
except (ImportError, RuntimeError) as e:
    USE_SIMULATION = True
    print(f"Hardware not available ({e}), using simulation mode")
    sonic = None
    infrared = None

# Sensor reads (real or simulated)
def read_ultrasonic_cm():
    if USE_SIMULATION:
        return random.uniform(10, 100)  # Random distance 10-100cm
    return sonic.get_distance()

def read_ir_left():
    if USE_SIMULATION:
        return random.choice([0, 1])
    return infrared.read_one_infrared(1)  # 0/1

def read_ir_right():
    if USE_SIMULATION:
        return random.choice([0, 1])
    return infrared.read_one_infrared(3)  # 0/1

ACTIONS = ["forward", "backward", "left", "right", "stop"]

def get_action_from_keyboard():
    # simplest: type action in terminal while driving
    a = input("action (forward/backward/left/right/stop): ").strip().lower()
    return a if a in ACTIONS else "stop"

try:
    with open("drive_log.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ultra_cm", "ir_left", "ir_right", "action"])
        while True:
            ultra = read_ultrasonic_cm()
            ir_l = read_ir_left()
            ir_r = read_ir_right()
            action = get_action_from_keyboard()
            w.writerow([ultra, ir_l, ir_r, action])
            f.flush()
            time.sleep(0.1)
except KeyboardInterrupt:
    print("\nData logging stopped")
finally:
    if not USE_SIMULATION:
        sonic.close()
        infrared.close()
    print("Sensors closed")