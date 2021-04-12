# apartments-app

Project for OICAR college course. Project consists off frontend, backend and mobile applications. For more information about each project and project dependencies, check each of the project's README pages.

## Run application locally

```bash
docker compose up
```

pgAdmin4 will be accessible on localhost on port 5050 (<http://localhost:5050>)  
Backend (RESTful API) will be accessible on localhost on port 8080 (<http://localhost:8080>)  

## Troubleshooting

### Docker

First stop containers and then remove all containers, volumes and PostgreSQL data

```docker
docker stop $(docker ps -a -q) && docker rm -v $(docker ps -a -q) && docker volume rm apartments-app_postgres_data
```

Remove all containers, volumes and PostgreSQL data

```docker
docker rm -v $(docker ps -a -q) && docker volume rm apartments-app_postgres_data
```

### [pgAdmin 4](http://localhost:5050)

Login credentials

- pgadmin email: admin@admin.com
- pgadmin password: admin

Access database from pgAdmin4

- host: host.docker.internal
- database: apartments_db
- username: ${POSTGRES_USER}
- password: ${POSTGRES_PASSWORD}
