# Assignment1

## First Step

- Create a PostgreSQL database with the name of your election.

 - In the Assignment1 folder run :
  
    ```pip install -r requirements.txt```

- Create an ".env" file in the bookstore folder, so that have a path like this:
  
  ```Assignment1\bookstore\.env```
- The ".env" format is the following:

  ```
  DB_NAME= database name
  DB_USER= postgres user
  DB_PASSWORD= password
  DB_HOST= host
  DB_PORT= port number
  ```

  Change this with the database information
  


## How to run migrations.
- In the Assignment1 folder run :
  
  ```python bookstore/manage.py makemigrations```

- Then:

  ```python bookstore/manage.py migrate```


## How to populate the database
- In the Assignment1 folder run :
  
  ```python bookstore/populate_db_fake.py```

## How to run the project
- In the Assignment1 folder run :
  
  ```python bookstore/manage.py runserver```

