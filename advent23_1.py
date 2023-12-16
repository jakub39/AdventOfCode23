subor = open("advent23_1.txt", "r").readlines()

vsetko = 6
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


for riadok in subor:
    digit_count = sum(1 for digit in digits if digit in riadok)
    if digit_count >= 2:
        for digit in digits:
            if digit in riadok:
                riadok = riadok.replace(digit, digit+" ")

    riadok = riadok.replace("one", "1")
    riadok = riadok.replace("two", "2")
    riadok = riadok.replace("three", "3")
    riadok = riadok.replace("four", "4")
    riadok = riadok.replace("five", "5")
    riadok = riadok.replace("six", "6")
    riadok = riadok.replace("seven", "7")
    riadok = riadok.replace("eight", "8")
    riadok = riadok.replace("nine", "9")
    cisla = (filter(str.isdigit, riadok))
    cisla = list(map(int, cisla))
    s = ""
    s += str(cisla[0])
    s += str(cisla[-1])
    vsetko += int(s)
    
print(vsetko)

