def get_rate(gallons):
    if gallons <= 3000:
        return 3
    elif gallons <= 15000:
        return 4
    elif gallons <= 29000:
        return 5
    elif gallons <= 49000:
        return 6
    else:
        return 8

def calculate_charge(gallons, rate):
    return (gallons / 1000) * rate

months = ("january", "february", "march")
gallons_used = []  # Changed from tuple () to list []

for month in months:
    gallon = int(input(f"Enter gallons of water used in {month}:  "))
    gallons_used.append(gallon)  # Fixed variable name and changed to 'append'

for i in range(3):
    rate = get_rate(gallons_used[i])  # Removed extra parenthesis
    charge = calculate_charge(gallons_used[i], rate)
    print(f"{months[i].capitalize()}: {gallons_used[i]} gallons, Rate: ${rate}, Charge: ${charge:.2f}")

highest_usage = max(gallons_used)
average_usage = sum(gallons_used) / 3

print(f"Highest water usage: {highest_usage} gallons")
print(f"Average water usage: {average_usage:.2f} gallons")
