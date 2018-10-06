from string import ascii_lowercase

t = int(input())
for _ in range(t):
    input()
    n = int(input())
    size = 1
    while (size * size) % n:
        size += 1
    repeat = size * size // n
    linear_map = ''.join(c * repeat for c in ascii_lowercase[:n])
    print(size)
    for start_idx in range(size):
        reverse = 1
        if start_idx % 2:
            reverse = -1
        line = ''.join(linear_map[start_idx*size:(start_idx+1)*size])
        print(line[::reverse])

