largest_total_calories = 0
current_elf_calories = 0

elves = []

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if line == "":
            elves.append(current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories += int(line)

elves.sort()

print(elves[-1])
print(elves[-1] + elves[-2] + elves[-3])
