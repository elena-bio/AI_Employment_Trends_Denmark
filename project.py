import pandas as pd

# Cleaining dataset
df_ai = pd. read_csv("ai_usage.csv",header= None)
df_ict = pd.read_csv("ict_skills.csv", header= None)

#Dara inspection
# Step 1
print(df_ai.shape)
print(df_ict.shape)

# Step 2: preview data
print(df_ai.head(3))
print(df_ict.head(3))

#Step 3:Info()
df_ai.info()
df_ict.info()

# Handlle missig value
# Step 1
print(df_ai.isna().sum())
print(df_ict.isnull().sum())

# Step 2: Investigate missing value
print(df_ai[df_ai.isna().any(axis=1)])
print(df_ict[df_ict.isna().any(axis=1)])

#Step 3: find special value 
print(df_ict.nunique())
print(df_ai.nunique())

# Step 4: finding Duplicates 
print(df_ai.duplicated().sum())
print(df_ict.duplicated().sum())

# Step 4-1 finding which row has duplicate 
print(df_ict[df_ict.duplicated()])
print(df_ai[df_ai.duplicated()])

# Step 5:checking what kind of data do we have 
print(df_ai.dtypes)
print(df_ict.dtypes)

#Step 6:Replace special missing value 
df_ict = df_ict.replace("..", pd.NA)
df_ai = df_ai.replace("..", pd.NA)
print(df_ai.isna().sum())
print(df_ai.head())

# check the column structure 
print(df_ai.head(10))
print(df_ict.head(10))

#Remove Notes / Metadata Rows
print(df_ict.tail(20))
print(df_ai.tail(20))
print(df_ai.iloc[35:42])
print(df_ict.iloc[35:42])
df_ai = df_ai.iloc[:39]
df_ict = df_ict.iloc[:121]
print(df_ai.tail())
print(df_ict.tail())

# Convert Numeric columns
print(df_ict.columns)
print(df_ai.columns)
print(df_ai.iloc[0])
print(df_ict.iloc[0])

# convert numeric columns 
for col in df_ai.columns[3:]:
    df_ai[col] = pd.to_numeric(df_ai[col], errors="coerce")

for col in df_ict.columns[3:]:
    df_ict[col] = pd.to_numeric(df_ict[col], errors="coerce")

print(df_ai.dtypes)
print(df_ict.dtypes)

# saving the clean data set 
df_ai.to_csv("ai_usage_cleaned.csv", index=False)
df_ict.to_csv("ict_skills_cleaned.csv", index=False)

# Analysis Part 
# Explore the data
print(df_ict.describe())
print(df_ai.describe())

print(df_ict.iloc[1])
print(df_ai.iloc[1])

df_ai.columns = [0, 1, "Industry", 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]

df_ict.columns = [0, 1, "Industry", 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
print(df_ai.columns)
print(df_ict.columns)
df_ai.to_csv("ai_usage_cleaned.csv", index=False)
df_ict.to_csv("ict_skills_cleaned.csv", index=False)
print(df_ict.describe())
print(df_ai.describe())
print(df_ai.columns)
print(df_ai.isna().sum())
print(df_ai[[2017, 2018, 2019, 2020, 2022]].head())
print(df_ai[[2021, 2023, 2024, 2025]].mean())

# visulize and see the answer of this question 
#  the first question :How has AI adoption changed over time?
import matplotlib.pyplot as plt
df_ai[[2021, 2023, 2024, 2025]].mean().plot()
plt.title("AI adoption Trend")
plt.savefig("AI adoption Trend")
plt.show()

# How have ICT skills changed over time in Denmark?
df_ict[[2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]].mean().plot()
plt.title("CTI skills Trend")
plt.savefig("CTI skills Trend")
plt.show()

# the third question :the second question :Which industries show the highest levels of AI adoption and ICT skills?
print(df_ai.groupby("Industry").mean(numeric_only=True))
industry_ai = df_ai.groupby("Industry").mean(numeric_only=True)

print(industry_ai.mean(axis=1).sort_values(ascending=False))

industry_ict = df_ict.groupby("Industry").mean(numeric_only=True)

print(industry_ict.mean(axis=1).sort_values(ascending=False))

##the fourth question :What do these trends suggest about the future workforce in Denmark?
## answer :The results suggest that AI and digital skills will become increasingly important in Denmark's future workforce. Industries related to information and communication are likely to experience the highest demand for these skills.
df_ai.to_csv("cleaned_ai_final.csv", index=False)

df_ict.to_csv("cleaned_ict_final.csv", index=False)