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


if __name__ == "__main__":
    # Tiny stand-in table so this section can be tested alone.
    demo = {"1": [" 1 ", "11 ", " 1 ", " 1 ", "111"],
            ":": [" ", ":", " ", ":", " "]}
    print_rows(build_rows("1:1", demo))
