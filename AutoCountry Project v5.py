# VERSION 5

FILE_PATH = "/Users/jackdiamond/Documents/HCC/HCC Programming Logic/Auto Country Project/allowed_vehicles.txt"

def load_allowed_vehicles():
    try:
        with open(FILE_PATH, 'r') as file:
            return file.read().splitlines() 
    except FileNotFoundError:
        print(f"{FILE_PATH} not found. Creating a new one.")
        with open(FILE_PATH, 'w') as file:
            pass  
        return []


def save_allowed_vehicles(vehicles):
    with open(FILE_PATH, 'w') as file:
        file.write('\n'.join(vehicles))  


def print_vehicles():
    vehicles = load_allowed_vehicles()
    print("The AutoCountry sales manager has authorized the purchase and sale of the following vehicles:")
    for vehicle in vehicles:
        print("- " + vehicle)

def search_vehicle():
    vehicles = load_allowed_vehicles()
    search_term = input("Please enter full Vehicle name: ")
    if search_term in vehicles:
        print(f"{search_term} is an authorized vehicle.")
    else:
        print(f"{search_term} is not an authorized vehicle. If you received this in error, please check the spelling and try again.")


def add_vehicle():
    vehicles = load_allowed_vehicles()
    new_vehicle = input("Please enter the full Vehicle name you would like to add: ")
    if new_vehicle not in vehicles:
        vehicles.append(new_vehicle)
        save_allowed_vehicles(vehicles)
        print(f"You have added \"{new_vehicle}\" as an authorized vehicle.")
    else:
        print(f"{new_vehicle} is already in the authorized list.")


def remove_vehicle():
    vehicles = load_allowed_vehicles()
    vehicle_to_remove = input("Please enter the full Vehicle name you would like to REMOVE: ")
    if vehicle_to_remove in vehicles:
        confirm_removal = input(f"Are you sure you want to remove \"{vehicle_to_remove}\" from the Authorized Vehicle List? (yes/no): ").lower()
        if confirm_removal == 'yes':
            vehicles.remove(vehicle_to_remove)
            save_allowed_vehicles(vehicles)
            print(f"You have REMOVED \"{vehicle_to_remove}\" as an authorized vehicle.")
        else:
            print("Removal cancelled.")
    else:
        print(f"{vehicle_to_remove} is not in the authorized list.")


def show_menu():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.5")
    print("********************************")
    print("Please enter the number below for the following menu:")
    print(" ")
    print("1. PRINT all Allowed Vehicles")
    print("2. Search for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("********************************")

        if choice == '1': 
            print_vehicles() 
        elif choice == '2':
            search_vehicle()
        elif choice == '3':
            add_vehicle()
        elif choice == '4':
            remove_vehicle()
        elif choice == '5': 
            print("Thank you for using AutoCountry Vehicle Finder, good-bye!") 
            break  
        else:
            print("Enter 1, 2, 3, 4, or 5:")

if __name__ == "__main__":
    main()
