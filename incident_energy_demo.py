# incident_energy_demo.py

def calculate_incident_energy(Ibf, t, D, Cf=1.0):
    """
    Estimate incident energy in cal/cm^2

    Parameters:
    Ibf (float): Bolted fault current (kA)
    t (float): Arcing time (seconds)
    D (float): Working distance (mm)
    Cf (float): Configuration factor (defaults to 1.0 for box-type equipment)

    Returns:
    float: Incident energy in cal/cm^2
    """
    return Cf * 0.0051 * Ibf**2 * t / (D / 10)**2


def main():
    print("⚡ ArcFlashPro – Incident Energy Calculator Demo ⚡")
    try:
        Ibf = float(input("Enter bolted fault current (kA): "))
        t = float(input("Enter arcing time (seconds): "))
        D = float(input("Enter working distance (mm): "))
        Cf = float(input("Enter configuration factor (e.g., 1.0): "))

        E = calculate_incident_energy(Ibf, t, D, Cf)
        print(f"\nEstimated Incident Energy: {E:.2f} cal/cm²")

        # Quick PPE suggestion
        if E < 1.2:
            level = "PPE Level 0 – Standard FR Clothing"
        elif E < 4:
            level = "PPE Level 1"
        elif E < 8:
            level = "PPE Level 2"
        elif E < 25:
            level = "PPE Level 3"
        else:
            level = "PPE Level 4+ (High Risk – Extreme Hazard)"
        print(f"Suggested PPE Category: {level}")

    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()
