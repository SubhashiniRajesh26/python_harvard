def calculateEnergy(mass):
    c = 300000000
    energy = mass * c**2
    return energy

def main():
    mass = int(input("enter the mass in kilograms: "))
    print(calculateEnergy(mass))


main()