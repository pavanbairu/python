# creating the database list and the list of databases are fixed which can be changed. i case will use tuple

db_tuple = ("mongodb", "mysql", "redis", "rabbitmq")
print(db_tuple)

# accesing the tuple by index
print(db_tuple[2])

# accesing the few tuples
new_db_tuple = db_tuple[1:3]
print(new_db_tuple)

# Unpack the tuple into x and y
(x, y) = new_db_tuple
print(x)
print(y)

# concatnation
new_tuple = db_tuple + ("cassandra", "oracle")
print(new_tuple)