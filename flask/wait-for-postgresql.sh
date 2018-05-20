#!/bin/sh sh
set -e

POSTGRES_DB=${POSTGRES_DB:-"database_name"}
POSTGRES_USER=${POSTGRES_USER:-"db_password"}
POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-"db_name"}

echo ""
echo "connecting to database: ${POSTGRES_USER}:${POSTGRES_PASSWORD}@tsn-db:5432/${POSTGRES_DB}"
until psql -q postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@ta-db:5432/${POSTGRES_DB} -c '\l'; do
  echo "waiting for database setup ..."
  sleep 1
done
echo "database is ready."
echo ""

exec $@