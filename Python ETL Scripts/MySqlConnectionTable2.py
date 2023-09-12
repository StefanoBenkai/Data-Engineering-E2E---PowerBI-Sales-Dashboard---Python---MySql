import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='sql7.freesqldatabase.com',
                             user='sql7563799',
                             password='**********',
                             database='sql7563799',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `test` (`userid`, `username`,`privilegeid`) VALUES (%s, %s, %s)"
        cursor.execute(sql, ('1', 'benkaim', '1'))
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `username`, `privilegeid` FROM `test` WHERE `username`=%s"
        cursor.execute(sql, ('benkaim',))
        result = cursor.fetchone()
        print(result)