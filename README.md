# ICEM Application (Backend)

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