class Photo:

	def __init__(self, PhotoID, Speed, Film, FStop, ColorBW, Resolution, Price, DateTaken, TransID, PName, PBDate):
		self.PhotoID = PhotoID
		self.Speed = Speed
		self.Film = Film
		self.FStop = FStop
		self.ColorBW = ColorBW
		self.Resolution = Resolution
		self.Price = Price
		self.DateTaken = DateTaken
		self.TransID = TransID
		self.PName = PName
		self.PBDate = PBDate

	# add properties if needed

class Photographer:

	def __init__(self, PName, PBDate, PBio, PAddress, ColorBW, PNationality):
		self.PName = PName
		self.PBDate = PBDate
		self.PBio = PBio
		self.PAddress = PAddress
		self.ColorBW = ColorBW
		self.PNationality = PNationality

class Influences:

	def __init__(self, InspiredName, InspiriedBDate, InfluencerName, InfluencerBDate):
		self.InspiredName = InspiredName
		self.InspiriedBDate = InspiriedBDate
		self.InfluencerName = InfluencerName
		self.InfluencerBDate = InfluencerBDate

class Transact:

	def __init__(self, TransID, Tdate, CardNo, CardType, CardExpDate, TotalAmount, LoginName):
		self.TransID = TransID
		self.Tdate = Tdate
		self.CardNo = CardNo
		self.CardType = CardType
		self.CardExpDate = CardExpDate
		self.TotalAmount = TotalAmount
		self.LoginName = LoginName

class Customer:

	def __init__(self, LoginName, Password, CName, CType, BillingAddress, Str1, Str2, City, State, Zip):
		self.LoginName = LoginName
		self.Password = Password
		self.CName = CName
		self.CType = CType
		self.BillingAddress = BillingAddress
		self.Str1 = Str1
		self.Str2 = Str2
		self.City = City
		self.State = State
		self.Zip = Zip

class Landscape:

	def __init__(self, PhotoID, Place, Country):
		self.PhotoID = PhotoID
		self.Place = Place
		self.Country = Country

class Location:

	def __init__(self, Place, Country, Description):
		self.Place = Place
		self.Country = Country
		self.Description = Description

class Abstract:

	def __init__(self, PhotoID, Comment):
		self.PhotoID = PhotoID
		self.Comment = Comment

class Portrait:

	def __init__(self, PhotoID, MName, MBDate, Agency):
		self.PhotoID = PhotoID
		self.MName = MName
		self.MBDate = MBDate
		self.Agency = Agency

class Model:

	def __init__(self, MName, MBDate, MBio, MSex):
		self.MName = MName
		self.MBDate = MBDate
		self.MBio = MBio
		self.MSex = MSex


	