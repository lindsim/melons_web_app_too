import sqlite3

class Melon(object):
    """A wrapper object that corresponds to rows in the melons table."""
    def __init__(self, id, melon_type, common_name, price, imgurl, flesh_color, rind_color, seedless):
        self.id = id
        self.melon_type = melon_type
        self.common_name = common_name
        self.price = price
        self.imgurl = imgurl
        self.flesh_color = flesh_color
        self.rind_color = rind_color
        self.seedless = bool(seedless)

    def price_str(self):
        return "$%.2f"%self.price

    def __repr__(self):
        return "<Melon: %s, %s, %s>"%(self.id, self.common_name, self.price_str())

class Customer(object):
    """a wrapper object that corresponds to rows in the Customer table."""
    def __init__(self, email, name, password):    
      self.email = email
      self.name = name
      self.password = password


def connect():
    conn = sqlite3.connect("melons.db")
    cursor = conn.cursor()
    return cursor

def get_melons():
    """Query the database for the first 30 melons, wrap each row in a Melon object"""
    cursor = connect()
    query = """SELECT id, melon_type, common_name,
                      price, imgurl,
                      flesh_color, rind_color, seedless
               FROM melons
               WHERE imgurl <> ''
               LIMIT 30;"""

    cursor.execute(query)
    melon_rows = cursor.fetchall()

    melons = []

    for row in melon_rows:
        melon = Melon(row[0], row[1], row[2], row[3], row[4], row[5],
                      row[6], row[7])

        melons.append(melon)

    print melons

    return melons

def get_melon_by_id(id):
    """Query for a specific melon in the database by the primary key"""
    cursor = connect()
    query = """SELECT id, melon_type, common_name,
                      price, imgurl,
                      flesh_color, rind_color, seedless
               FROM melons
               WHERE id = ?;"""

    cursor.execute(query, (id,))

    row = cursor.fetchone()
    
    

    melon = Melon(row[0], row[1], row[2], row[3], row[4], row[5],
                  row[6], row[7])
    
    return melon

def get_customer_by_email(email, password):
    cursor = connect()
    query = """SELECT email, givenname, password
               FROM  customers
               WHERE email =? AND password =?;"""

    cursor.execute(query, (email, password))

    row = cursor.fetchone()

    if not row:
      # query = """INSERT INTO customers 
      #             (email, password)
      #             VALUES (?, ?);"""
      
      cursor.execute(query, (email, password))
      customer_info = """You are a new customer! 
      We need more information about you. 
      We haven't made a new form for you yet. 
      One day. Enjoy these gifs. Melons be with you.
      """
    
    else:
      customer_info = "YOU HAVE LOGGED IN" 
      Customer(row[0], row[1], row[2])
    
    return customer_info
