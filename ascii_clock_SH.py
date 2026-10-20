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


if __name__ == "__main__":
    for ch, rows in {**build_digits_0_to_4(), **build_colon()}.items():
        print(ch)
        for row in rows:
            print("|" + row + "|")
