def todec(number):
    if isinstance(number, int):
        number = str(number)
    if not all(x in '01' for x in number):
        return "Wrong input"
    line = number.lstrip('0')
    if len(line) <= 1:
        return int(number)
    else:
        line = line[1:]
        return 2 ** len(line) + todec(line)

x= int(input())
print(todec(x))
