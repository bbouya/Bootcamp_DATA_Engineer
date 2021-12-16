    """[Notion of du modul]
     The pupose of the module is at first to create, administrate
     and normalize a Postgresql database. then we are going to analyse
     the data and visualize the content of the database
     Finally we will see advanced notions like caching
     
    """
    

# Exercice 0 - Setup : 
# The client -Server Archetecture
PostgreSql is an open source database which follows a client-server archetecture. it is devided in three different components:
 - client, a program on the user machine which communicates the users query to the server and receives the servers answers.
 - a server, a program running in the background that manages access to a specefic resource, service or network. The server will understand the client query and apply it to the database, then it will send an answer to the client.
 - a databaes system, where the data is stored.

 


