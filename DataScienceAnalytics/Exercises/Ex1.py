import pandas as pd
filename = "donnees_communes.csv"
df = pd.read_csv(filename, delimiter=';') 

# Exercise 1
def totalPopulation(df):
    if 'PTOT' in df.columns:
        total = df['PTOT'].sum()  
        return total

total = totalPopulation(df)
print(f"The total population is: {total}")

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
    return total 


total2 = totalPopulation(df, 1)
total2 = totalPopulation(df, "2A")
total2 = totalPopulation(df, 974) #870870
total2 = totalPopulation(df, 75) #2182174

#EXERCISE 3 ------------------------------------


def populationByCom(df, dep):
    new_list = []  
    dep = str(dep) 
    for index, row in df.iterrows():  
        if str(row["CODDEP"]) == dep:
            #not sure if i should use PTOT here
            new_list.append((row["COM"], row["PTOT"]))
    sorted_list = sorted(new_list, key=lambda x: x[1])  # x[1] refers to the population
    return sorted_list[:10]

  
print(populationByCom(df, 1))

#EXERCISE 4 ------------------------------------
