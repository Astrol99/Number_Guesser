import time

number = int(input("Please enter a number to guess: "))
limit = int(input("Please enter the limit of guesses: "))

start = time.time()

for i in range(limit):
    print(f"Trying - {i}...")
    if i == number:
        print("     SUCCESS")
        print(f"[!] Found number! - {i}")
        end = time.time() - start
        print(f"Found number in {end} seconds")
        print(f"Approx. {i/end} guesses per second")
        break
    else:
        print("     FAILED")
