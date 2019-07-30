import sqlite3

def connect():
	conn = sqlite3.connect("profile.db")
	cur = conn.cursor()
	cur.execute(" CREATE TABLE IF NOT EXISTS profile (id INTEGER PRIMARY KEY , name text , dob text ,phone INTEGER, bloodgroup text)")
	conn.commit()
	conn.close()


def insert(name,dob,phone,bloodgroup):
	conn = sqlite3.connect("profile.db")
	cur = conn.cursor()
	cur.execute(" INSERT INTO profile VALUES (NULL,?,?,?,?) ",( name,dob,phone,bloodgroup ) )
	conn.commit()
	conn.close()

def view():
	conn = sqlite3.connect("profile.db")
	cur = conn.cursor()
	cur.execute(" SELECT * FROM profile " )
	rows = cur.fetchall()
	conn.close()
	return rows


def search(name='',dob='',phone='',bloodgroup=''):
	conn = sqlite3.connect("profile.db")
	cur = conn.cursor()
	cur.execute(" SELECT * FROM profile where name= ? OR dob=? or phone=? or bloodgroup=?  ",(name,dob,phone,bloodgroup) )
	rows = cur.fetchall()
	conn.close()
	return rows

def delete(id):
	conn = sqlite3.connect("profile.db")
	cur = conn.cursor()
	cur.execute(" DELETE FROM profile where id = ? ",(id,) )
	conn.commit()
	conn.close()


def update(id,name,dob,phone,bloodgroup):
	conn = sqlite3.connect("profile.db")
	cur = conn.cursor()
	cur.execute(" UPDATE profile SET name =? , dob = ?, phone=?,bloodgroup=? where id =?",(name,dob,phone,bloodgroup,id) )
	conn.commit()
	conn.close()


connect()

#update(4,"Smith","23-10-1987",919991,"A+")
#print(view())
