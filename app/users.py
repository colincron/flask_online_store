from app.db import get_db

def get_all_users():
    cursor = get_db().execute("select * from user;", ())
    results = cursor.fetchall()
    cursor.close()
    return results

def create_user(first_name,last_name,hobbies):
    db=get_db()
    db.execute("insert into user values (?, ?, ?)", (first_name, last_name, hobbies))
    db.commit()
    db.close()
    return "Item submitted!"

def update_user(toset, string1, whereset, string2  ):
    cursor = get_db().execute('update user set ' + toset + '=' + string1 + ' where ' + whereset + '=' + string2 + ';')
    cursor.close()
