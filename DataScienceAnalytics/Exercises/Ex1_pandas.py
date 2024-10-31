import pandas as pd
filename = "donnees_communes.csv"
df = pd.read_csv(filename, delimiter=';') 

# Exercise 1
def totalPopulation(df):
    if 'PTOT' in df.columns:
        total = df['PTOT'].sum()  
        print(f"The total population is: {total}")
        return total

totalPopulation(df)

#EXERCISE 2 

#becacuse the CODDEP contains non-integers therefore automatically convers dep 1 to "01" etc; we want to avoid that
def convert_coddep(value):
    try:
        return int(value)
    except ValueError:
        # If it fails, return the original value
        return value

df['CODDEP'] = df['CODDEP'].apply(convert_coddep)


def totalPopulation(df, dep):
    total = 0  # Initialize total
    dep = str(dep)  # Ensure dep is a string for comparison
    for index, row in df.iterrows():  # Iterate over DataFrame rows
        if str(row["CODDEP"]) == dep:  # Compare CODDEP as a string
            total += row['PTOT']  # Add to total population
    print(f"The total population in dep {dep} is: {total}")  # Output result
    return dep,total 


totalPopulation(df, 1)
#total2 = totalPopulation(df, "2A")
#total2 = totalPopulation(df, 974) #870870
#total2 = totalPopulation(df, 75) #2182174

#EXERCISE 3 ------------------------------------


def populationByCom(df, dep):
    new_list = []  
    dep = str(dep) 
    for index, row in df.iterrows():  
        if str(row["CODDEP"]) == dep:
            #not sure if i should use PTOT here
            new_list.append((row["COM"], row["PTOT"]))
    sorted_list = sorted(new_list, key=lambda x: x[1])  # x[1] refers to the population
    answer = (sorted_list[:10])
    print("Ten coms with lowest population in dep " + str(dep) + " are: " + str(answer))
    return answer

populationByCom(df, 1)

#EXERCISE 4 ------------------------------------
def totalPopulationMulti(df, deps):
    total = 0  
    deps = [str(dep) for dep in deps]  
    
    for index, row in df.iterrows():  
        if str(row["CODDEP"]) in deps:  
            total += row['PTOT'] 
    
    print(f"The total population in departments {', '.join(deps)} is: {total}")  
    return total 


departments = [1, 2, 11]  
totalPopulationMulti(df, departments)

#EXERCISE 5 ------------------------------------

def mostPopulated(df, deps):
    population_dict = {}
    deps = [str(dep) for dep in deps]
    
    for index, row in df.iterrows():
        coddep = str(row["CODDEP"])  
        if coddep in deps:  # Check if the department code is in the list of departments
            if coddep in population_dict:  # If the department already exists, add the population
                population_dict[coddep] += row["PTOT"]
            else:  # Otherwise, initialize the population
                population_dict[coddep] = row["PTOT"]
 
    sorted_population = sorted(population_dict.items(), key=lambda x: x[1], reverse=True)
    answer =  sorted_population[0]
    print("Department " + str(answer[0]) + " has the biggest population of " + str(answer[1]))
    return answer

departments = ["2A", 4, 11]
mostPopulated(df, departments)


#EXERCISE 6 ------------------------------------

def lowerThan(number):
    unique_coddep = df["CODDEP"].unique() #Get all CODDEPS
    dep_list = []
    for i in unique_coddep: #make them into a list 
        dep_list.append(i)
    new_list = []
    for dep in dep_list:
        i = totalPopulation(df, dep) #use prev function to calculate population of each dep
        if (i[1]) < number:
            new_list.append(i)
       
    print("Deps with population lower than " + str(number) + " are: " + str(new_list))
    return new_list

lowerThan(200000)

#EXERCISE 7 ------------------------------------

def totalPopulationByRegion(df, reg):
    total = 0  
    reg = str(reg)  
    for index, row in df.iterrows():  
        if str(row["REG"]) == reg:  
            total += row['PTOT']  
    #print(f"The total population in dep {dep} is: {total}")  # Output result
    return reg,total 

def mostAndLeastRegions(df):
    unique_coddep = df["REG"].unique() #Get all CODDEPS
    reg_list = []
    for i in unique_coddep: #make them into a list 
        reg_list.append(i)
    
    reg_pop = []
    for region in reg_list:
        i = totalPopulationByRegion(df, region) #use prev function to calculate population of each dep
        reg_pop.append(i)
    
    sorted_regions = sorted(reg_pop, key=lambda x: x[1], reverse=False)  # Sort by population in descending order
    least =  sorted_regions[0]
    most =  sorted_regions[-1]
    print("Least populated region is " + str(least) + ", most populated is: " + str(most))
    return least,most

mostAndLeastRegions(df)

#EXERCISE 8 ------------------------------------
def onlyOverTenk(df):
    df_filtre = df[df["PTOT"] > 10000]
    df_filtre.to_csv("Over10K.csv", index=False)
    print(f"Completed")
    
onlyOverTenk(df)

#EXERCISE 8 ------------------------------------
def population_par_departement(df, dep_list):
    dictionary = {}
    for dep in dep_list:
        i = totalPopulation(df, dep) #use prev function to calculate population of each dep
        dictionary[i[0]] = i[1] #bec 0 is a dep number
    return dictionary



print(population_par_departement(df, [3,6,82]))
