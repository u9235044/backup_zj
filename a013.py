"""
Input
每個輸入檔中會有一個或以上的測試資料。每一行由兩個數字組成一筆測試資料，且所有數字將會小於4,000。檔案最後會以符號 # 表示結束。
Output
每筆測試資料的答案必須輸出到檔案中，並且換行。如果答案為零，則須輸出字串 ZERO。

羅馬數字規律
1. 左到右
2. 最多連續出現三個同樣字母, 所以 4 = 5 - 1, 9 = 10 - 1
"""

ROMAN_NUMBER = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


ROMAN_NUMBER_SPECIFIC = {
    "CM": 900,
    "CD": 400,
    "XC": 90,
    "XL": 40,
    "IX": 9,
    "IV": 4,
}


def convert_int_to_roman(int_to_convert):
    # the input will be 0 to 3999
    if int_to_convert == 0:
        return 'ZERO'
    else:
        result = ''
        while int_to_convert > 0:
            for r, i in ROMAN_NUMBER.items():                
                if int_to_convert >= i:
                    int_to_convert = int_to_convert - i
                    result = result + r
                    break
            #print(result)
            #print(int_to_convert)            
        return result


def convert_roman_to_int(roman_string):
    if len(roman_string) == 0:
        return 0
    elif len(roman_string) == 1:
        return ROMAN_NUMBER[roman_string]
    else:
        # from left to right
        #roman_array = list(roman_string)
        result = 0
        specific_check = False
        while_count = 0
        #for i in range(len(roman_array)):
        while not roman_string == '':
            while_count = while_count + 1
            #print("while_count: " + str(while_count))
            for r, j in ROMAN_NUMBER_SPECIFIC.items():
                if roman_string.find(r) == 0:
                    #print('before: ' + roman_string)
                    #print(r)
                    #print(j)
                    result = result + j
                    roman_string = roman_string[2:len(roman_string)]
                    #print('after: ' + roman_string)
                    #print(r)
                    #print(j)
                    specific_check = True
                    break
            
            if specific_check:
                pass
                #print('skip signle char check')
            else:
               for r, j in ROMAN_NUMBER.items():
                if roman_string.find(r) == 0:
                    #print('before: ' + roman_string)
                    #print(r)
                    #print(j)
                    result = result + j
                    roman_string = roman_string[1:len(roman_string)]
                    #print('after: ' + roman_string)
                    #print(r)
                    #print(j)
                    break
            
            specific_check = False

        return result


def roman_devide(single_row_input):
    #print(single_row_input)
    number_a = convert_roman_to_int(single_row_input.split(' ')[0])
    number_b = convert_roman_to_int(single_row_input.split(' ')[1])
    #print('number_a: ' + str(number_a))
    #print('number_b: ' + str(number_b))
    if number_a == number_b :
        return "ZERO"
    elif number_a > number_b:
        result = number_a - number_b
    elif number_b > number_a:
        result = number_b - number_a

    #print('result: ' + str(result))
    result_in_roman = convert_int_to_roman(result)
    #print('result_in_roman: ' + result_in_roman)

    return result_in_roman


def main():
    test_input = "MM IV"
    result = roman_devide(test_input)
    #result = convert_roman_to_int("MCMXCIV")
    #result = convert_int_to_roman(20)
    print(result)    


def main_zj():
    result = ''
    while True:
        try:
            s = input()
            temp = roman_devide(s)
            result = result + temp + '\n'
        except:
            break
    print(result)


if __name__ == '__main__':
    main()