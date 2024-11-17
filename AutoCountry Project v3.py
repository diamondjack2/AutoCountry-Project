AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

def print_vehicles():
    print("The AutoCountry sales manager has authorized the purchase and sale of the following vechicles:")
    for vehicle in AllowedVehiclesList:
        print("- " + vehicle)

def search_vehicle():
    search_term = input("Please enter full Vehicle name: ")
    if search_term in AllowedVehiclesList:
        print(f"{search_term} is an authorized vehicle.")
    else:
        print(f"{search_term} is not an authorized vehicle, if you received this in error please check the spelling and try again")

def add_vehicle():
    new_vehicle = input("Please Enter the full Vehicle name you would like to add:")
    AllowedVehiclesList.append(new_vehicle) 
    print(f"You have added \"{new_vehicle}\" as an authorized vehicle")
          
def show_menu():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.2")
    print("********************************")
    print("Please Enter the following number below the following menu:")
    print(" ")
    print("1. PRINT all Allowed Vehicles")
    print("2. Search for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter 1, 2, 3, or 4:") 

        if choice == '1': 
            print_vehicles() 
        elif choice == '2':
            search_vehicle()
        elif choice == '3':
            add_vehicle()
        elif choice == '4': 
            print("Thank you for using AutoCountry Vehicle Finder, good-bye!") 
            break  
        else:
            print("Please enter 1, 2, 3 or 4.") 

main()
