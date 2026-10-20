# By submitting this assignment, all team members agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Reed Scott (UIN: 838002005)
#               Sho Hiroi (UIN: 837008392)
#               Xavier Gomez (UIN: 538001968)
#               Izaac Almeida (UIN: 238008017)
# Section:      553
# Assignment:   Lab 8A
# Date:         15 October 2026

def is_valid_time(text):
    #1.2 Return True if text looks like H:MM or HH:MM with a real time.
    parts = text.split(":")
    if len(parts) != 2:                       # need exactly one colon
        return False
    hours, minutes = parts
    if not (hours.isdigit() and minutes.isdigit()):
        return False
    if len(hours) not in (1, 2) or len(minutes) != 2:
        return False
    return 0 <= int(hours) <= 23 and 0 <= int(minutes) <= 59


def get_time():
    #1.1 Ask the user for a time until a valid one is entered.
    time_str = input("Enter the time: ").strip()
    while not is_valid_time(time_str):
        print("Invalid time. Use H:MM or HH:MM, e.g. 1:02 or 12:56.")
        time_str = input("Enter the time: ").strip()
    return time_str


if __name__ == "__main__":
    print("You entered:", get_time())
