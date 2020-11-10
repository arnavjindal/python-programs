#make a loop in main_1() for printing line individualy instead of list and printing all lines instead of one line



def getdate():
    import datetime
    return str(datetime.datetime.now())


def Main():
    Name = int(input("Enter- 1,2,3 for Arnav, Jindal, Fam (RESPECTIVELY): "))
    Eat_Fit = int(input('For updating the Log Press 1 for Fitness , 2 for Eat-Log : '))
    if Name == 1:
        if Eat_Fit == 1:
            Fit_append = input("Updating in Aranv-Fitness: ")
            with open("Arnav_fit.txt", "a" ) as Arnav_fit:
                Arnav_fit.write("[")
                Arnav_fit.write(getdate())
                Arnav_fit.write("]  ")
                Arnav_fit.write(Fit_append + "\n")
                Arnav_fit.write("")
            print('Updated successfully')
        elif Eat_Fit == 2:
            eat_append = input("Updating in Arnav-Eat: ")
            with open("Arnav_eat.txt", "a" ) as Arnav_eat:
                Arnav_eat.write("[")
                Arnav_eat.write(getdate())
                Arnav_eat.write("]")
                Arnav_eat.write(" ")
                Arnav_eat.write(eat_append)
                Arnav_eat.write("\n")
            print('Updated successfully')
    elif Name == 2:
        if Eat_Fit == 1:
            Fit_append = input("Updating in Jindal-Fitness: ")
            with open("Jindal_fit.txt", "a" ) as Jindal_fit:
                Jindal_fit.write("[")
                Jindal_fit.write(getdate())
                Jindal_fit.write("]")
                Jindal_fit.write("  ")
                Jindal_fit.write(Fit_append)
                Jindal_fit.write("\n")
            print('Updated successfully')
        elif Eat_Fit == 2:
            eat_append = input("Updating in Jindal-Eat: ")
            with open("Jindal_eat.txt", "a" ) as Jindal_eat:
                Jindal_eat.write("[")
                Jindal_eat.write(getdate())
                Jindal_eat.write("]")
                Jindal_eat.write("  ")
                Jindal_eat.write(eat_append)
                Jindal_eat.write("\n")
            print('Updated successfully')
    elif Name == 3:
        if Eat_Fit == 1:
            Fit_append = input("Updating in Fam-Fitness: ")
            with open("Fam_fit.txt", "a" ) as Fam_fit:
                Fam_fit.write("[")
                Fam_fit.write(getdate())
                Fam_fit.write("]")
                Fam_fit.write("  ")
                Fam_fit.write(Fit_append)
                Fam_fit.write("\n")
            print('Updated successfully')
        elif Eat_Fit == 2:
            eat_append = input("Updating in Fam-Eat: ")
            with open("Fam_eat.txt", "a" ) as Fam_eat:
                Fam_eat.write("[")
                Fam_eat.write(getdate())
                Fam_eat.write("]")
                Fam_eat.write("  ")
                Fam_eat.write(eat_append)
                Fam_eat.write("\n")
            print('Updated successfully')


def Main_1():
    Name = int(input("Enter- 1,2,3 for Arnav, Jindal, Fam (RESPECTIVELY): "))
    Eat_Fit = int(input('For updating the Log Press 1 for fit , 2 for eat : '))
    if Name == 1:
        if Eat_Fit == 1:
            with open("Arnav_fit.txt") as A_open_fit:
                for i in A_open_fit:                #----------------------USING FOR LOOP IS BETTER APPROACH READING FILES----------------------#
                    print(i,end="")
                # print(A_open_fit.readlines())
        elif Eat_Fit == 2:

            with open("Arnav_eat.txt") as A_open_eat:
                print(A_open_eat.readlines())
    elif Name == 2:
        if Eat_Fit == 1:

            with open("Jindal_fit.txt") as Jindal_open_fit:
                print(Jindal_open_fit.readlines())
        elif Eat_Fit == 2:

            with open("Jindal_eat.txt" ) as Jindal_open_eat:
                print(Jindal_open_eat.readlines())
    elif Name == 3:
        if Eat_Fit == 1:

            with open("Fam_fit.txt" ) as Fam_open_fit:
                print(Fam_open_fit.readlines())
        elif Eat_Fit == 2:
            with open("Fam_eat.txt") as Fam_open_eat:
                print(Fam_open_eat.readlines())




a= input("you want to retrieve[R] or you want to log data[L]: ")
if a== "L":
    Main()
else:
    Main_1()