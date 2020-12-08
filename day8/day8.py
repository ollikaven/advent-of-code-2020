from copy import deepcopy

with open("day8/input.txt", "r") as file:
    _input = [x.strip().split(" ") for x in file.readlines()]


def run_boot_code(instructions):
    accumulator = 0
    i = 0
    run_log = []
    while i not in run_log:
        ins = instructions[i]
        run_log.append(i)
        if ins[0] == "nop":
            i += 1
        elif ins[0] == "acc":
            i += 1
            accumulator += int(ins[1])
        elif ins[0] == "jmp":
            i += int(ins[1])
        if i >= len(instructions):
            return [accumulator, True]
    return [accumulator, False]


def fix_corruption(init_input):
    ins = init_input[0]
    acc = 0
    for j, ins in enumerate(init_input):
        new_input = deepcopy(init_input)
        if ins[0] == "nop":
            new_input[j][0] = "jmp"
        elif ins[0] == "jmp":
            new_input[j][0] = "nop"
        result = run_boot_code(new_input)
        acc = result[0]
        if result[1] == True:
            break
    return acc


accumulator = run_boot_code(_input)[0]
print(f"0801: {accumulator}")
acc = fix_corruption(_input)
print(f"0802: {acc}")
