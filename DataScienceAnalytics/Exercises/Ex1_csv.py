import csv

filename = "donnees_communes.csv"

# Load CSV data without pandas
def load_csv(filename, delimiter=';'):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        data = [row for row in reader]
    return data

data = load_csv(filename)

def convert_coddep(data):
    for row in data:
        try:
            row['CODDEP'] = int(row['CODDEP'])
        except ValueError:
            # If it fails, return the original value
            pass
    return data

convert_coddep(data)

# Exercise 1 OK
for row in data:
    row['PTOT'] = int(row['PTOT'])
    
def totalPopulation(data):
    total = sum(row['PTOT'] for row in data)
    print(f"The total population is: {total}")
    return total

totalPopulation(data)

# Exercise 2 OK
def totalPopulationDepartment(data, dep):
    dep = str(dep)  # Convert the input department code to string
    total = 0 
    for row in data:
        if str(row.get('CODDEP')) == dep:
            total += int(row['PTOT'])
    print(f"The total population in department {dep} is: {total}")
    return total

totalPopulationDepartment(data, "2A")
totalPopulationDepartment(data, 1)

# Exercise 3 OK
def populationByCom(data, dep):
    dep = str(dep)
    coms = [(row['COM'], row['PTOT']) for row in data if str(row['CODDEP']) == dep]
    sorted_coms = sorted(coms, key=lambda x: int(x[1]))[:10]
    print(f"Ten communities with the lowest population in dep {dep} are: {sorted_coms}")
    return sorted_coms

populationByCom(data, '1')

# Exercise 4 OK
def totalPopulationMulti(data, deps):
    deps = set(map(str, deps))
    total = sum(int(row['PTOT']) for row in data if str(row['CODDEP']) in deps)
    print(f"The total population in departments {', '.join(deps)} is: {total}")
    return total

departments = [1, 2, 11]
totalPopulationMulti(data, departments)

# Exercise 5 OK
def mostPopulated(data, deps):
    dep_pop = {}
    deps = set(map(str, deps))
    for row in data:
        if str(row['CODDEP']) in deps:
            dep_pop[row['CODDEP']] = dep_pop.get(row['CODDEP'], 0) + int(row['PTOT'])
    most_pop_dep = max(dep_pop, key=dep_pop.get)
    print(f"Department {most_pop_dep} has the largest population of {dep_pop[most_pop_dep]}")
    return most_pop_dep, dep_pop[most_pop_dep]

departments = ["2A", "4", "11"]
mostPopulated(data, departments)

# Exercise 6 OK 
def lowerThan(data, number):
    unique_deps = set(row['CODDEP'] for row in data)
    dep_list = []
    for dep in unique_deps:
        dep_population = totalPopulationDepartment(data, dep)
        if dep_population < number:
            dep_list.append(dep)
    print(f"Departments with population lower than {number}: {dep_list}")
    return dep_list

lowerThan(data, 200000)

# Exercise 7 OK
def totalPopulationByRegion(data, reg):
    reg = str(reg)
    total = sum(row['PTOT'] for row in data if row['REG'] == reg)
    return reg, total

def mostAndLeastRegions(data):
    regions = set(row['REG'] for row in data)
    region_pops = [totalPopulationByRegion(data, reg) for reg in regions]
    sorted_regions = sorted(region_pops, key=lambda x: x[1])
    least, most = sorted_regions[0], sorted_regions[-1]
    print(f"Least populated region: {least}, most populated region: {most}")
    return least, most

mostAndLeastRegions(data)

# Exercise 8 Maybe ok????
def onlyOverTen(data):
    over_10k = [row for row in data if row['PTOT'] > 10000]
    with open("Over10K.csv", "w", newline='', encoding='utf-8') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(over_10k)
    print("Completed")

onlyOverTen(data)

# Exercise 9 OK
def populationByDepartment(data, dep_list):
    dep_pop_dict = {}
    for dep in dep_list:
        dep_pop = totalPopulationDepartment(data, dep)
        dep_pop_dict[dep] = dep_pop
    return dep_pop_dict

print(populationByDepartment(data, [3, 6, 82]))
