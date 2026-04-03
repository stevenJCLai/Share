import sys
from ase.units import Hartree

while True:
    Total_energy = input("Please type in total energy (a.u.) or type Q to exit = ").strip()
    if Total_energy.upper() == "Q" or Total_energy == "":
        sys.exit()

    try:
        TE = round(float(Total_energy)*Hartree, 3)
        print(f"Total enery = {TE} eV.")
        continue
    
    except ValueError:
        print(f"'{Total_energy}' is not a valid number. Try again.")
        continue