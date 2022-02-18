def startswith_capital_counter(names):
    title_count = 0
    for name in names:
        if name.istitle():
            title_count += 1

    return title_count

