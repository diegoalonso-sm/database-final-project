### Topics

| Column        | Type          | Description                          |
| ------------- | ------------- | ------------------------------------ |
| title         | string        | The name of topics listed on GitHub. |
| description   | string        | A short description of the topic.    |

### Users

| Column          | Type          | Description                                               |
| --------------- | ------------- | --------------------------------------------------------- |
| owner           | string        | The User owner of the repository.                         |
| owner_type      | string        | The type of owner. For example, "User" or "Organization". | 

### Repositories

| Column          | Type          | Description                                                                                                     |
| --------------- | ------------- | --------------------------------------------------------------------------------------------------------------- |
| name            | string        | The name of the repository.                                                                                     |
| topic           | string        | The name of topics listed on GitHub.                                                                            |
| owner           | string        | The User owner of the repository.                                                                               |
| description     |	string        | The description of the repository.                                                                              |
| license         |	string        | The license associated with the repository. For example, "mit" or "mpl-2.0".                                    |                   
| is_archived	    | boolean	      | Indicates if the repository is unmaintained.                                                                    |
| is_forked       |	boolean	      | Identifies if the repository is a fork.                                                                         |
| size	          | integer       |	The file size of repository in bytes.                                                                           |
| language	      | string        | The programming language this reposity is written in.                                                           |
| open_issues     |	integer       | The number of open issues in the repository.                                                                    |
| forks           |	integer       |	How many forks there are of this repository in the whole network.                                               |
| stars           |	integer       |	How many stars there are of this repository.                                                                    |
| watchers        |	integer       |	The number of users watching the repository.                                                                    |
| has_wiki        |	boolean       |	Either true to enable the wiki for this repository or false to disable it.                                      |
| has_pages       |	boolean       |	Either true to enable the pages for this repository or false to disable it.                                     |
| has_sponsorship |	boolean       |	Either true to enable the sponsor button for this repository or false to disable it.                            |
| created_at	    | string        |	Identifies the date and time when the object was created in ISO format. For example, 2022-03-14T10:39:35Z.      |
| updated_at	    | string        |	Identifies the date and time when the object was last updated in ISO format. For example, 2022-03-14T10:39:35Z. |

### Cambios para normalizar

- Se elimina la columna logo_image de Topics.
- Se elimina la columna tags de Repositories.
- Se elimina la columna full-name de Repositories.
- Se elimina la columna og-image de Repositories.
