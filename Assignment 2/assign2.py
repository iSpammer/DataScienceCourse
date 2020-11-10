#!/usr/bin/env python3
import math
type = "0"
while True:
    try:
        type = input("For circle press 1, for rectangle press 2, to exit press 9\n")
        if type == "1":
            radius = int(input("Enter circle radius\n"))
            if radius <= 0:
                raise Exception("circle radius cannot be less then 0\n")
            else:
                print("Circle perimetre is: ", 2*math.pi*radius,"\n")
                break
        elif type == "2":
            rect_or_carre = input("for rectangle please enter 1, for square please enter 2\n")
            if rect_or_carre=="1":
                try:
                    long = int(input("Long == ?\n"))
                    lat = int(input("Lat == ?\n"))
                    if long <= 0 or lat <= 0:
                        raise Exception("long/lat cannot be less then 0")
                    print("Rectangle perimetre is: ", 2*(long+lat))
                    break
                except:
                    print("Error Ocurred, Please enter a valid number\n")
            elif rect_or_carre=="2":
                long = int(input("Long == ?\n"))
                if long <= 0:
                    raise Exception("long/lat cannot be less then 0")
                print("Square perimetre is: ", 4*(long))
                break
    
            else:
                print("Please enter a valid choise\n")
        elif type =="9":
            break
            exit(0)
        else:
            print("Please enter a valid choise\n")
    except:
        print("please enter a valid number")
                        
    