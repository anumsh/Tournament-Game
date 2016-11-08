rdb-fullstack
=============

#Tournament

This project uses the PostgreSQL database to keep track of players and matches in a game tournament.It will define the database Schema (SQL table definitions) in tournament.sql file and writing code that will use it to track a Swiss tournament in tournament.py file.

#Installtion

https://github.com/udacity/fullstack-nanodegree-vm

#Examples

Commmand Line

:~/Desktop/fullstack/vagrant/tournament$ vagrant up

:~/Desktop/fullstack/vagrant/tournament$ vagrant ssh

vagrant@vagrant-ubuntu-trusty-32:cd /vagrant/tournament

vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ ls
tournament.py   tournament.sql      tournament_test.pyc
tournament.pyc  tournament_test.py

vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ psql;
psql (9.3.12)
Type "help" for help.

# DB-Schema

create database databasename;

create table tablename (
column1 datatype1,
columnname2 datatype2);

create view as
   select column1,column2 from tablename;

#DB-API

conn = connect()
c = conn.cursor()
c.execute("your query;")
conn.commit()
conn.close()

#Resouces

https://discussions.udacity.com/c/nd000-stage-5-choose-your-path/back-end-developer

http://www.postgresql.org/docs/8.1/static/sql-fetch.html

http://www.postgresql.org/docs/8.3/static/tutorial-join.html

#License

This content of repository is licenced under  © 2011–2016 Udacity, Inc.