#!/usr/bin/env python
# tournament.py -- implementation of a Swiss-system tournament
# importing psycopg2 file
import psycopg2

# this function will connect to database - tournament
# output will be tournament database connection
def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

# this function will delete all the records of matches from tournament database
# here , we are using delete query to delete all the entries/values in matches table
# here we have call connect() function to connect with tournament database and assign it
# to con variable
def deleteMatches():
    """Remove all the match records from the database."""
    con = connect()
    c = con.cursor()
    c.execute("delete from matches")
    con.commit()
    con.close()

# this function will delete all the records of players from tournament database
# using delete query to delete all the entries/values in players table
def deletePlayers():
    """Remove all the player records from the database."""
    con = connect()
    c = con.cursor()
    c.execute("delete from players")
    con.commit()
    con.close()

# this function will counts the number of registered player in player table
# select query is used to fetch the records of player table
# for counting the records, aggregate function (COUNT) is used
# it will return (player_count) to function
def countPlayers():
    """Returns the number of players currently registered."""
    con = connect()
    c = con.cursor()
    c.execute("select count(*) from players")
    player_count=c.fetchone()[0]
    if player_count == 0:
        return player_count
    else:
        player_count = player_count
        return player_count
    con.close()

# this function will registered the player name in player table
# insert query is used to insert the player name
# input- it will take argument(name), this argument is inserted into player table
def registerPlayer(name):
    """ Records the player name into the database """
    con = connect()
    c = con.cursor()
    c.execute("insert into players (player_name) values(%s)",(name,))
    con.commit()
    con.close()

# this function will return the player_win_records.
# select qusery is used to fetch the player win records from standing view.
# return the list of player_id,player_name,wins,total_match)
def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    """
    con = connect()
    c = con.cursor()
    c.execute("select * from standings")
    player_record=c.fetchall()
    return player_record
    con.close()

#this function will insert the winner and loser name into matches table
# insert query is used to insert the winner and loser name in matches table
def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    """
    con = connect()
    c = con.cursor()
    c.execute("insert into matches (winner_id,loser_id) values(%s,%s)",(winner,loser))
    con.commit()
    con.close()

# this function will return the list of pairs of players for next round
# output will be pairs of players .
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    """
    con = connect()
    c = con.cursor()
    c.execute("select * from standings")
    player_records=c.fetchall()
    player_rank = []
    for row in player_records:
        player_rank.append(((row[0]),(row[1]),(row[2]),(row[3])))
    player_rank = playerStandings()
    count = 0
    pairings = []
    while count < len(player_rank):
        player1_id = player_rank[count][0]
        player1_name = player_rank[count][1]
        player2_id = player_rank[count+1][0]
        player2_name = player_rank[count+1][1]
        pairings.append((player1_id,player1_name, player2_id, player2_name))
        count += 2
    return pairings