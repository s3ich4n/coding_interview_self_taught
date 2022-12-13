import random

TRIALS = 100_000
same_birthdays = 0


for _ in range(TRIALS):
    birthdays = []

    for i in range(50):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            same_birthdays += 1
            break
        birthdays.append(birthday)

print(f"same birthday rate: {same_birthdays / TRIALS * 100}")
