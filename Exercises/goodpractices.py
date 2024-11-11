#Data Types and Variables 

#Track expenses for a budget calculation
monthly_income = 3000
rent = 1000
groceries = 300
utilities = 200

total_expenses = rent + groceries + utilities
savings = monthly_income - total_expenses
print(savings)

#Budget vs total
grocery_list = {"milk": 2.5, "bread": 1.5, "eggs": 3, "fruit": 5}
budget = 10
total = 0
for item, price in grocery_list.items():
    if total + price <= budget:
        total += price
        print(f"{item} added. Total: ${total}")
    else:
        print(f"{item} skipped. Budget exceeded.")
        
#Calculating average
def average_speed(distance, time):
    return distance / time
 
print("Average Speed:",average_speed(150, 2),"km/h")

students = {"Alice": 85, "Bob": 92, "Charlie": 78}
avg_score = sum(students.values()) / len(students)
print("Average Score:", avg_score)

#Reading a file 
with open("data.txt","r") as file:
    for line in file:
        print(line.strip())
        
#Importing libraries, Time left until:
from datetime import datetime
event_date = datetime(2024,12,31)
days_left = (event_date - datetime.now()).days
print("Days until event:", days_left)

#Pandas
import pandas as pd
 
data = {"Day": ["Mon", "Tue", "Wed", "Thu", "Fri"], "Steps": [5000, 8000, 6000, 7500, 9000]}
df = pd.DataFrame(data)
print("Average steps:", df["Steps"].mean())


#*args **kwargs
def space_adventure(*args, **kwargs):
    spaceship = kwargs.get("spaceship", "SS Galactic")
    crew = kwargs.get("crew", ["Captain Stellar", "Lieutenant Starshine", "Robo-K9"])
    mission = kwargs.get("mission", "collect alien coffee beans")
    
    # Constructing the story
    locations = ', '.join(args) if args else "the unknown regions of space"
    crew_members = ', '.join(crew)
    story = (f"Onboard the {spaceship}, the fearless crew ({crew_members}) embarked on a daring mission "
             f"to {mission} in {locations}. Along the way, they encountered a space squid, "
             "a disco-dancing asteroid belt, and a mysterious alien DJ playing retro Earth tunes!")
    
    return story
 
# Sample calls
#print(space_adventure("Mars", "Jupiter", mission="find the galaxy's largest slice of space pizza"))
print(space_adventure("Alpha Centauri", spaceship="The Cosmic Cookie", crew=["Astro Alex", "Nebula Nate"]))
#print(space_adventure())  # Using all default values
