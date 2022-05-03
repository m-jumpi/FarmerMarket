import models.model


# def select_main_page():
#     con = models.model.sql_connection()
#     cursor = con.cursor()
#     query = ("SELECT MarketName, State, City, Street, zip FROM FarmerMarkets")
#     cursor.execute(query)
#     result = cursor.fetchall()
#     for (MarketName, State, City, Street, zip) in result:
#         print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(MarketName, State, City, Street, zip))
#     cursor.close()
#     con.close()

# def select_main_page():
#     con = models.model.sql_connection()
#     cursor = con.cursor()
#     query = ("SELECT MarketName, State, City, Street, zip FROM FarmerMarkets")
#     cursor.execute(query)
#     result = cursor.fetchall()
#     str="<table><tr><th>Market Name</th><th>State</th><th>City</th><th>Street</th><th>Zip</th></tr>"
#     for (MarketName, State, City, Street, zip) in result:
#         str+="<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(MarketName, State, City, Street, zip)
#     cursor.close()
#     str+='</table>'
#     con.close()
#     return str

# def select_main_page():
#     con = models.model.sql_connection()
#     cursor = con.cursor()
#     query = ("SELECT MarketName, State, City, Street, zip FROM FarmerMarkets")
#     cursor.execute(query)
#     result = cursor.fetchall()
#     cursor.close()
#     con.close()
#     return result


def select_by_city(city_name):
    con = models.model.sql_connection()
    cursor = con.cursor()
    query = ("SELECT MarketName, State, City, Street, zip FROM FarmerMarkets WHERE City = %s")
    cursor.execute(query, (city_name,))
    result = cursor.fetchall()
    for (MarketName, State, City, Street, zip) in result:
        print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(MarketName, State, City, Street, zip))
    cursor.close()
    con.close()
