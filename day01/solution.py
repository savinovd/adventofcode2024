from collections import Counter


def read_columns(file_path):
    left_col = []
    right_col = []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = line.strip().split()
            left_col.append(int(left))
            right_col.append(int(right))

    return left_col, right_col


def total_distance(left, right):
    return sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))


def similarity_score(left, right):
    right_counts = Counter(right)
    return sum(num * right_counts[num] for num in left)


left, right = read_columns("day01/input.txt")
print("Total distance:", total_distance(left, right))
print("Similarity score:", similarity_score(left, right))