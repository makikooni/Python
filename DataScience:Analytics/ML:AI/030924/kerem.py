from logics import *
 
rain = Symbol("rain") # if is raining
newcastle = Symbol("Newcastle") # kerem visiting Newcastle
london = Symbol("London") # kerem visited London
 
knowledge = And(
    Implication(Not(rain), newcastle),
    Or(newcastle, london),
    Not(And(newcastle, london)),
    london
)
 
print(model_check(knowledge, rain))
print(knowledge.formula())
 
 