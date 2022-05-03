import mysql.connector


def sql_connection():
    try:
        con = mysql.connector.connect(user='root', password='12345As!', host='localhost', database='FarmerMarkets')
    except Exception as ex:
        print(ex)
    else:
        return con


# def select_main_page():
#     con = sql_connection()
#     cursor = con.cursor()
#     query = ("SELECT FMID, MarketName, State, City, Street, zip, x, y FROM FarmerMarkets")
#     cursor.execute(query)
#     result = cursor.fetchall()
#     cursor.close()
#     con.close()
#     return result


def select_details_page(id):
    con = sql_connection()
    cursor = con.cursor()
    query = ("SELECT * FROM FarmerMarkets WHERE FMID = %s")
    cursor.execute(query, (id,))
    result = cursor.fetchall()
    cursor.close()
    con.close()
    return result


def insert_review(ReviewText, Rating, MarketID, UserEmail):
    con = sql_connection()
    cursor = con.cursor()
    query = ("INSERT INTO Reviews (ReviewText, Rating, MarketID, UserEmail) VALUES (%s, %s, %s, %s)")
    cursor.execute(query, (ReviewText, Rating, MarketID, UserEmail))
    con.commit()
    cursor.close()
    con.close()


# def select_reviews_page(id):
#     con = sql_connection()
#     cursor = con.cursor()
#     query = ("SELECT ReviewText, Rating, MarketID FROM Reviews WHERE MarketID = %s")
#     cursor.execute(query, (id,))
#     result = cursor.fetchall()
#     cursor.close()
#     con.close()
#     return result

def select_reviews_page(id):
    con = sql_connection()
    cursor = con.cursor()
    query = ("SELECT ReviewText, Rating, MarketID, UserName  FROM Reviews INNER JOIN Users On Reviews.UserEmail = Users.EmailID WHERE MarketID = %s")
    cursor.execute(query, (id,))
    result = cursor.fetchall()
    cursor.close()
    con.close()
    return result


def select_city():
    con = sql_connection()
    cursor = con.cursor()
    query = ("SELECT DISTINCT city FROM FarmerMarkets ORDER BY city")
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    con.close()
    return result


def select_by_city(city):
    con = sql_connection()
    cursor = con.cursor()
    query = ("SELECT FMID, MarketName, State, City, Street, zip FROM FarmerMarkets WHERE City = %s")
    cursor.execute(query, (city,))
    result = cursor.fetchall()
    cursor.close()
    con.close()
    return result


def select_state():
    con = sql_connection()
    cursor = con.cursor()
    query = ("SELECT DISTINCT state FROM FarmerMarkets ORDER BY State")
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    con.close()
    return result


def select_by_state(state):
    con = sql_connection()
    cursor = con.cursor()
    query = ("SELECT FMID, MarketName, State, City, Street, zip FROM FarmerMarkets WHERE State = %s")
    cursor.execute(query, (state,))
    result = cursor.fetchall()
    cursor.close()
    con.close()
    return result


def select_by_name(name='%'):
    con = sql_connection()
    cursor = con.cursor()
    query = (
        f"SELECT FMID, MarketName, State, City, Street, zip, x, y FROM FarmerMarkets WHERE MarketName LIKE '{name}%'")
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    con.close()
    return result

def inserst_user(email, username, password):
    con = sql_connection()
    cursor = con.cursor()
    query = ("INSERT INTO Users (EmailID, UserName, Password) VALUES (%s, %s, %s)")
    cursor.execute(query, (email, username, password))
    con.commit()
    cursor.close()
    con.close()

def select_user(email):
    con = sql_connection()
    cursor = con.cursor()
    query = ("SELECT EmailID, UserName, Password FROM Users WHERE EmailID = %s")
    cursor.execute(query, (email,))
    result = cursor.fetchall()
    cursor.close()
    con.close()
    return result