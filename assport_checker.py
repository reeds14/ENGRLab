# By submitting this assignment, all team members agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Reed Scott (UIN: 838002005)
#               Sho Hiroi (UIN: 837008392)
#               Xavier Gomez (UIN: 538001968)
#               Izaac Almeida (UIN: 238008017)
# Section:      553
# Assignment:   Lab 11A
# Date:         10 November 2026

def split_passports(content): #Split file content into passport blocks (lists of lines).
    blocks = []
    current = []
    for line in content.split('\n'):
        if line.strip() == '':
            if current:
                blocks.append(current)
                current = []
        else:
            current.append(line)
    if current:
        blocks.append(current)
    return blocks


def passport_keys(block): #Extract the set of field names present in a passport block.
    keys = set()
    for token in ' '.join(block).split():
        if ':' in token:
            keys.add(token.split(':', 1)[0])
    return keys


def main():
    filename = input("Enter the name of the file: ")
    with open(filename, 'r') as f:
        content = f.read()

    blocks = split_passports(content)
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'pid', 'cid'}

    valid_blocks = [b for b in blocks if required.issubset(passport_keys(b))]

    print(f"There are {len(valid_blocks)} valid passports")

    with open('valid_passports.txt', 'w') as out:
        for i, block in enumerate(valid_blocks):
            if i > 0:
                out.write('\n')
            out.write('\n'.join(block) + '\n')


main()