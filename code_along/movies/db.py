from pymysql import connect, cursors

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "movies"
}

con = connect(**db_config)


def get_movies():
    pass


def get_actors():
    pass


def find_movie():
    pass
