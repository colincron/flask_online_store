from app.db import get_db

def get_all_products():
    cursor = get_db().execute("select * from products;", ())
    results = cursor.fetchall()
    cursor.close()
    return results

def create_product(name, category, price, stock, img):
    db = get_db()
    db.execute("insert into products values('%s','%s','%s','%s','%s')" % (name, category, price, stock, img))
    db.commit()
    db.close()
    return "Item Submitted"

def modify_product(old_name, select, change_to):
    cursor = get_db()
    cursor.execute("update products set '%s'='%s' where prod_name='%s'" % (select, change_to, old_name))
    cursor.commit()
    cursor.close()
    return "Item modified! (Unless this still doesn't work..."

def remove_product(name):
    cursor = get_db()
    cursor.execute("delete from products where prod_name='%s';") % (name)
    cursor.commit()
    cursor.close()
    return "Item deleted! (Unless this still doesn't work...)"
