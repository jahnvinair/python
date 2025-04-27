def read_fuzzy_set(set_name):
    fuzzy_set = {}
    print(f"Enter elements and membership values for {set_name} (e.g., 'x1:0.5' for mu(x1)=0.5). Enter empty line to finish:")
    while True:
        line = input().strip()
        if not line:
            break
        try:
            element, value = line.split(':')
            value = float(value.strip())
            if 0 <= value <= 1:
                fuzzy_set[element.strip()] = value
            else:
                print("Membership value must be between 0 and 1.")
        except ValueError:
            print("Invalid input. Use format 'element:value'")
    return fuzzy_set

def fuzzy_demorgan_intersection(set1, set2):
    # Get all elements
    elements = set(set1.keys()) | set(set2.keys())
    # Compute intersection and its complement
    intersection = {e: min(set1.get(e, 0), set2.get(e, 0)) for e in elements}
    comp_intersection = {e: 1 - intersection[e] for e in elements}
    # Compute complements and their union
    comp1 = {e: 1 - set1.get(e, 0) for e in set1}
    comp2 = {e: 1 - set2.get(e, 0) for e in set2}
    union_comp = {e: max(comp1.get(e, 1), comp2.get(e, 1)) for e in elements}
    return comp_intersection, union_comp

def main():
    set1 = read_fuzzy_set("Set 1")
    set2 = read_fuzzy_set("Set 2")
    if not (set1 and set2):
        print("At least one set is empty.")
        return
    comp_intersection, union_comp = fuzzy_demorgan_intersection(set1, set2)
    print("Complement of Intersection:", {k: round(v, 2) for k, v in comp_intersection.items()})
    print("Union of Complements:", {k: round(v, 2) for k, v in union_comp.items()})
    if comp_intersection == union_comp:
        print("De Morgan's Law (Complement of Intersection = Union of Complements) holds.")
    else:
        print("De Morgan's Law does not hold (possible error in input).")

if __name__ == "__main__":
    main()