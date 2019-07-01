FROM mdillon/postgis
# We copy the SQL dump into this directory so that the schema and data automatically migrates into the container.
COPY data/postgis_init.sql /docker-entrypoint-initdb.d/
