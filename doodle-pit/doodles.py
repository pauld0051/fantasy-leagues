for item_a in range(101, 0, -1):
    line = ""
    for item_b in range(-1, 100, item_a):
        line += "*"
    print(line)
