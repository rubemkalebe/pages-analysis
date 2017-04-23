from helpers import categories

class GetCategories(object):
    '''
    classdocs
    '''


    @staticmethod
    def get(udao, location = 'Natal'):
        cs = ''
        for u in udao.fetchall():
            if location in u.location:
                for p in u.pages:
                    cs += (categories.categories[p.category] + ' ')
        return cs