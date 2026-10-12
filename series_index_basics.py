import pandas as pd

age_nam = pd.Series(
    [90, 75, 88],
    index=["Ali", "Mona", "Hany"]
)

print(age_nam)
print(age_nam.index)
print(age_nam.values)
print(age_nam.dtype)
