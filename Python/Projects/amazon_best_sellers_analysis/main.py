import pandas as pd

df = pd.read_csv('bestsellers.csv')

print(df.head())

print(df.shape)

print(df.columns)

print(df.describe())

#Remove duplicate rows
df.drop_duplicates(inplace=True)

#Rename columns to be more descriptive and easier to work with
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

#Covert Price column to float data type
df["Price"] = df["Price"].astype(float)

#Author Popularity
author_counts = df['Author'].value_counts()
print(author_counts)

#Rating by Genre
avg_rating_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_genre)

#Export top selling authors to csv file
author_counts.head(10).to_csv("top_authors.csv")

#Export avg rating genre to csv file
avg_rating_genre.to_csv("avg_rating_genre.csv")