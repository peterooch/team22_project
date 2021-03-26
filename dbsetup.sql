--https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
CREATE DATABASE student_board;

CREATE USER student_board_user with PASSWORD 'student_board';

ALTER ROLE student_board_user SET client_encoding TO 'utf8';
ALTER ROLE student_board_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE student_board_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE student_board TO student_board_user;
