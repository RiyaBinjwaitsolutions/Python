month=int(input("Enter Month Number: "))
match month:
    case 1 | 12 | 2:
        print("Winter")
    case 3 | 4 | 5:
        print("Summer")
    case 6 | 7 | 8:
        print("Monsoon")
    case 9 | 10 | 11:
        print("Autumn")
    case _:
        print("Invalid Month")
