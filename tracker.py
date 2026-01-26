import time

print("Screen Time Monitor Started")

start_time = time.time()

try:
    while True:
        time.sleep(5)
        current_time = time.time()
        elapsed_time = current_time - start_time
        minutes = elapsed_time / 60
        print(f"Screen Time: {round(minutes, 2)} minutes")

except KeyboardInterrupt:
    print("\nMonitoring Stopped")
