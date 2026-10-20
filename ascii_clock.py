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


def build_digits_0_to_4():
    #2.1 Return the 5-row, 3-column patterns for digits 0 through 4.
    return {
        "0": ["000",
              "0 0",
              "0 0",
              "0 0",
              "000"],
        "1": [" 1 ",
              "11 ",
              " 1 ",
              " 1 ",
              "111"],
        "2": ["222",
              "  2",
              "222",
              "2  ",
              "222"],
        "3": ["333",
              "  3",
              "333",
              "  3",
              "333"],
        "4": ["4 4",
              "4 4",
              "444",
              "  4",
              "  4"],
    }


def build_colon():
    #2.2 Return the 1-column colon pattern (dots on rows 2 and 4).
    return {":": [" ", ":", " ", ":", " "]}


def build_digits_5_to_9():
    #2.3 Return the 5-row, 3-column patterns for digits 5 through 9.
    return {
        "5": ["555",
              "5  ",
              "555",
              "  5",
              "555"],
        "6": ["666",
              "6  ",
              "666",
              "6 6",
              "666"],
        "7": ["777",
              "  7",
              "  7",
              "  7",
              "  7"],
        "8": ["888",
              "8 8",
              "888",
              "8 8",
              "888"],
        "9": ["999",
              "9 9",
              "999",
              "  9",
              "999"],
    }


def merge_patterns(*pattern_dicts):
    #2.4 Combine several pattern dictionaries into one lookup table.
    patterns = {}
    for d in pattern_dicts:
        patterns.update(d)
    return patterns


HEIGHT = 5      # every character is drawn 5 rows tall


def build_rows(time_str, patterns):
    #3.1 For each of the 5 output rows, join the matching slice of every character's pattern with a single space between characters.
    rows = []
    for row_num in range(HEIGHT):
        pieces = []
        for ch in time_str:
            pieces.append(patterns[ch][row_num])
        rows.append(" ".join(pieces))
    return rows


def print_rows(rows):
    #3.2 Print the finished rows, one per line.
    for row in rows:
        print(row)


def main():
    # Shared variables (see ascii_clock_planning.pdf, section 2)
    time_str = get_time()                                   # node 1
    patterns = merge_patterns(build_digits_0_to_4(),        # nodes 2.1-2.4
                              build_colon(),
                              build_digits_5_to_9())
    rows = build_rows(time_str, patterns)                   # node 3.1
    print_rows(rows)                                        # node 3.2


if __name__ == "__main__":
    main()
