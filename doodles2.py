def mutate_string(input_string, replacements):
    # Complete the function here
    t = list(zip(*replacements))
    return ''.join(map(lambda p: p[1] if p[0] not in t[0] else t[1][t[0].index(p[0])], enumerate(input_string)))


# Sample function call
input_string = 'hello world'
replacements = [(1, ''), (2, ''), (3, ''), (4, 'i')]
print(mutate_string(input_string, replacements))

input_string = 'Bacon and eggs'
replacements = [(0, 'P'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n'), (6, ' '),
                (7, 'i'), (8, 's'), (9, ' '), (10, 'f'), (11, 'u'), (12, 'n'), (13, '!')]
print(mutate_string(input_string, replacements))
