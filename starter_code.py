import os


def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_list(numbers[1:])


def count_even(numbers):
    if len(numbers) == 0:
        return 0
    if numbers[0] % 2 == 0:
        return 1 + count_even(numbers[1:])
    return count_even(numbers[1:])


def find_strings_with(strings, target):
    if len(strings) == 0:
        return []

    first = strings[0]
    rest = find_strings_with(strings[1:], target)

    if target in first:
        return [first] + rest
    return rest


def count_files(directory_path):
    if os.path.isfile(directory_path):
        return 1

    count = 0
    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)
        count += count_files(full_path)

    return count


def find_infected_files(directory_path, extension=".encrypted"):
    if os.path.isfile(directory_path):
        if directory_path.endswith(extension):
            return [directory_path]
        return []

    infected = []
    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)
        infected.extend(find_infected_files(full_path, extension))

    return infected


if __name__ == "__main__":
    print("RECURSION ASSIGNMENT - STARTER CODE")

    print("\nTest sum_list:")
    print(sum_list([1, 2, 3, 4]))

    print("\nTest count_even:")
    print(count_even([1, 2, 3, 4, 5, 6]))

    print("\nTest find_strings_with:")
    print(find_strings_with(["hello", "world", "help"], "hel"))

    print("\nTotal files (breach_data):", count_files("breach_data"))
    print("Total infected files:", len(find_infected_files("breach_data")))

    print("\nFinance infected:", len(find_infected_files("breach_data/Finance")))
    print("HR infected:", len(find_infected_files("breach_data/HR")))
    print("Sales infected:", len(find_infected_files("breach_data/Sales")))

# ============================================================================
# PART 2: COUNT ALL FILES
# ============================================================================


def count_files(directory_path):
    if os.path.isfile(directory_path):
        return 1

    count = 0
    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)
        count += count_files(full_path)

    return count


# ============================================================================
# PART 3: FIND INFECTED FILES
# ============================================================================


def find_infected_files(directory_path, extension=".encrypted"):
    if os.path.isfile(directory_path):
        if directory_path.endswith(extension):
            return [directory_path]
        return []

    infected = []
    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)
        infected.extend(find_infected_files(full_path, extension))

    return infected


# ============================================================================
# TESTING & BENCHMARKING
# ============================================================================

if __name__ == "__main__":
    print("RECURSION ASSIGNMENT - STARTER CODE")
    print("Complete the functions above, then run this file to test your work.\n")

    print("\nTest sum_list:")
    print(sum_list([1, 2, 3, 4]))  # 10
    print(sum_list([]))  # 0

    print("\nTest count_even:")
    print(count_even([1, 2, 3, 4, 5, 6]))  # 3
    print(count_even([1, 3, 5]))  # 0

    print("\nTest find_strings_with:")
    print(find_strings_with(["hello", "world", "help"], "hel"))  # ['hello', 'help']

    print("\nTotal files (Test Case 1):", count_files("test_cases/case1_flat"))  # 5
    print("Total files (Test Case 2):", count_files("test_cases/case2_nested"))  # 4
    print("Total files (Test Case 3):", count_files("test_cases/case3_infected"))  # 5

    print(
        "Total Infected Files (Test Case 1):",
        len(find_infected_files("test_cases/case1_flat")),
    )  # 0
    print(
        "Total Infected Files (Test Case 2):",
        len(find_infected_files("test_cases/case2_nested")),
    )  # 0
    print(
        "Total Infected Files (Test Case 3):",
        len(find_infected_files("test_cases/case3_infected")),
    )  # 3
