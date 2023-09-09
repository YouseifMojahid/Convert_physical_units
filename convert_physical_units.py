def see_units():
    available = input("Do you want to the units (yes / no)? ")

    if available == "yes":
        print("g = Giga")
        print("m = Mega")
        print("k = kilo")
        print("h = Hecto")
        print("c = Centi")
        print("mm = milli")
        print("mmm = Micro")
        print("p = Vento")
    elif available == "No":
        print("Okay, it's up to you")
    else:
        print("Sorry but I can't understand you")

see_units()

first_unit = input("The first unit is: ")
done = True

match first_unit:
    case "g":
        g = 9
        first_unit = g
    case "m":
        m = 6
        first_unit = m
    case "k":
        k = 3
        first_unit = k
    case "h":
        h = 2
        first_unit = h
    case "c":
        c = -2
        first_unit = c
    case "mm":
        mm = -3
        first_unit = mm
    case "mmm":
        mmm = -6
        first_unit = mmm
    case "n":
        n = -9
        first_unit = n
    case "p":
        p = -12
        first_unit = p
    case _:
        done = False
        print("Please write a correct unit")

if done == True:
    second_unit = input("The second unit is: ")
    match second_unit:
        case "g":
            g = 9
            second_unit = g
        case "m":
            m = 6
            second_unit = m
        case "k":
            k = 3
            second_unit = k
        case "h":
            h = 2
            second_unit = h
        case "c":
            c = -2
            second_unit = c
        case "mm":
            mm = -3
            second_unit = mm
        case "mmm":
            mmm = -6
            second_unit = mmm
        case "n":
            n = -9
            second_unit = n
        case "p":
            p = -12
            second_unit = p
        case _:
            print("Please write a correct unit")

    print(f"10({int(first_unit) - int(second_unit)})")
