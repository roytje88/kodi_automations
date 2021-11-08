# kodi_automations
all automations for Kodi

## Autodelete
Set of scripts to autodelete episodes of a tvshow when the episode is watched. 
The script has to be manually started. You can add it to a cronjob.

When the script is started for the first time, it searches for the right database in the MySQL server on localhost (so an SQL database is required; see the kodi-wiki to set this up).
After that, an SQLite database is created with all TV shows. 

Every TV show in this .db is set to default autodelete = 0. 
When a TV show must be autodeleted, the autodelete parameter should be set to 1. 
You can do this with the following commands:
<pre>
# First load the database
$ sqlite3 settings.db

# query all TV shows
sqlite3> select * from allshows; 

# query all TV shows which will be set to autodelete
sqlite3> select * from allshows where autodelete = 1;

# set autodelete for a TV show
sqlite3> update allshows set autodelete = 1 where showname = [Name of TV Show];
# alternatively use the Show ID in the first column of the table
sqlite3> update allshows set autodelete = 1 where id = [ID of TV Show];


# unset autodelete for a TV show
sqlite3> update allshows set autodelete = 0 where showname = [Name of TV Show];
# alternatively use the Show ID in the first column of the table
sqlite3> update allshows set autodelete = 0 where id = [ID of TV Show];

</pre>
