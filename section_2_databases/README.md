# Govtech Data Engineer Tech Challenge


## Section 2: Databases

Business requirements  
1) car & salesperson : one-to-one relationships


### Setup postgres instance with docker
1) In the terminal, change the working directory to the where the project folder is in the command line.

 ```console
 cd ~/home/govtech_de_test/section_2_databases
 ```

2) Build the docker image.
```console
docker build -t govtech-postgres .
```

3) Spinning up a docker container.
```console
docker run --name govtech-postgres -e POSTGRES_PASSWORD=Qwer!@#$ -p 5432:5432 -d govtech-postgres
```

4) Connect to psql bash in terminal and verify tables are created
 ```console
docker exec -it govtech-postgres bash
 ```

Inspect tables.
```
psql -U postgres
```
show all databases, connect to database and list all tables
```
\list
\connect carsales
\dt
```

### ER diagram


### SQL query
