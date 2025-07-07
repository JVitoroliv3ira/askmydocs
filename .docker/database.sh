#!/bin/bash

CONTAINER_NAME="askmydocs-database"
POSTGRES_USER="askmydocs"
POSTGRES_PASSWORD="12345678"
POSTGRES_DB="askmydocs"
POSTGRES_PORT=5432
POSTGRES_IMAGE="postgres:16"

CONTAINER_EXISTS=$(docker ps -a -q -f name="^${CONTAINER_NAME}$")
CONTAINER_RUNNING=$(docker ps -q -f name="^${CONTAINER_NAME}$")

if [ -n "$CONTAINER_RUNNING" ]; then
  echo "Container '$CONTAINER_NAME' já está rodando. Nada a fazer."
  exit 0
fi

if [ -n "$CONTAINER_EXISTS" ]; then
  echo "Container '$CONTAINER_NAME' existe mas está parado. Iniciando..."
  docker start $CONTAINER_NAME > /dev/null
else
  echo "Criando novo container PostgreSQL '$CONTAINER_NAME'..."
  docker run -d \
    --name $CONTAINER_NAME \
    -e POSTGRES_USER=$POSTGRES_USER \
    -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
    -e POSTGRES_DB=$POSTGRES_DB \
    -p $POSTGRES_PORT:5432 \
    $POSTGRES_IMAGE
fi

echo "Aguardando PostgreSQL iniciar..."
until docker exec $CONTAINER_NAME pg_isready -U $POSTGRES_USER > /dev/null 2>&1; do
  sleep 1
done

echo "Instalando extensão pgvector..."
docker exec -u root $CONTAINER_NAME bash -c "apt-get update && apt-get install -y postgresql-server-dev-16 build-essential git"
docker exec $CONTAINER_NAME bash -c "cd /tmp && git clone --branch v0.5.1 https://github.com/pgvector/pgvector.git && cd pgvector && make && make install"

echo "Criando extensão no banco askmydocs..."
docker exec $CONTAINER_NAME psql -U $POSTGRES_USER -d $POSTGRES_DB -c "CREATE EXTENSION IF NOT EXISTS vector;"

echo "PostgreSQL rodando e pronto para uso com pgvector."
echo "Acesso: user=$POSTGRES_USER | password=$POSTGRES_PASSWORD | db=$POSTGRES_DB"
echo "Porta local: $POSTGRES_PORT"
