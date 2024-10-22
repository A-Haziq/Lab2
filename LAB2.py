def display_main_menu():
    print("Enter some numbers e.g 5, 67, 23")

def calc_average(temp_list):
    return sum(temp_list) / len(temp_list) if len(temp_list) > 0 else 0
    
def get_user_input():
    x = input("Enter some numbers(seperate with commas): ")
    y = [float(num.strip()) for num in x.split(",")]
    return y

def find_min_max(temp_list):
    if not temp_list:
        return [None, None]
    return [min(temp_list), max(temp_list)]


def sort_temperature(temp_list):
    return sorted(temp_list)

def calc_median_temperature(temp_list):
    sorted_list = sorted(temp_list)
    n = len(sorted_list)

    if n % 2 == 1:
        return sorted_list[n // 2]
    
    else:
        mid1 = sorted_list[n // 2 -1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) /2

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

    average = calc_average(num_list)
    print(f"The average temperature is: {average}")

    min_max = find_min_max(num_list)
    print(f"The minimum and maximum temperatures are: {min_max}")

    sorted_temps = sort_temperature(num_list)
    print(f"The sorted temperatures are: {sorted_temps}")

    median = calc_median_temperature(num_list)
    print(f"The median temperature is: {median}")

if __name__ == "__main__":
    main()

