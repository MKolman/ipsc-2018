switch_limit, size_limit = None, (1, 25)
# switch_limit, size_limit = 2, (4, 4)
t = int(input())
for _ in range(t):
    input()
    n = int(input())
    line = input().split()
    switches = dict()

    def get_prefix(i):
        result = []
        j = 1
        while j * j <= i:
            if i % j == 0:
                result.append(switches.get(j, ''))
            j += 1
        return ''.join(result)

    def new_rule(i, label):
        if not label.isalpha():
            # print('    NotAlpha', i, label)
            return False
        if switch_limit and len(switches) >= switch_limit:
            # print('    Too many', i, label)
            return False
        if size_limit[0] <= len(label) <= size_limit[1]:
            switches[i] = label
            return True
        # print('    Too big', i, label)
        return False

    for i, label in enumerate(line):
        i += 1
        prefix = get_prefix(i)
        if label.lower() != label or not label.startswith(prefix):
            # print('if label.lower() != label:', i, label, prefix)
            break
        if not (label.isalpha() or label == str(i)):
            # print('if not (label.isalpha() or label == str(i)):', i, label, prefix)
            break

        if prefix == '':
            if label != str(i) and new_rule(i, label) is False:
                # print('if new_rule(i, label) is False:', i, label, prefix)
                break
            continue

        if prefix == label:
            continue
        elif new_rule(i, label[len(prefix):]) is False:
            # print('elif new_rule(i, label[len(prefix):]) is False:', i, len(prefix), label[len(prefix):], label, prefix, switches)
            # print('  ', len(prefix), len(label), len(label[len(prefix):]), label, label[len(prefix):])
            break
    else:
        i += 1
    print(i-1)
