def parse_disk_map(disk_map):
    disk = []
    free_spaces = []
    file_id = 0
    for i, char in enumerate(disk_map):
        x = int(char)
        if i % 2 == 0:
            disk.extend([file_id] * x)
            file_id += 1
        else:
            free_spaces.extend(len(disk) + j for j in range(x))
            disk.extend([-1] * x)
    return disk, free_spaces


def compact_disc(disk, free_spaces):
    for i in free_spaces:
        if len(disk) <= i: 
            break
        while disk[-1] == -1:
            disk.pop()
        disk[i] = disk.pop()
    return disk


def checksum(disk):
    return sum(i * x for i, x in enumerate(disk))


# disk_map = "12345"
with open("day09/input.txt") as input_file:
    disk_map = input_file.read().strip() 
print(disk_map)
disk, frees = parse_disk_map(disk_map=disk_map)
print(frees)
print(disk)
compacted = compact_disc(disk, frees)
print(checksum(compacted))
