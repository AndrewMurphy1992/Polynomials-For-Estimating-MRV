  GNU nano 7.2                                  gnome.py                                           
def compute_root(a, n):
    if n <= 1:
        raise ValueError("n must be greater than 1 to avoid division by zero.")
    # Solves for x in: a * x^(n-1) = 1 -> x = a**(-1/(n-1))
    return a ** (-1 / (n - 1))

def generate_matching_a_values(root, n_min, n_max):
    results = []
    for n in range(n_min, n_max + 1):
        # Solves for the new 'a' given the constant root: a = x**(-(n-1))
        a = root ** (-(n - 1))
        results.append((n, a))
    return results

def main():
    print("--- Estimated MRV ---")
    a = float(input("Enter initial percentage (e.g., 0.85): "))
    n = int(input("Enter exponent/sets (e.g., 3): "))
    
    root = compute_root(a, n)
    print(f"\nImplied growth/decay root (x): {root:.6f}")
    
    n_min = int(input("\nEnter minimum sets for projection (must be > 1): "))
    n_max = int(input("Enter maximum sets for projection: "))
    
    print("\nMatching (n, a) pairs for the same root:")
    print("---------------------------------------")
    for target_n, a_val in generate_matching_a_values(root, n_min, n_max):
        print(f"Sets (n) = {target_n:2d}  ->  Required Decimal % (a) = {a_val:.6f}")

if __name__ == "__main__":
    main()

