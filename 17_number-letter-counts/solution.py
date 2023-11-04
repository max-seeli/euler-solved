# Problem: 17
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

def number_to_english(x):
    if x == 1000:
        return "one thousand"
    elif x >= 100:
        return number_to_english(x // 100) + " hundred" + (" and " + number_to_english(x % 100) if x % 100 != 0 else "")
    elif x >= 20:
        return ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][x // 10 - 2] + ("-" + number_to_english(x % 10) if x % 10 != 0 else "")
    elif x >= 10:
        return ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen","eighteen", "nineteen"][x - 10]
    else:
        return ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][x]

print(sum(len(number_to_english(i).replace(" ", "").replace("-", "")) for i in range(1, 1001)))
