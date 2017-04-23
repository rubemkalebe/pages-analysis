

class User(object):

	def __init__(self,facebook_id, initials, gender, birthday, location,pages): 
		self.__facebook_id = facebook_id
		self.__initials = initials
		self.__gender = gender 
		self.__birthday = birthday
		self.__location = location
		self.__pages = pages

	

	def set_id(self,facebook_id):
		self.__facebook_id = facebook_id

	def get_id(self):
		return self.__facebook_id

	def set_initials(self,initials):
		self.__initials_id = initials

	def get_initials(self):
		return self.__initials

	def set_gender(self,gender):
		self.__gender = gender

	def get_gender(self):
		return self.__gender

	def set_birthday(self,birthday):
		self.__birthday = birthday

	def get_birthday(self):
		return self.__birthday

	def set_location(self,location):
		self.__location = location

	def get_location(self):
		return self.__location

	def set_pages(self, pages):
		self.__pages = pages

	def get_pages(self):
		return self.__pages

	def user_as_dict(self):
		return {
            'facebook_id' : self.__facebook_id,
            'initials' : self.__initials,
            'gender' : self.__gender,
            'birthday' : self.__birthday,
            'location' : self.__location,
            'pages' : [x.page_as_dict() for x in self.__pages]
        }
	
	facebook_id = property(get_id, set_id, None, None)
	initials = property(get_initials, set_initials, None, None)
	gender = property(get_gender, set_gender, None, None)
	birthday = property(get_birthday, set_birthday, None, None)
	location = property(get_location, set_location, None, None)
	pages = property(get_pages, set_pages, None, None)