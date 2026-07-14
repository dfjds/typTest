import time

# countdown from 60 seconds, print on the same line
for remaining in range(60, 0, -1):
    print(f"{remaining:2d}s", end="\r", flush=True)
    time.sleep(1)
print("\n")


typed = input("> ")

def test_typing_speed(typed, time):
    chars = len(typed)
    wpm = (chars / 5) / (time / 60)

    print(f"Your typing speed is {wpm:.2f} WPM.")