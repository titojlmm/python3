# Problem: Print the Number of Neutrons in an Atomic Nucleus
# 1. Print the atoms with its protons (Z)
atoms = ("Hydrogen", 1, "Helium", 2, "Lithium", 3, "Beryllium", 4, "Boron", 5, "Carbon", 6)
for i in atoms:
  print(i)

# 2.1 Supposing N = 2*Z - Check the type of the element (isinstance)
atoms = ("Hydrogen", 1, "Helium", 2, "Lithium", 3, "Beryllium", 4, "Boron", 5, "Carbon", 6)
for i in atoms:
  if isinstance(i, int):  # Is i an integer?
    j = i*2
    print("has ", i, "protons and ", j, " neutrons.")
  else:
    print("Element ", i)

# 2.1 Supposing N = 2*Z - Divide names and protons in even and uneven index elements
atoms = ("Hydrogen", 1, "Helium", 2, "Lithium", 3, "Beryllium", 4, "Boron", 5, "Carbon", 6)
for i in range(0, len(atoms)):
  if i % 2 == 1:
    j = atoms[i]*2
    print("has ", atoms[i], "protons and ", j, " neutrons.")
  else:
    print("Element ", atoms[i])
