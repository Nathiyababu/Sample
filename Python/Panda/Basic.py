import pandas as pd
#Data cleaning

#print(dir(pd))

data={
    "cars":["bmw","audi","kia","tata"],
    "ranks":[5,4,2,3]
}
x=pd.DataFrame(data)
print(x)
print(pd.__version__)
