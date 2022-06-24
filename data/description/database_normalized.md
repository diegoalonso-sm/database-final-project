
### Repositories

| Column        | Type       | Description                                                       |
| ------------- | ---------- | ----------------------------------------------------------------- |
| **full_name** |	**string** | **The full name of the repository. This means {owner}/{name}.**   |
| is_archived	  | boolean	   | Indicates if the repository is unmaintained.                      |
| size	        | integer    | The file size of repository in bytes.                             |
| watchers      |	integer    | The number of users watching the repository.                      |
| forks         |	integer    | How many forks there are of this repository in the whole network. |
| stars         |	integer    | How many stars there are of this repository.                      |
| open_issues   |	integer       | The number of open issues in the repository.                   |

### Owners

| Column     | Type       | Description                                               |
| ---------- | ---------- | --------------------------------------------------------- |
| **owner**  | **string** | **The user owner of the repository.**                     |
| owner_type | string     | The type of owner. For example, "User" or "Organization". | 

### Created by

| Column                     | Type       | Description                                                                 |
| -------------------------- | ---------- | --------------------------------------------------------------------------- |
| **Repositories.full_name** | **string** | **The full name of the repository. This means {owner}/{name}.**             |
| **owner**                  | **string** | **The user owner of the repository.**                                       |
| created_at	               | string        |	Identifies the date and time when the object was created in ISO format. |


### Topics

| Column                     | Type       | Description                                                     |
| -------------------------- | ---------- | --------------------------------------------------------------- |
| **Repositories.full_name** | **string** | **The full name of the repository. This means {owner}/{name}.** |
| **topic**                  | **string** | **The name of topics listed on GitHub.**                        |

### Languages

| Column                     | Type       | Description                                                     |
| -------------------------- | ---------- | --------------------------------------------------------------- |
| **Repositories.full_name** | **string** | **The full name of the repository. This means {owner}/{name}.** |
| **Language**               | **string** | **The programming language this reposity is written in.**       |
