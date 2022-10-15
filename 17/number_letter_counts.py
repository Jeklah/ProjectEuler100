# project euler problem 17

def number_letter_counts():
    ones = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
    teens = {10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
    tens = {2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}
    hundred = 7
    thousand = 8
    count = 0
    for i in range(1, 1000):
        if i < 10:
            count += ones[i]
        elif i < 20:
            count += teens[i]
        elif i < 100:
            count += tens[i // 10]
            if i % 10 != 0:
                count += ones[i % 10]
        elif i < 1000:
            count += ones[i // 100] + hundred
            if i % 100 != 0:
                count += 3
                if i % 100 < 10:
                    count += ones[i % 100]
                elif i % 100 < 20:
                    count += teens[i % 100]
                else:
                    count += tens[(i % 100) // 10]
                    if (i % 100) % 10 != 0:
                        count += ones[(i % 100) % 10]
    count += ones[1] + thousand
    return count

if __name__ == '__main__':
    print(number_letter_counts())
