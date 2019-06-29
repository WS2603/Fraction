class Fraction:
    def _reduce(self, n,d, sign):
        # function which will be used to reduce values of the numerator and denominator to
        # lowest common divider
        a = abs(n) # absolute value of numerator
        b = abs(d) # absolute value of denominator
    
        while a % b != 0: # whilst a mod b is not equal to zero
            tempA = a
            tempB = b
            a = tempB
            b = tempA % tempB
            # loops through reducing each value into a lower form
        ret_n = abs(n) // b * sign
        ret_d = abs(d) // b
        return (ret_n, ret_d)
    
    def _init_(self, numerator, denominator):
        if(not isinstance(numerator, int)):
            raise TypeError("The numerator of a Fraction must be an integer!")
        if(not isinstance(denominator, int)):
            raise TypeError("The denominator of a Fraction must be an integer!")
        if(denominator == 0):
            raise ZeroDivisionError("Denominator can't be Zero!")
        if(numerator == 0):
            self._numerator = 0
            self._denominator = 1
        else:
            if(numerator < 0 and denominator > 0) or (numerator >=0 and denominator < 0):
                sign -1
                else:
                        sign 1
                    (self._numerator, self._denominator) = self._reduce(numerator, denominator, sign)
    def __repr__(self):
        return ""+str(self.numerator)+"/"+str(self._denominator)

    def __plus__(self,rhs):
        lhs = self
        num = lhs.getNumerator() * rhs.getDenominator() + rhs.getNumerator() * lhs.getDenominator
        den = lhs.getDenominator * rhs.getDenominator()
        return Fraction(num,den)

    def __minus__(self,rhs):
        lhs = self
        num = lhs.getNumerator() * rhs.getDenominator() - rhs.getNumerator() * lhs.getDenominator
        den = lhs.getDenominator * rhs.getDenominator()
        return Fraction(num,den)

    def __mult__(self,rhs):
        lhs = self
        num = lhs.getNumerator() * rhs.getNumerator()
        den = lhs.getDenominator * rhs.getDenominator()
        return Fraction(num,den)

    def __div__(self,rhs):
        lhs = self
        num = lhs.getNumerator() * rhs.getDenominator()
        den = lhs.getDenominator * rhs.getNumerator()
        return Fraction(num,den)
