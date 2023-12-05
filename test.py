import re
if __name__ == '__main__':

    input = """400..300..
...*...*."""

    lines = input.splitlines()

    symbolList = '*'
    i =0
    j = 0
    symbolatpos = -3
    arraylist = []
    previousline = ''
    numbers_at_pos = []
    numbers_at_posPrev= []
    totalsum = 0
    for line in lines:
        j=0
        for char in line:
            if char.isdigit():
                numbers_at_pos.append(j)
            j += 1
            ## check if some thing from the list is in the the line and where--> list of symbolsatpos

        for m in re.finditer('*#', line):
            arraylist= arraylist.append(int(m.start()))
        if symbolList in line:
            symbolatpos = line.find(symbolList)
        i += 1
        print(f"Arraylist {arraylist}")
        k =0
        symbolatposList = [3,8]
        if not previousline== '':

            for number in numbers_at_posPrev:
                for symbolindex in symbolatposList:
                    if (number == symbolindex) or ((number+1) == symbolindex) or ((number-1) == symbolindex):
                        print(f"{numbers_at_posPrev}")
                        index_found_connected = numbers_at_posPrev.index(number)
                        index_smallest = 9999
                        index_biggest =numbers_at_posPrev[index_found_connected]
                        indexNumber = index_found_connected
                        b = index_found_connected
                        while b > 0:
                            print(f"Number {number}, index={index_found_connected};{numbers_at_posPrev[b-1]};{(b)}")
                            if numbers_at_posPrev[b-1] == numbers_at_posPrev[b]-1:
                                b = b - 1
                                index_smallest = numbers_at_posPrev[b]
                            else:
                                b=0

                        b = index_found_connected
                        while b < (len(numbers_at_posPrev)-1):
                            if numbers_at_posPrev[b+1] == numbers_at_posPrev[b]+1:
                                b += 1
                                index_biggest = numbers_at_posPrev[b]
                            else:
                                b=len(previousline)
                        totalsum += int(previousline[index_smallest:index_biggest+1])

        previousline = line
        numbers_at_posPrev = numbers_at_pos
    print(f"Totalsum = {totalsum}")
