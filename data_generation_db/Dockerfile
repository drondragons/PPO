# Use the official PostgreSQL 13.4 image as the base
FROM postgres:13.4

# Set environment variables for the database name, username, and password
ENV POSTGRES_DB=city_library
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=Gou_15189

# Copy the SQL script to initialize the database
COPY init_db /docker-entrypoint-initdb.d/
COPY /sql_scripts/*.sql /docker-entrypoint-initdb.d/sql_scripts/
COPY /TableData /docker-entrypoint-initdb.d/TableData/
# COPY /sql_scripts/create_db.sql /sql_scripts/init_db /sql_scripts/drop_db.sql /sql_scripts/create_dt.sql /sql_scripts/create_constraints.sql /sql_scripts/create_functions.sql /sql_scripts/insert_data.sql /docker-entrypoint-initdb.d/
# COPY /TableData/Roles.csv /TableData/Authors.csv /docker-entrypoint-initdb.d/

#CMD ./docker-entrypoint-initdb.d/init_db

# Expose the PostgreSQL default port (5432)

RUN localedef -i ru_RU -f UTF-8 ru_RU.UTF-8

EXPOSE 5433

# docker build -t city_library_image .
# docker run -d --name city_library_container -p 5433:5433 city_library_image
# docker start city_library_container
# docker exec -it city_library_container bash
# docker stop city_library_container
# docker rm city_library_container
# docker rmi city_library_image