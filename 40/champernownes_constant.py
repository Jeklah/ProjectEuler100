# project euler problem 40
# author: Jeklah


def champernownes_constant():
    """Find the value of the following expression:
    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000"""
    champernownes_constant = "".join(str(i) for i in range(1, 1000000))
    return int(champernownes_constant[0]) * int(champernownes_constant[9]) * int(champernownes_constant[99]) * int(champernownes_constant[999]) * int(champernownes_constant[9999]) * int(champernownes_constant[99999]) * int(champernownes_constant[999999])


if __name__ == "__main__":
    print(champernownes_constant())
