# project euler problem 40
# author: Jeklah


def champernownes_constant():
    """Find the value of the following expression:
    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000"""
    champernownes_const = "".join(str(i) for i in range(1, 1000000))
    return int(champernownes_const[0]) * \
        int(champernownes_const[9]) * \
        int(champernownes_const[99]) * \
        int(champernownes_const[999]) * \
        int(champernownes_const[9999]) * \
        int(champernownes_const[99999]) * \
        int(champernownes_const[999999])


if __name__ == "__main__":
    print(champernownes_constant())
