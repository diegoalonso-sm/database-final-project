### Topics

| Column      | Type       | Description                              |
| ----------- | ---------- | ---------------------------------------- |
| **name**    | **string** | **The name of topics listed on GitHub.** |
| description | string     | A short description of the topic.        |

### Owners

| Column     | Type       | Description                                               |
| ---------- | ---------- | --------------------------------------------------------- |
| **name**   | **string** | **The user owner of the repository.**                     |
| owner_type | string     | The type of owner. For example, "User" or "Organization". | 

### Repositories

| Column      | Type       | Description                                                                                              |
| ----------- | ---------- | -------------------------------------------------------------------------------------------------------- |
| **name**    |	**string** | **The full name of the repository. This means {owner}/{name}.**                                          |
| description |	string     | The description of the repository.                                                                       |
| size	      | integer    | The file size of repository in bytes.                                                                    |
| is_forked   |	boolean	   | Identifies if the repository is a fork.                                                                  |
| forks       |	integer    | How many forks there are of this repository in the whole network.                                        |
| stars       |	integer    | How many stars there are of this repository.                                                             |
| watchers    |	integer    | The number of users watching the repository.                                                             |
| last_update | string     | Identifies the date and time when the object was last updated in ISO format (I.E. 2022-03-14T10:39:35Z). |

### classified_by

| Column                | Type       | Description                              |
| --------------------- | ---------- | ---------------------------------------- |
| **Repositories.name** | **string** | **The name of the repository.**          |
| **Topics.name**       | **string** | **The name of topics listed on GitHub.** |

### created_by

| Column                | Type       | Description                                                     |
| --------------------- | ---------- | --------------------------------------------------------------- |
| **Repositories.name** |	**string** | **The full name of the repository. This means {owner}/{name}.** |
| **Owner.name**        | **string** | **The name of topics listed on GitHub.**                        |
