
import pandas as pd

directory1 = "C:\\Users\\diego\\OneDrive\\Escritorio\\DB Project\\data\\topics.csv"
directory2 = "C:\\Users\\diego\\OneDrive\\Escritorio\\DB Project\\data\\repositories.csv"

df1 = pd.read_csv(directory1)
df2 = pd.read_csv(directory2)

# Owners (entity)
df_owners = df2[['owner', 'owner_type']]
df_owners.to_csv("C:\\Users\\diego\\OneDrive\\Escritorio\\DB Project\\data\\normalized\\owners.csv", index=False)

# Repositories (entity)
df_repositories = df2[['full_name', 'is_archived', 'size', 'watchers', 'forks', 'stars', 'open_issues']]
df_repositories.to_csv("C:\\Users\\diego\\OneDrive\\Escritorio\\DB Project\\data\\normalized\\repositories.csv", index=False)

# Topics (entity)
df_topics = df2[['full_name', 'topic']]
df_topics.to_csv("C:\\Users\\diego\\OneDrive\\Escritorio\\DB Project\\data\\normalized\\topics.csv", index=False)

# Languages (entity)
df_topics = df2[['full_name', 'language']]
df_topics.to_csv("C:\\Users\\diego\\OneDrive\\Escritorio\\DB Project\\data\\normalized\\languages.csv", index=False)

# Created_by (relation)
df_topics = df2[['full_name', 'owner', 'created_at']]
df_topics.to_csv("C:\\Users\\diego\\OneDrive\\Escritorio\\DB Project\\data\\normalized\\created_at.csv", index=False)
