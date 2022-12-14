'''
Elves are bringing food with them as they prepare to go searching in the woods for stars. Each elf carries a variable
number of items, each with a calorie count.  Data is contained in input.txt. Data looks like:
1000
1000

3000

4000
......
where a blank line represents a delimiter between elfs.

Problem: parse the data and find the elf carrying the largest total number of calories.
Bonus: get the total of the calories carried by the 3 most caloric carrying elves.
'''
elf_calories = []
curr_elf = 0
with open('input.txt') as elf_data:
    for line in elf_data:
        if line != '\n':
            curr_elf += int(line)
        else:
            elf_calories.append(curr_elf)
            curr_elf = 0
elf_calories.sort()
top_elves = elf_calories[-3:]
print(max(elf_calories))
print(top_elves)
print(sum(top_elves))

