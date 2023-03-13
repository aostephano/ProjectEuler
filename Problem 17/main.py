# Using num2words library
# pip install num2words

from num2words import num2words

print(str(num2words(1000)).replace(" ", ""))

# myStr = "abcde"
# print(len(myStr))
mySum = 0



for i in range(1,1001):


    # print(str(num2words(i)).replace(" ", "").replace("-", ""))
    mySum += len(str(num2words(i)).replace(" ", "").replace("-", ""))

print(mySum)

# def numberToWords(number):
#     word = ''
#
#     numbers = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
#                6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
#                11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
#                15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
#                19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
#                50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
#                90: 'Ninety'}
#
#
#     return word

def test_say_number(data, expected_output):
    """Test cases for say_number(i)."""
    output = lambda anonFunc: print("Anon")
    assert output == expected_output, \
        "\n    for:      {}\n    expected: {}\n    got:      {}".format(
            data, expected_output, output)

