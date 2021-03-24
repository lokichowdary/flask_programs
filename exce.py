class Error(Exception):
    pass

class ValueToSmall(Error):
    pass

class ValueToLarge(Error):
    pass

class ZeroNotDivisible(Error):
    pass
