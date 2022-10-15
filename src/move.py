def get_move():
    while True:
        row = input("Enter Row:")
        if row.isnumeric():
            row = int(row)

        else:
            print("invalid input")
            continue

        if row > 3:
            print("invalid input")
            continue
        else:
            row = row - 1
            break

    while True:
        column = input("Enter Column:")
        if column.isnumeric():
            column = int(column)
        else:
            print("not a number")
            continue

        if column > 3:
            print("invalid input")
            continue
        else:
            column = column - 1
            break

    return row, column
