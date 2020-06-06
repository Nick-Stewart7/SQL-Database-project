import sqlite3
import pandas as pd
from tupleClasses import *

# conn = sqlite3.connect('Photoshop.db')
conn = sqlite3.connect(':memory:')
c = conn.cursor()

def createDB():
	# Creates Tables for the Database

	c.execute("""CREATE TABLE photo (
                PhotoID integer not null primary key,
                Speed text,
                Film text,
                FStop text,
                ColorBW text,
                Resoltion text,
                Price real,
                DateTaken integer,
                TransID integer DEFAULT None,
                PName text,
                PBDate text,
                foreign key (TransID)
                    references transact (TransID)
                        on delete SET DEFAULT
                        on update SET DEFAULT 
                foreign key (PName, PBDate)
                    references photographer (PName, PBdate)
                        on delete cascade
                        on update cascade)""")

	c.execute("""CREATE TABLE photographer (
                PName text not null,
                PBDate integer not null,
                PBio text,
                PAddress text,
                ColorBW text,
                PNationality text,
                primary key (PName, PBdate))""")

	c.execute("""CREATE TABLE influences (
                InspiredName text,
                InspiredBDate integer,
                InfluencerName text,
                InfluencerBDate integer,
                primary key (InspiredName, InspiredBDate, InfluencerName, InfluencerBDate)
                foreign key (InspiredName, InspiredBDate)
                    references photographer (PName, PBdate)
                        on delete cascade
                        on update cascade
                foreign key (InfluencerName, InfluencerBDate)
                    references photographer (PName, PBdate)
                        on delete cascade
                        on update cascade)""")

	c.execute("""CREATE TABLE transact (
                TransID integer primary key not null,
                Tdate integer,
                CardNo text,
                CardType text,
                CardExpDate text,
                TotalAmount real,
                LoginName text,
                foreign key (LoginName)
                    references customer (LoginName)
                        on delete no action
                        on update cascade)""")

	c.execute("""CREATE TABLE customer (
                LoginName text primary key not null,
                Password text,
                CName text,
                CType text,
                BillingAddress text,
                Str1 text,
                Str2 text,
                City text,
                State text,
                Zip numeric)""")

	c.execute("""CREATE TABLE landscape (
                PhotoID integer primary key not null,
                Place text,
                Country text,
                foreign key (PhotoID)
                    references photo (PhotoID)
                        on delete cascade
                        on update cascade
				foreign key (Place, Country)
                    references location (Place, Country)
                        on delete cascade
                        on update cascade)""")

	c.execute("""CREATE TABLE location (
                Place text,
                Country text,
                Description text,
                primary key (Place, Country))""")

	c.execute("""CREATE TABLE abstract (
                PhotoID integer primary key not null,
                Comment text)""")

	c.execute("""CREATE TABLE portrait (
                PhotoID integer not null,
                MName text,
                MBDate integer,
                Agency text,
                primary key (PhotoID, MName, MBDate)
                foreign key (MName, MBDate)
                    references model (MName, MBDate)
                        on delete cascade
                        on update cascade)""")

	c.execute("""CREATE TABLE model (
                MName text not null,
                MBDate integer not null,
                MBio text,
                MSex text,
                primary key (MName, MBDate))""")

	conn.commit()

def enableKeySupport():
	conn.execute('pragma foreign_keys = ON')
	# rows = conn.execute('pragma foreign_keys')
	# for r in rows:
		# print(r)

#PHOTO FUNCTIONS
def insert_photo(Photo):
    with conn:
        c.execute("INSERT INTO photo VALUES (:PhotoID, :Speed, :Film, :FStop, :ColorBW, :Resolution, :Price, :DateTaken, :TransID, :PName, :PBDate)", 
        	{'PhotoID': Photo.PhotoID, 'Speed': Photo.Speed, 'Film': Photo.Film, 'FStop': Photo.FStop, 'ColorBW': Photo.ColorBW, 'Resolution': Photo.Resolution, 'Price': Photo.Price, 'DateTaken': Photo.DateTaken, 'TransID': Photo.TransID, 'PName': Photo.PName, 'PBDate': Photo.PBDate})


def get_photo(Photo):
    c.execute("SELECT * FROM photo WHERE PhotoID =:PhotoID", {'PhotoID': Photo.PhotoID})
    return c.fetchall()


def update_photo(Photo, TransID):
    with conn:
        c.execute("""UPDATE photo SET TransID = :TransID WHERE PhotoID = :PhotoID""", 
        	{'PhotoID': Photo.PhotoID, 'TransID': TransID})


def remove_photo(Photo):
    with conn:
        c.execute("DELETE from photo WHERE PhotoID = :PhotoID",
            {'PhotoID': Photo.PhotoID})

#PHOTOGRAPHER FUNCTIONS
def insert_photographer(Photographer):
    with conn:
        c.execute("INSERT INTO photographer VALUES (:PName, :PBDate, :PBio, :PAddress, :ColorBW, :PNationality)",
            {'PName': Photographer.PName, 'PBDate': Photographer.PBDate, 'PBio': Photographer.PBio, 'PAddress': Photographer.PAddress, 'ColorBW': Photographer.ColorBW, 'PNationality': Photographer.PNationality})

def remove_photographer(Photographer):
    with conn:
        c.execute("DELETE from photographer WHERE PName = :PName AND PBDate = :PBDate",
            {'PName': Photographer.PName, 'PBDate': Photographer.PBDate})

def get_photographer(Photographer):
    c.execute("SELECT * FROM photographer WHERE PName = :PName AND PBDate = :PBDate", 
    	{'PName': Photographer.PName, 'PBDate': Photographer.PBDate})
    return c.fetchall()

#INFLUENCE FUNCTIONS
def insert_influences(Influences):
	with conn:
		c.execute("INSERT INTO influences VALUES (:InspiredName, :InspiriedBDate, :InfluencerName, :InfluencerBDate)",
			{'InspiredName': Influences.InspiredName, 'InspiriedBDate': Influences.InspiriedBDate, 'InfluencerName': Influences.InfluencerName, 'InfluencerBDate': Influences.InfluencerBDate})

def remove_influences(Influences):
	with conn:
		c.execute("DELETE from influences WHERE InspiredName = :InspiredName AND InspiriedBDate = :InspiriedBDate AND InfluencerName = :InfluencerName AND InfluencerBDate = :InfluencerBDate)",
            {'InspiredName': Influences.InspiredName, 'InspiriedBDate': Influences.InspiriedBDate, 'InfluencerName': Influences.InfluencerName, 'InfluencerBDate': Influences.InfluencerBDate})

#TRANSACTION FUNCTIONS
def insert_transact(Transact):
    with conn:
        c.execute("INSERT INTO transact VALUES (:TransID, :Tdate, :CardNo, :CardType, :CardExpDate, :TotalAmount, :LoginName)",
            {'TransID': Transact.TransID, 'Tdate': Transact.Tdate, 'CardNo': Transact.CardNo, 'CardType': Transact.CardType, 'CardExpDate': Transact.CardExpDate, 'TotalAmount': Transact.TotalAmount, 'LoginName': Transact.LoginName})

def remove_transact(Transact):
    with conn:
        c.execute("DELETE from photographer WHERE TransID = :TransID",
            {'TransID': Transact.TransID})

def get_transact(Transact, Photo):
	c.execute("CREATE VIEW trans AS SELECT PhotoID, Price, DateTaken, PName, Transact.TransID, Transact.Tdate, Transact.TotalAmount, Transact.LoginName FROM photo INNER JOIN transact ON Photo.TransID = Transact.TransID WHERE Transact.TransID = 0001")

#CUSTOMER FUNCTIONS
def insert_customer(Customer):
    with conn:
        c.execute("INSERT INTO customer VALUES (:LoginName, :Password, :CName, :CType, :BillingAddress, :Str1, :Str2, :City, :State, :Zip)",
            {'LoginName': Customer.LoginName, 'Password': Customer.Password, 'CName': Customer.CName, 'CType': Customer.CType, 'BillingAddress': Customer.BillingAddress, 'Str1': Customer.Str1, 'Str2': Customer.Str2, 'City': Customer.City, 'State': Customer.State, 'Zip': Customer.Zip})

def remove_customer(Customer):
    with conn:
        c.execute("DELETE from customer WHERE LoginName = :LoginName",
            {'LoginName': Customer.LoginName})

#LANDSCAPE FUNCTIONS
def insert_landscape(Landscape):
    with conn:
        c.execute("INSERT INTO landscape VALUES (:PhotoID, :Place, :Country)",
            {'PhotoID': Landscape.PhotoID, 'Place': Landscape.Place, 'Country': Landscape.Country})

def remove_landscape(Landscape):
    with conn:
        c.execute("DELETE from landscape WHERE PhotoID = :PhotoID",
            {'PhotoID': Landscape.PhotoID})

#LOCATION FUNCTIONS
def insert_location(Location):
    with conn:
        c.execute("INSERT INTO location VALUES (:Place, :Country, :Description)",
            {'Place': Location.Place, 'Country': Location.Country, 'Description': Location.Description})

def remove_location(Location):
    with conn:
        c.execute("DELETE from location WHERE Place = :Place AND Country = :Country",
            {'Place': Location.Place, 'Country': Location.Country})

#ABSTRACT FUNCTIONS
def insert_abstract(Abstract):
    with conn:
        c.execute("INSERT INTO abstract VALUES (:PhotoID, :Comment)",
            {'PhotoID': Abstract.PhotoID, 'Comment': Abstract.Comment})

def remove_abstract(Abstract):
    with conn:
        c.execute("DELETE from abstract WHERE PhotoID = :PhotoID",
            {'PhotoID': Abstract.PhotoID})

#PORTRAIT FUNCTIONS
def insert_portrait(Portrait):
    with conn:
        c.execute("INSERT INTO portrait VALUES (:PhotoID, :MName, :MBDate, :Agency)",
            {'PhotoID': Portrait.PhotoID, 'MName': Portrait.MName, 'MBDate': Portrait.MBDate, 'Agency': Portrait.Agency})

def remove_portrait(Portrait):
    with conn:
        c.execute("DELETE from portrait WHERE PhotoID = :PhotoID AND MName = :MName AND MBDate = :MBDate",
            {'PhotoID': Portrait.PhotoID, 'MName': Portrait.MName, 'MBDate': Portrait.MBDate})                          

#MODEL* FUNCTIONS
def insert_model(Model):
    with conn:
        c.execute("INSERT INTO model VALUES (:MName, :MBDate, :MBio, :MSex)",
            {'MName': Model.MName, 'MBDate': Model.MBDate, 'MBio': Model.MBio, 'MSex': Model.MSex})

def remove_model(Model):
    with conn:
        c.execute("DELETE from model WHERE MName = :MName AND MBDate = :MBDate",
            {'MName': Model.MName, 'MBDate': Model.MBDate}) 

#Populates tables
def populate_DB():

	#Landscape
	photographer1 = Photographer('Henri Cartier-Bresson', 19080822, 'Legendary Candid Photographer', 'Chanteloup France', 'BW', 'French')
	photographer3 = Photographer('Dorothea Lange', 18950526, 'Depression-era Photographer', 'Hoboken NJ', 'BW', 'American')
	photographer4 = Photographer('Michael Kenna', 19531120, 'Landscape Photographer', 'Widnes UK', 'BW', 'English')
	photographer6 = Photographer('Robert Capa', 19131022, 'Combat Photographer', 'Budapest Hungary', 'BW', 'Hungarian')
	#Portrait
	photographer5 = Photographer('Richard Avedon', 19230515, 'Fashion Photographer', 'New York NY', 'BW', 'American')
	photographer2 = Photographer('Annie Leibovitz', 19491002, 'Celebrity Photographer', 'Waterbury CT', 'Color', 'American')
	photographer7 = Photographer('Yousef Karsh', 19081223, 'Greatist Portait Photographer of the 20th Century', 'Mardin Turkey', 'BW', 'Armenian')
	#Abstract
	photographer8 = Photographer('Edward Weston', 18860324, 'Innovative Photographer', 'Highland Park IL', 'BW', 'American')
	photographer9 = Photographer('Robert Frank', 19241109, 'Expression Photographer', 'Zurich Switzerland', 'BW', 'Swiss')
	photographer10 = Photographer('Elliott Erwitt', 19280726, 'Absurdity Photographer', 'Paris France', 'BW', 'French')
	insert_photographer(photographer1)
	insert_photographer(photographer2)
	insert_photographer(photographer3)
	insert_photographer(photographer4)
	insert_photographer(photographer5)
	insert_photographer(photographer6)
	insert_photographer(photographer7)
	insert_photographer(photographer8)
	insert_photographer(photographer9)
	insert_photographer(photographer10)

	customer1 = Customer('PhotoLover', 'ILikePictures', 'Diane Helmsworth', 'Curator', '35', 'Highland Drive', None, 'Jackson', 'New Jersey', 85010)
	customer2 = Customer('PhotoBuyer', 'ILikePhotos', 'Mike Hunter', 'Hobbyist', '21', 'Yustopit Ave', None, 'Austin', 'Texas', 73301)
	customer3 = Customer('ThePicKing', 'doggie99', 'Carlos Harlos', 'Photographer', '12', 'Booty Lane', None, 'Newbern', 'North Carolina', 28560)
	customer4 = Customer('PhotosR4me', 'pingpong2006', 'Dave Yang', 'Hobbyist', '594', 'Country Road', None, 'Austin', 'Texas', 73301)
	customer5 = Customer('ClevlandHeat', 'ss4evr', 'Woodrow Held', 'Hobbyist', '74', 'High Road', None, 'Sacramento', 'California', 94203)
	insert_customer(customer1)
	insert_customer(customer2)
	insert_customer(customer3)
	insert_customer(customer4)
	insert_customer(customer5)

	trans1 = Transact(1, 20200501, '2356256385475698', 'Visa', '3/2022', 225.00, 'PhotoLover')
	trans2 = Transact(2, 20200510, '2356958372602694', 'Visa', '5/2022', 150.00, 'PhotoBuyer')
	trans3 = Transact(3, 20200320, '6584392753969751', 'Visa', '6/2021', 200.00, 'ThePicKing')
	trans4 = Transact(4, 20190501, '2356256385475698', 'Visa', '3/2022', 50.00, 'PhotoLover')
	trans5 = Transact(5, 20200401, '4738928882746247', 'Visa', '3/2020', 200.00, 'PhotosR4me')
	trans6 = Transact(6, 20200401, '9999993757260647', 'Visa', '3/2020', 30.00, 'ClevlandHeat')
	insert_transact(trans1)
	insert_transact(trans2)
	insert_transact(trans3)
	insert_transact(trans4)
	insert_transact(trans5)
	insert_transact(trans6)

	photo1 = Photo(100, '1/1000' , 'Kodak Tri-X 400', '4', 'BW', '1920x1080', 200.00, 19280822, 5, 'Henri Cartier-Bresson', 19080822)
	photo2 = Photo(101, '1/1000' , 'Kodak Tri-X 400', '4', 'BW', '1920x1080', 25.00, 19150822, None, 'Dorothea Lange', 18950526)
	photo3 = Photo(102, '1/1000' , 'Kodak Tri-X 400', '4', 'BW', '1920x1080', 100.00, 19601211, 3, 'Michael Kenna', 19531120)
	photo4 = Photo(103, '1/1000' , 'Kodak Tri-X 400', '4', 'BW', '1920x1080', 100.00, 19601211, 3, 'Michael Kenna', 19531120)
	photo5 = Photo(104, '1/1000' , 'Kodak Tri-X 400', '4', 'BW', '1920x1080', 75.00, 19400120, 1, 'Robert Capa', 19131022)
	photo6 = Photo(200, '1/1000' , 'Kodak Tri-X 400', '4', 'BW', '1920x1080', 75.00, 19480720, 1, 'Elliott Erwitt', 19280726)
	photo7 = Photo(201, '1/1000' , 'Kodak Tri-X 400', '4', 'BW', '1920x1080', 75.00, 19480720, 1, 'Elliott Erwitt', 19280726)
	photo8 = Photo(202, '1/1000' , 'Kodak Tri-X 400', '4', 'BW', '1920x1080', 10.00, 19480903, 6, 'Robert Frank', 19241109)
	photo9 = Photo(203, '1/1000' , 'Kodak Tri-X 400', '4', 'BW', '1920x1080', 10.00, 19120903, 6, 'Edward Weston', 18860324)
	photo10 = Photo(204, '1/1000' , 'Kodak Tri-X 400', '4', 'BW', '1920x1080', 10.00, 19120903, 6, 'Edward Weston', 18860324)
	photo11 = Photo(300, '1/1000' , 'Kodak Tri-X 400', '4', 'BW', '1920x1080', 50.00, 19530903, 2, 'Richard Avedon', 19230515)
	photo12 = Photo(301, '1/1000' , 'Kodak Tri-X 400', '4', 'BW', '1920x1080', 50.00, 19530903, 2, 'Richard Avedon', 19230515)
	photo13 = Photo(302, '1/1000' , 'Kodak Tri-X 400', '4', 'BW', '1920x1080', 50.00, 19701003, None, 'Annie Leibovitz', 19491002)
	photo14 = Photo(303, '1/1000' , 'Kodak Tri-X 400', '4', 'BW', '1920x1080', 50.00, 19701003, 4, 'Yousef Karsh', 19081223)
	photo15 = Photo(304, '1/1000' , 'Kodak Tri-X 400', '4', 'BW', '1920x1080', 50.00, 19701003, 2, 'Annie Leibovitz', 19491002)
	insert_photo(photo1)
	insert_photo(photo2)
	insert_photo(photo3)
	insert_photo(photo4)
	insert_photo(photo5)
	insert_photo(photo6)
	insert_photo(photo7)
	insert_photo(photo8)
	insert_photo(photo9)
	insert_photo(photo10)
	insert_photo(photo11)
	insert_photo(photo12)
	insert_photo(photo13)
	insert_photo(photo14)
	insert_photo(photo15)

	influence1 = Influences('Dorothea Lange', 18950526, 'Henri Cartier-Bresson', 19080822)
	influence2 = Influences('Richard Avedon', 19230515, 'Henri Cartier-Bresson', 19080822)
	influence3 = Influences('Edward Weston', 18860324, 'Robert Frank', 19241109)
	influence4 = Influences('Elliott Erwitt', 19280726, 'Robert Frank', 19241109)
	influence5 = Influences('Robert Frank', 19241109, 'Edward Weston', 18860324)
	insert_influences(influence1)
	insert_influences(influence2)
	insert_influences(influence3)
	insert_influences(influence4)
	insert_influences(influence5)

	location1 = Location('Paris', 'France', 'The city of lights')
	location2 = Location('Dustbowl', 'USA', 'The dustiest of farmlands')
	location3 = Location('Abruzzo', 'Italy', 'Beautiful Italia')
	location4 = Location('Sicily', 'Italy', 'Home of the thick pizza')
	insert_location(location1)
	insert_location(location2)
	insert_location(location3)
	insert_location(location4)

	landscape1 = Landscape(100, 'Paris', 'France')
	landscape2 = Landscape(101, 'Dustbowl', 'USA')
	landscape3 = Landscape(102, 'Abruzzo', 'Italy')
	landscape4 = Landscape(103, 'Abruzzo', 'Italy')
	landscape5 = Landscape(104, 'Sicily', 'Italy')
	insert_landscape(landscape1)
	insert_landscape(landscape2)
	insert_landscape(landscape3)
	insert_landscape(landscape4)
	insert_landscape(landscape5)

	abstract1 = Abstract(200, 'Children with masks by Elliott Erwitt')
	abstract2 = Abstract(201, 'Dog rollerskating by Elliott Erwitt')
	abstract3 = Abstract(202, 'C/O Berlin by Robert Frank')
	abstract4 = Abstract(203, 'The Flame of Recognition by Edward Weston')
	abstract5 = Abstract(204, 'Two Shells by Edward Weston')
	insert_abstract(abstract1)
	insert_abstract(abstract2)
	insert_abstract(abstract3)
	insert_abstract(abstract4)
	insert_abstract(abstract5)

	model1 = Model('Marilyn Monroe', 19260601, 'Marilyn Monroe was an American actress, model, and singer.', 'Female')
	model2 = Model('Leonardo DiCaprio', 19741111, 'Leonardo Wilhelm DiCaprio is an American actor, producer, and environmentalist.', 'Male')
	model3 = Model('Albert Einstein', 18790314, 'Albert Einstein was a German-born theoretical physicist who developed the theory of relativity, one of the two pillars of modern physics.', 'Male')
	insert_model(model1)
	insert_model(model2)
	insert_model(model3)

	portrait1 = Portrait(300, 'Marilyn Monroe', 19260601, 'BigTalent')
	portrait2 = Portrait(301, 'Marilyn Monroe', 19260601, 'BigTalent')
	portrait3 = Portrait(302, 'Leonardo DiCaprio', 19741111, 'PhotoAgency')
	portrait4 = Portrait(303, 'Albert Einstein', 18790314, 'NobelPhotos')
	portrait5 = Portrait(304, 'Marilyn Monroe', 19260601, 'BigTalent')
	insert_portrait(portrait1)
	insert_portrait(portrait2)
	insert_portrait(portrait3)
	insert_portrait(portrait4)
	insert_portrait(portrait5)

	conn.commit()

createDB()
enableKeySupport()
populate_DB()

while True:
	number = input("Which test query should I run?\n")
	if number == '1':
		c.execute("CREATE VIEW Q1 as SELECT Cname, transact.TotalAmount, transact.Tdate FROM customer INNER JOIN transact ON customer.LoginName = transact.LoginName WHERE transact.TotalAmount > 100")
		print(pd.read_sql_query("SELECT * FROM Q1",conn))
	if number == '2':
		c.execute("CREATE VIEW Q2 as SELECT PhotoID, Price, DateTaken, PName FROM photo WHERE TransID is NULL")
		print(pd.read_sql_query("SELECT * FROM Q2",conn))
	if number == '3':
		c.execute("CREATE VIEW Q3 as SELECT C.LoginName, C.CName FROM customer C WHERE NOT EXISTS (SELECT * FROM photo P, portrait M WHERE P.PhotoID = M.PhotoID AND M.MName = 'Marilyn Monroe' AND M.MBDate = 19260601 AND NOT EXISTS (SELECT * FROM transact T WHERE T.LoginName = C.LoginName AND T.TransID = P.TransID))")
		print(pd.read_sql_query("SELECT * FROM Q3",conn))
	if number == '4':
		c.execute("CREATE VIEW Q4 as SELECT InfluencerName FROM influences, photographer P WHERE influences.InspiredName = P.PName AND P.PNationality = 'American' EXCEPT SELECT InfluencerName FROM influences, photographer P WHERE influences.InspiredName = P.PName AND P.PNationality != 'American'")
		print(pd.read_sql_query("SELECT * FROM Q4",conn))
	if number == '5':
		c.execute("CREATE VIEW Q5 as SELECT PName FROM photo WHERE photoID in (SELECT photoID from portrait) EXCEPT SELECT PName FROM photo WHERE photoID in (SELECT photoID from landscape) AND (SELECT photoID from Abstract)")
		print(pd.read_sql_query("SELECT * FROM Q5",conn))
	if number == '6':
		c.execute("CREATE VIEW Q6 as SELECT transID FROM photo GROUP BY transID HAVING COUNT(transID) > 2")
		print(pd.read_sql_query("SELECT * FROM Q6",conn))
	if number == '7':
		c.execute("CREATE VIEW YphotoIDs as SELECT photoID from photo where PName in (SELECT PName FROM photo WHERE PName = 'Richard Avedon' AND photoID in (SELECT photoID from portrait) EXCEPT SELECT PName FROM photo WHERE photoID in (SELECT photoID from landscape) AND (SELECT photoID from Abstract))")
		c.execute("CREATE VIEW Q7 as SELECT MName FROM model WHERE NOT EXISTS (SELECT PhotoID FROM YphotoIDs EXCEPT SELECT PhotoID FROM portrait WHERE portrait.MName = model.MName)")
		print(pd.read_sql_query("SELECT * FROM Q7",conn))
	if number == '8':
		c.execute("CREATE VIEW Q8 as SELECT photographer.PName, photographer.PBdate, SUM(photo.Price) FROM photographer INNER JOIN photo ON photographer.PName = photo.PName GROUP BY photographer.PName ORDER BY SUM(photo.Price) DESC")
		print(pd.read_sql_query("SELECT * FROM Q8",conn))
	if number == '9':
		photoDELETE = Photo(999, '1/1000' , 'Kodak Tri-X 400', '4', 'BW', '1920x1080', 200.00, 19280822, 5, 'Henri Cartier-Bresson', 19080822)
		insert_photo(photoDELETE)
		print(pd.read_sql_query("SELECT * FROM photo",conn))
		c.execute("DELETE FROM Photo WHERE PhotoID = 999")
		print(pd.read_sql_query("SELECT * FROM photo",conn))
	if number == '10':
		photoUPDATE = Photo(999, '1/1000' , 'Kodak Tri-X 400', '4', 'BW', '1920x1080', 200.00, 19280822, 5, 'Henri Cartier-Bresson', 19080822)
		insert_photo(photoUPDATE)
		print(pd.read_sql_query("SELECT * FROM photo",conn))
		c.execute("UPDATE photo SET PName = 'Yousef Karsh', PBDate = 19081223 WHERE photoID = 999")
		print(pd.read_sql_query("SELECT * FROM photo",conn))
	if number == '11':
		c.execute ("CREATE VIEW Q11 as SELECT SUM(TotalAmount), customer.LoginName, customer.CName FROM transact INNER JOIN customer ON customer.LoginName = transact.LoginName GROUP BY transact.LoginName")
		print(pd.read_sql_query("SELECT * FROM Q11",conn))
	if number == '12':
		c.execute ("CREATE VIEW Q12 as SELECT SUM(Price), photographer.PName FROM photo INNER JOIN photographer ON photo.PName = photographer.PName WHERE photo.TransID IS NOT NULL GROUP BY photo.PName")
		print(pd.read_sql_query("SELECT * FROM Q12",conn))
	if number == '13':
		print("Abstract")
		c.execute ("CREATE VIEW Q13a as SELECT SUM(Price) FROM photo INNER JOIN abstract ON abstract.PhotoID = photo.PhotoID WHERE photo.TransID IS NOT NULL")
		print(pd.read_sql_query("SELECT * FROM Q13a",conn))
		print("Landscape")
		c.execute ("CREATE VIEW Q13b as SELECT SUM(Price) FROM photo INNER JOIN landscape ON landscape.PhotoID = photo.PhotoID WHERE photo.TransID IS NOT NULL")
		print(pd.read_sql_query("SELECT * FROM Q13b",conn))
		print("Portrait")
		c.execute ("CREATE VIEW Q13c as SELECT SUM(Price) FROM photo INNER JOIN portrait ON portrait.PhotoID = photo.PhotoID WHERE photo.TransID IS NOT NULL")
		print(pd.read_sql_query("SELECT * FROM Q13c",conn))
	if number == '14':
		print(pd.read_sql_query("SELECT SUM(TotalAmount), TransID, Tdate FROM transact GROUP BY Tdate ORDER BY SUM(TotalAmount) DESC LIMIT 3",conn))
	if number == 'done' or number == "Done":
		print("CYA LATER ALLIGATOR")
		break

#c.execute("SELECT name FROM sqlite_master WHERE type='table';")
#print(c.fetchall())
# print(c.fetchone())
conn.close()