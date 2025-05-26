def spam():
    global eggs
    eggs = 99
    def bacon():
        global eggs
        ham = 101
        eggs = 0
        print(eggs)
    bacon()
    print(eggs)


def bacon():
    ham = 101
    eggs = 98
    print(ham)

bacon()
spam()

spam()
