
import pandas as pd

directory1 = "C:\\Users\\diego\\OneDrive\\Escritorio\\DB Project\\data\\topics.csv"
directory2 = "C:\\Users\\diego\\OneDrive\\Escritorio\\DB Project\\data\\repositories.csv"

df1 = pd.read_csv(directory1)
df2 = pd.read_csv(directory2)

# Topics (entity)
df_topics = df1[['title','description']]
df_topics.to_csv("C:\\Users\\diego\\OneDrive\\Escritorio\\DB Project\\data\\topics_normalized.csv")

# Owners (entity)
df_owners = df2[['owner', 'owner_type']]
df_owners.to_csv("C:\\Users\\diego\\OneDrive\\Escritorio\\DB Project\\data\\owners_normalized.csv")

# Repositories (entity)
df_repositories = df2[['full_name', 'description', 'size', 'is_forked', 'forks', 'stars', 'watchers', 'updated_at']]
df_repositories.to_csv("C:\\Users\\diego\\OneDrive\\Escritorio\\DB Project\\data\\repositories_normalized.csv")

# classified_by (relation)
df_classified_by = pd.concat([df1[['title']],df2[['full_name', 'description', 'size', 'is_forked', 'forks', 'stars', 'watchers', 'updated_at']]])
df_classified_by.to_csv("C:\\Users\\diego\\OneDrive\\Escritorio\\DB Project\\data\\classified_by_normalized.csv")

# created_by (relation)
df_classified_by = df2[['full_name', 'owner', 'created_at']]
df_classified_by.to_csv("C:\\Users\\diego\\OneDrive\\Escritorio\\DB Project\\data\\created_by_normalized.csv")