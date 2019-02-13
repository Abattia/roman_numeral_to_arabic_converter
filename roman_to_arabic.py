def to_arabic(a_roman):
    """
    Returns arabic number equivalent to a roman
    :arg a_roman: <str>
    Returns <int>
    """
    result = 0

    def leading_numeral_is(numeral):
        """
        Returns True if leading numeral is numeral
        :arg numeral: <str>
        Returns <boole>
        """
        return a_roman[:len(numeral)] == numeral

    def leading_numerals_remain():
        """
        Returns True if there are still leading numerals
        to be processed
        Returns <boole>
        """
        return len(a_roman) > 0

    def remove_leading_numeral(numeral):
        """
        Returns a_roman with leading numeral removed
        :arg numeral: <str>
        Returns <str>
        """
        return a_roman[len(numeral):]

    while leading_numerals_remain():

        for roman_symbol, arabic in [("M", 1000),
                                     ("CM", 900),
                                     ("D", 500),
                                     ("CD", 400),
                                     ("C", 100),
                                     ("XC", 90),
                                     ("L", 50),
                                     ("XL", 40),
                                     ("X", 10),
                                     ("IX", 9),
                                     ("V", 5),
                                     ("IV", 4),
                                     ("I", 1)]:

            if leading_numeral_is(roman_symbol):
                result += arabic
                a_roman = remove_leading_numeral(roman_symbol)

    return result
