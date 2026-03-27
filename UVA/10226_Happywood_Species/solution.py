cases = int(input())
_ = input()

for i in range(cases):
    species = {}
    while 1:
        try:
            tree_name = input()
            if tree_name == "":
                break
            elif tree_name in species:
                species[tree_name] += 1
            else:
                species[tree_name] = 1
        except:
            break

    total_species = sum(species.values())

    for key in sorted(species.keys()):
        print(f"{key} {species[key] / total_species * 100:.4f}")

    if i != cases - 1:
        print()