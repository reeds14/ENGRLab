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


if __name__ == "__main__":
    patterns = merge_patterns(build_digits_5_to_9(), {":": [" ", ":", " ", ":", " "]})
    print(sorted(patterns))
    for row in patterns["7"]:
        print("|" + row + "|")
