class RomanConverter:
    def __init__(self):
        """
        Constructor for RomanConverter class.
        Initializes a dictionary of Roman numeral symbols and their corresponding integer values.
        """
        self.value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]

    def int_to_roman(self, num):
        """
        Converts an integer to a Roman numeral.
        
        :param num: The integer to be converted.
        :return: A string representing the Roman numeral equivalent of the integer.
        """
        roman_numeral = ""
        for value, symbol in self.value_map:
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral


# Example usage:
converter = RomanConverter()
number = int(input("Enter an integer: "))
roman_numeral = converter.int_to_roman(number)
print(f"The Roman numeral for {number} is {roman_numeral}.")