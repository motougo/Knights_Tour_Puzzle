def last_indexof_max(numbers):
    max_pos = -1
    pos = 0
    for num in numbers:
        if max_pos == -1 and len(numbers):
            max_pos = 0
            max_num = num
        elif num >= max_num:
            max_pos = pos
            max_num = num
        pos += 1
    return max_pos
