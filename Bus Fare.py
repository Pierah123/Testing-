def calculate_bus_fare():
    # Constants
    base_fare = 5.00
    fare_per_stop = 2.50

    # Get input from user
    start_stop = int(input("What number stop are you at? "))
    end_stop = int(input("What is the stop you want to go to? "))

    # Calculate number of stops travelled
    num_stops = abs(end_stop - start_stop)

    # Calculate total fare
    total_fare = base_fare + (fare_per_stop * num_stops)

    # Output result
    print(f"The fare from Stop {start_stop} to Stop {end_stop} is ${total_fare:.2f}")

# Run the function
calculate_bus_fare()
