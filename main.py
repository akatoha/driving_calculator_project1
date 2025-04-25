
def driver_check():
    while True:
        while True:
            try:
                age = int(input("🔢 Enter your age: "))
                break
            except ValueError:
                print("❌ It must be a number!")

        while True:
            drive_license = input("🚗 Do you have a driver license? (1 - yes, 2 - no): ")
            if drive_license in ["1", "2"]:
                break
            else:
                print("❌ Enter only 1 or 2")

        if age >= 18 and drive_license == "1":
            print("✅ All good, you can drive!")
        elif age < 18 and drive_license == "2":
            print("⛔ You must be 18+ and have a license.")
        elif age < 18:
            print("⛔ You must be 18+.")
        else:
            print("⛔ You must have a driver license.")

        again = input("🔁 Restart? (1 - yes, 2 - no): ")
        if again != "1":
            break


def calculator():
    while True:
        while True:
            try:
                a = float(input("🔢 Enter first number: "))
                break
            except ValueError:
                print("❌ Not a number!")

        while True:
            try:
                b = float(input("🔢 Enter second number: "))
                break
            except ValueError:
                print("❌ Not a number!")

        while True:
            print("\n🔧 Choose operation:")
            print("1 — Addition (+)")
            print("2 — Subtraction (-)")
            print("3 — Multiplication (*)")
            print("4 — Division (/)")
            operation = input("Enter 1/2/3/4: ")

            if operation == "1":
                print(f"✅ Result: {a + b}")
                break
            elif operation == "2":
                print(f"✅ Result: {a - b}")
                break
            elif operation == "3":
                print(f"✅ Result: {a * b}")
                break
            elif operation == "4":
                try:
                    result = a / b
                    print(f"✅ Result: {result}")
                    break
                except ZeroDivisionError:
                    print("❌ Can't divide by zero!")
            else:
                print("❌ Invalid choice!")

        again = input("🔁 Try again? (y/n): ").lower()
        if again != "y":
            print("👋 Thank you for using the calculator!")
            break


# === Main Menu ===
while True:
    print("\n💼 ====== MAIN MENU ======")
    print("1 — 🧮 Calculator")
    print("2 — 🚘 Driver Check")
    print("3 — ❌ Exit")

    choice = input("Enter number (1/2/3): ")

    if choice == "1":
        calculator()
    elif choice == "2":
        driver_check()
    elif choice == "3":
        print("👋 Bye!")
        break
    else:
        print("❌ Invalid input. Try again.")
