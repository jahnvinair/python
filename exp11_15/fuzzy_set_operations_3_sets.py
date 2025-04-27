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

def fuzzy_operations(set1, set2, set3):
    # Get all elements across sets
    elements = set(set1.keys()) | set(set2.keys()) | set(set3.keys())
    # Initialize result sets
    union = {}
    intersection = {}
    complement1 = {e: 1 - set1.get(e, 0) for e in set1}
    complement2 = {e: 1 - set2.get(e, 0) for e in set2}
    complement3 = {e: 1 - set3.get(e, 0) for e in set3}
    # Compute union and intersection
    for e in elements:
        union[e] = max(set1.get(e, 0), set2.get(e, 0), set3.get(e, 0))
        intersection[e] = min(set1.get(e, 0), set2.get(e, 0), set3.get(e, 0))
    return union, intersection, complement1, complement2, complement3

def main():
    set1 = read_fuzzy_set("Set 1")
    set2 = read_fuzzy_set("Set 2")
    set3 = read_fuzzy_set("Set 3")
    if not (set1 and set2 and set3):
        print("At least one set is empty.")
        return
    union, intersection, comp1, comp2, comp3 = fuzzy_operations(set1, set2, set3)
    print("Union:", {k: round(v, 2) for k, v in union.items()})
    print("Intersection:", {k: round(v, 2) for k, v in intersection.items()})
    print("Complement of Set 1:", {k: round(v, 2) for k, v in comp1.items()})
    print("Complement of Set 2:", {k: round(v, 2) for k, v in comp2.items()})
    print("Complement of Set 3:", {k: round(v, 2) for k, v in comp3.items()})

if __name__ == "__main__":
    main()
