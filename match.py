day=input("enter the number: ")

match(day) :

    case "1" | "2" | "3" | "4" | "5":

        print("weekdays")

    case "6"|"7":

        print("weekend")

    case _:

        print("invalid day")