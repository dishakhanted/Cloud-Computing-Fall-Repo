import psycopg2
from db_config import users_db_connection_string

conn = psycopg2.connect(users_db_connection_string)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        userID SERIAL NOT NULL UNIQUE,
        schoolID integer NOT NULL,
        isAdmin boolean NOT NULL,
        firstName varchar(40) NOT NULL,
        lastName varchar(40) NOT NULL,
        columbiaEmail varchar(30) NOT NULL,
        password char(60) NOT NULL,
        profilePicture BYTEA,
        major varchar(40) NOT NULL,
        jobTitle varchar(40),
        company varchar(40),
        graduationYear integer NOT NULL,
        userDescription varchar(500),
        creationDT timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
        CONSTRAINT primaryKeyUserID PRIMARY KEY (userID),
        CONSTRAINT foreignKeySchoolID FOREIGN KEY (schoolID) REFERENCES schools
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS schools (
        schoolID SERIAL NOT NULL UNIQUE,
        schoolName varchar(40) NOT NULL,
        CONSTRAINT primaryKeySchoolID PRIMARY KEY (schoolID)
    );
""")

conn.commit()
cur.close()
conn.close()