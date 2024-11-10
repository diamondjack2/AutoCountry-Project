AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

def print_vehicles():
    print("The AutoCountry sales manager has authorized the purchase and sale of the following vechicles:")
    for vehicle in AllowedVehiclesList:
        print("- " + vehicle)

def show_menu():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below the following menu:")
    print(" ")
    print("1. PRINT all Allowed Vehicles")
    print("2. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter 1 or 2:") 

        if choice == '1': 
            print_vehicles() 
        elif choice == '2': 
            print("Thank you for using AutoCountry Vehicle Finder, good-bye!") 
            break  
        else:
            print("Please enter 1 or 2.") 

main()
