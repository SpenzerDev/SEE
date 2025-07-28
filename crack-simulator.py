import time
import random
import sys

# Characters that can appear in a password
CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

# Simulated target password
TARGET_PASSWORD = "P@ssw0rd123!"

# Animation speed (lower is faster)
SPEED = 0.05

def simulate_crack(target):
    print("\n[+] Initiating brute-force password cracking simulation...\n")
    guessed = ""
    for i in range(len(target)):
        while True:
            guess = random.choice(CHARS)
            sys.stdout.write(f"\r[Cracking] {guessed + guess}")
            sys.stdout.flush()
            time.sleep(SPEED)
            if guess == target[i]:
                guessed += guess
                break
    print(f"\n\n[✓] Password successfully cracked: {guessed}")

if __name__ == "__main__":
    simulate_crack(TARGET_PASSWORD)