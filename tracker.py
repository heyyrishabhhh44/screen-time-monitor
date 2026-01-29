import time
from config import TRACK_INTERVAL

APP_VERSION = "1.0"

print("Screen Time Monitor Started...")
print("Press CTRL + C to stop tracking")
print("App Version:", APP_VERSION)


start_time = time.time()

try:
    while True:
        time.sleep(TRACK_INTERVAL)
        current_time = time.time()
        elapsed_time = current_time - start_time
        minutes = elapsed_time / 60
        print(f"Active Screen Time: {round(minutes, 2)} minutes")


except KeyboardInterrupt:
    print("\nMonitoring Stopped")
