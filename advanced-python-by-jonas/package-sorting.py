#1. Identify the size and weight of a package
#2. Categorise these packages in xs, s, m, l, xl
#3. Sort the packages based on size and weight
#4. Distribute the packages according to the size and weight 
#5. Create a model that shows the amount of packages of each size

# Define a function to categorize packages based on their size and weight
def categorize_package(size, weight):
    if size <= 10 and weight <= 5:
        return "xs"
    elif size <= 20 and weight <= 10:
        return "s"
    elif size <= 30 and weight <= 20:
        return "m"
    elif size <= 40 and weight <= 30:
        return "l"
    else:
        return "xl"

# Define a function to sort packages based on size and weight
def sort_packages(packages):
    # Sort packages by size first, then by weight
    sorted_packages = sorted(packages, key=lambda p: (p[0], p[1]))
    return sorted_packages

# Define a function to distribute packages based on their size and weight
def distribute_packages(packages):
    # Categorize packages based on their size and weight
    categorized_packages = [(size, weight, categorize_package(size, weight)) for (size, weight) in packages]
    
    # Sort packages based on their size and weight
    sorted_packages = sort_packages(categorized_packages)
    
    # Create a model to show the amount of packages of each size
    package_model = {}
    for (_, _, category) in sorted_packages:
        if category not in package_model:
            package_model[category] = 0
        package_model[category] += 1
    
    return package_model

# Define a list of packages, where each package is a tuple containing its size and weight
packages = [(25, 15), (30, 10), (35, 5), (40, 20), (45, 25)]

# Distribute and model the packages
package_model = distribute_packages(packages)

# Print the resulting package model
for (category, count) in package_model.items():
    print(f"Category {category}: {count} packages")
