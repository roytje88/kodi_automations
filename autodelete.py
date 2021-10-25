#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sqlalchemy import create_engine
import pymysql
import pandas as pd
import sqlite3, os
from sqlite3 import Error


# In[ ]:


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute('pragma foreign_keys = ON;')
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def createDB():
    conn = create_connection('settings.db')
    allShows = """CREATE TABLE IF NOT EXISTS allShows (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    showname text not null,
                    autodelete integer not null
    );"""
    
    
    
    create_table(conn, allShows)
    
def readTable(table,inclusieflogischverwijderd=True):
    import pandas as pd
    con = sqlite3.connect("settings.db")
    return pd.read_sql_query("SELECT * from "+table, con)


# In[ ]:


def reload():
    database = 'settings.db'
    try:
        os.remove(database)
    except:
        pass
    createDB()


# In[ ]:


reload()


# In[ ]:


def mySQL():
    sqlEngine       = create_engine('mysql+pymysql://kodi:kodi@127.0.0.1', pool_recycle=3600)
    return sqlEngine.connect()


# In[ ]:


for i in pd.read_sql("show databases", mySQL()).values.tolist():
    if i[0][0:8] == 'MyVideos':
        db = i[0]
        


# In[ ]:


def addNewShow(tvshow):
    if tvshow not in readTable('allShows')['showname'].values.tolist() and tvshow != None:
        sqlNewShow = """insert into allShows (showname,autodelete) values ('""" + tvshow + """','0');"""
        try:
            database = 'settings.db'
            conn = create_connection(database)
            c = conn.cursor()
            c.execute(sqlNewShow)
            conn.commit()
        except Error as e:
            print(e)


# In[ ]:


if 1==1:
    addNewShow('Walker')
    conn.commit()


# In[ ]:


if readTable('allShows').values.tolist() == []:
    database = 'settings.db'
    conn = create_connection(database)
    c = conn.cursor()
    sql = 'select c00 from '+db+'.tvshow'
    for i in pd.read_sql(sql, mySQL()).values.tolist():
        if i[0] != None:
            sqlNewShow = """insert into allShows (showname,autodelete) values ('""" + i[0].replace("'","''") + """','0');"""
            c = conn.cursor()
            c.execute(sqlNewShow)
    conn.commit()
            


# In[ ]:


sql = """select a.idFile , a.c12 AS "Season" , a.c13 AS "Episode" ,a.c00 AS "Episode Name" , b.c00 AS "Show Name" , a.c18 AS "File name", c.playCount, c.lastPlayed from """+db+""".episode a , """+db+""".tvshow b, """+db+""".files c WHERE a.idShow = b.idShow and a.idFile=c.idFile """+"""and c.playCount > 0 and c.lastPlayed is not null"""


# In[ ]:


playedEpisodes = pd.read_sql(sql, mySQL())


# In[ ]:


settings = readTable('allShows')


# In[ ]:


toDelete = settings[settings['autodelete']==1]


# In[ ]:


epsToDelete = playedEpisodes.merge(toDelete, left_on='Show Name', right_on='showname')


# In[ ]:


import os
for i in epsToDelete[['File name']].values.tolist():
    if os.path.exists(i[0][22:]):
        try:
            os.remove(i[0][22:])
            print('Deleted ' + i[0][22:])
        except:
            print('Error deleting ' + i[0][22:])

