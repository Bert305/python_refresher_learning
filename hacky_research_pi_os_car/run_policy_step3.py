
# Install these packages if not already installed:
# sudo apt update
# sudo apt install -y python3-pandas python3-sklearn python3-joblib

# --
# Install GPIO packages if not already done:
# pip install rpi-lgpio RPi.GPIO
# sudo pip3 install --break-system-packages pandas scikit-learn joblib
# --
# Run the file:
# sudo .venv/bin/python3 run_policy_step3.py
# --> If don't work, try:
# sudo python3 run_policy_step3.py

# run_policy.py
import joblib
import time
import os
import random

# Try sensors; fall back to simulation if unavailable
USE_SIM_SENSORS = False
try:
    from ultrasonic import Ultrasonic
    from infrared import Infrared
    _sonic = Ultrasonic()
    _infrared = Infrared()
    print("Using real hardware sensors")
except (ImportError, RuntimeError) as e:
    USE_SIM_SENSORS = True
    _sonic = None
    _infrared = None
    print(f"Sensors not available ({e}), using simulation mode")

# Try to import real motor driver; fall back to simulation if unavailable
USE_SIM_MOTOR = False
try:
    from motor import Ordinary_Car
except (ImportError, RuntimeError) as e:
    USE_SIM_MOTOR = True
    print(f"Motor hardware not available ({e}), using simulation mode")

    class Ordinary_Car:  # simulation stub
        def set_motor_model(self, d1, d2, d3, d4):
            print(f"[SIM MOTOR] set_motor_model({d1}, {d2}, {d3}, {d4})")
        def close(self):
            print("[SIM MOTOR] close")

# Check if model exists
if not os.path.exists("car_policy.joblib"):
    print("ERROR: car_policy.joblib not found. Run train_model_step2.py first.")
    exit(1)

model = joblib.load("car_policy.joblib")
print("Loaded car_policy.joblib")
print(f"Sensor mode: {'real' if not USE_SIM_SENSORS else 'simulation'}")
print(f"Motor mode: {'real' if not USE_SIM_MOTOR else 'simulation'}")

# Initialize hardware (or simulation)
sonic = _sonic if not USE_SIM_SENSORS else None
infrared = _infrared if not USE_SIM_SENSORS else None
motor = Ordinary_Car()

# Sensor reads (real or simulated)
def read_ultrasonic_cm():
    if USE_SIM_SENSORS:
        return random.uniform(10, 100)
    return sonic.get_distance()

def read_ir_left():
    if USE_SIM_SENSORS:
        return random.choice([0, 1])
    return infrared.read_one_infrared(1)

def read_ir_right():
    if USE_SIM_SENSORS:
        return random.choice([0, 1])
    return infrared.read_one_infrared(3)

def do_action(a):
    """Execute motor commands based on predicted action"""
    if a == "forward":
        motor.set_motor_model(1500, 1500, 1500, 1500)
    elif a == "backward":
        motor.set_motor_model(-1500, -1500, -1500, -1500)
    elif a == "left":
        motor.set_motor_model(1500, 1500, -1000, -1000)
    elif a == "right":
        motor.set_motor_model(-1000, -1000, 1500, 1500)
    elif a == "stop":
        motor.set_motor_model(0, 0, 0, 0)
    print("ACTION:", a)

try:
    print("Starting autonomous mode...")
    while True:
        X = [[read_ultrasonic_cm(), read_ir_left(), read_ir_right()]]
        action = model.predict(X)[0]
        print(f"PRED: {action}, X={X[0]}, sim_sensors={USE_SIM_SENSORS}, sim_motor={USE_SIM_MOTOR}")
        do_action(action)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nStopping autonomous mode")
finally:
    motor.set_motor_model(0, 0, 0, 0)
    if not USE_SIM_SENSORS:
        sonic.close()
        infrared.close()
    motor.close()
    print("Hardware closed")