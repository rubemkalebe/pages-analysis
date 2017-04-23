import facebook
import requests
from ..helpers import token
from ..model.user import User
from ..model.page import Page
from ..database.user_dao import UserDAO

from tqdm import tqdm

class FriendsProcessor(object):
    '''
    classdocs
    '''


    def __init__(self, db):
        '''
        Constructor
        '''
        self.__graph = facebook.GraphAPI(access_token = token.acess_token, version = '2.3')
        self.__userDAO = UserDAO(db)
        
    def processFriends(self):
        friends = self.__graph.get_object('me/friends')
        
        while True:
            try:
                self.processResult(friends)
                friends = requests.get(friends['paging']['next']).json()
            except KeyError:
                break
            
    def processResult(self, friends):
        for dic in tqdm(friends['data']):
            self.processFriend(dic['id'])
        
    def processFriend(self, fid):
        likes = self.hasLikes(fid)
        if len(likes['data']) > 0 and self.__userDAO.find_user(fid) == None:
            friend = self.__graph.get_object(fid)
            
            u = User(
                facebook_id = friend['id'],
                initials = friend['first_name'][0] + friend['last_name'][0],
                gender = friend['gender'],
                birthday = '',
                location = '',
                pages = []
            )
            
            try:
                u.birthday = friend['birthday']
            except KeyError:
                u.birthday = ''
                
            try:
                u.location = friend['location']['name']
            except KeyError:
                u.location = ''
                
            self.processLikes(likes, u)
            
            self.__userDAO.insert(u)
        
    def hasLikes(self, fid):
        return self.__graph.get_object(fid + '/likes')
    
    def processLikes(self, likes, user):
        while True:
            try:
                for dic in likes['data']:
                    try:
                        user.pages.append(Page(
                            page_name = dic['name'],
                            page_id = dic['id'],
                            category = dic['category']
                        ))
                    except KeyError:
                        continue
                likes = requests.get(likes['paging']['next']).json()
            except KeyError:
                break