def list_sum(some_list):
    if some_list == []:
        return 0
    # base case
    else:
        return some_list.pop(0) + list_sum(some_list)
    # recursive case