rules_limit, label_size_limit = None, (1, 25)
# rules_limit, label_size_limit = 2, (4, 4)
t = int(input())
for _ in range(t):
    input()
    n = int(input())
    line = input().split()
    switch_rules = dict()

    def get_prefix(i):
        result = []
        j = 1
        while j <= i:
            if i % j == 0:
                result.append(switch_rules.get(j, ''))
            j += 1
        return ''.join(result)

    def add_new_rule(i, label):
        if not label.isalpha():
            return False
        if rules_limit and len(switch_rules) >= rules_limit:
            return False
        if label_size_limit[0] <= len(label) <= label_size_limit[1]:
            switch_rules[i] = label
            return True
        return False

    for i, label in enumerate(line):
        i += 1
        prefix = get_prefix(i)
        if label.lower() != label or not label.startswith(prefix):
            break
        if not (label.isalpha() or label == str(i)):
            break

        if prefix == '':
            if label != str(i) and add_new_rule(i, label) is False:
                break
            continue

        if prefix == label:
            continue
        elif add_new_rule(i, label[len(prefix):]) is False:
            break
    else:
        i += 1
    print(i-1)
