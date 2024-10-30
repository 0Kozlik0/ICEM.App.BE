# ICEM Application (Backend)

## How to access endpoints

Example:
`http://localhost:8000/ikem_api/test`

Links for endpoints documentation (server needst to be started first): `http://localhost:8000/docs/`


## How to start application?

### Local

`uvicorn src.api.main:app --reload`

***Info***: needs to be located in a main folder (cd ICEM.App.BE)

### Production

## Docker

### Local
`docker-compose -f docker/docker-compose.dev.yml up`

for rebuild

`docker-compose -f docker/docker-compose.dev.yml up --build`

### Production