from ..model.user import User
from ..model.page import Page

class UserDAO(object):
    '''
    classdocs
    '''


    def __init__(self, db):
        '''
        Constructor
        '''
        self.__db = db
        
    def insert(self, _user):
        if(self.find_user(_user.facebook_id) == None):
            self.__db.users.insert_one(_user.user_as_dict())
    
    def fetchall(self):
        users = set()
        empCol = self.__db.users.find()
        for emp in empCol:
            u = User(
                facebook_id = emp['facebook_id'],
                initials = emp['initials'],
                gender = emp['gender'],
                birthday = emp['birthday'],
                location = emp['location'],
                pages = [(Page(page_name = x['page_name'], page_id = x['page_id'],
                            category = x['category'])) for x in emp['pages']]
            )
            users.add(u)
        return users
    
    def clear(self):
        self.__db.users.remove({})
        
    def find_user(self, fid):
        dic = self.__db.users.find_one({'facebook_id' : fid})
        if(dic != None):
            u = User(
                facebook_id = dic['facebook_id'],
                initials = dic['initials'],
                gender = dic['gender'],
                birthday = dic['birthday'],
                location = dic['location'],
                pages = dic['pages']
            )
            return u
        else:
            return None