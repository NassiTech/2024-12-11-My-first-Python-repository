def begruessung(
    name,
):

    #  [def begruessung name: SyntaxError: expected '('] ->  () is missing
    # print(
    # "Hallo, " + Name)
    # IndentationError: expected an indented block after function definition on line 1
    # Name not defined -> should be name (not capitalized)
    print("Hallo, " + name)


def addiere_zahlen(a, b):  # SyntaxError: expected ':'    Colon missing ":"
    ergebnis = a + b
    # return ergebis  # ergebnis n missing otherwise undefined variable
    # NameError: name 'ergebis' is not defined. Did you mean: 'ergebnis'?
    return ergebnis


def subtrahiere_zahlen(a, b):  # substrahiere und nicht subtrahiere
    # return a - c             # result of substraction missing
    return a - b  # Variable c undefined


def main():  # SyntaxError: expected ':'    Colon missing ":"
    zahl1 = int(input("Gib eine Zahl ein: "))  # cast string to integer
    zahl2 = int(input("Gib eine weitere Zahl ein: "))

    summe = addiere_zahlen(zahl1, zahl2)
    print(
        "Die Summe ist: " + str(summe)
    )  # TypeError: can only concatenate str (not "int") to str

    differenz = subtrahiere_zahlen(zahl1, zahl2)
    print(
        "Die Differenz ist: " + str(differenz)
    )  # TypeError: can only concatenate str (not "int") to str

    begruessung("Max")


# if __name__ = "__main__":    # invalid syntax. Maybe you meant '==' or ':=' instead of '='?
if __name__ == "__main__":
    main()
