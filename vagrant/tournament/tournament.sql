-- Table definitions for the tournament project.

-- it will drop the database if it already exists
DROP DATABASE IF EXISTS tournament ;

-- creating new database with name-tournament
CREATE DATABASE tournament;

-- it will switch to tournament database from other database(vagrant)
\c tournament;

-- creating table players
-- players table have two columns (player_id) and (player_name)
-- datatype for player_id is SERIAL(auto increment)and player_name is text(add unlimited text)
CREATE TABLE players (
player_id SERIAL PRIMARY KEY,
player_name TEXT);

--creating  table matches
-- matches column have three columns (match_id,winner_id,loser_id)
-- datatypes for match_id is SERIAL and for (winner_id and loser_id) is INTEGER(numeric values)
-- winner_id and loser_id is a foriegn key of matches table as both tables are reference to
--(player_id) of players table
CREATE TABLE matches (
match_id SERIAL PRIMARY KEY,
winner_id INTEGER REFERENCES players(player_id),
loser_id INTEGER REFERENCES players(player_id));

-- creating a view (player_wins) which will record the total number of matches the player win
-- along with player_id and player_name
CREATE VIEW player_wins AS
    SELECT player_id, player_name, COUNT(winner_id) AS wins
      FROM players
 LEFT JOIN matches ON player_id = winner_id
  GROUP BY player_id;


--creating a view (player_losses) which will record the total number of matches the player lose
--along with player_id and player_name
CREATE VIEW player_losses AS
    SELECT player_id, player_name, COUNT(loser_id) AS loss
      FROM players
 LEFT JOIN matches ON player_id = loser_id
  GROUP BY player_id;

--creating view (standings) which will record the playerid,playername,
--number of matches win by player and total number of matches played by one player
-- there is four columns- player_is,player_name,wins,match
-- table is order(desending) by wins column(number of matches win by player)
CREATE VIEW standings AS
    SELECT player_wins.player_id, player_wins.player_name, player_wins.wins,
    (player_wins.wins + player_losses.loss) AS total_match
      FROM player_wins
      JOIN player_losses ON player_wins.player_id = player_losses.player_id
      ORDER BY wins DESC;



