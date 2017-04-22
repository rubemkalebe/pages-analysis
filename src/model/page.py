

class Pages(obejct):

	def _init_(self,page_name, page_id, category): 
		self.__page_name = page_name
		self.__page_id = page_id
		self.__category = category
	

	def set_id(self,page_id):
		self.__page_id = page_id

	def get_id(self):
		return self.__page_id

	def set_name(self,name):
		self.__page_name = page_name

	def get_name(self):
		return self.__page_name

	def set_category(self,category):
		self.__category = category

	def get_category(self):
		return self.__category


	def page_as_dict():
		 return {
            'page_id' : self.__page_id,
            'page_name' : self.__page_name,
            'category' : self.__category,
            
        }
    page_id = property(get_id, set_id, None, None)
    page_name = property(get_name, set_name, None, None)
    category = property(get_category, set_category, None, None)
    



    