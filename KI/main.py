# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.de
def fig(n):
    if(n == 1):
        return 1
    if(n == 2):
        return 1
    return fig(n-1)+fig(n-2)

print(fig(13))

print(3/3+3)
print(3+3/3)
print(3+3*3+3)

def nfak(n):
    if n <= 0:
        return 1
    return n*nfak(n-1)

print(nfak(9))

class Rechteck:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def flaeche(self):
        return self.a*self.b


eck = Rechteck(3 ,5)

print(eck.flaeche())

class Quadrat (Rechteck):
    def __init__(self, a):
        super().__init__(a, a)
        self.a = a
        self.b = a


qua  = Quadrat(5)

print(qua.flaeche())