from ..helpers import categories

class GetCategories(object):
    '''
    classdocs
    '''


    @staticmethod
    def get(udao, location = 'Natal'):
        dic = {}
        for u in udao.fetchall():
            if location in u.location:
                for p in u.pages:
                    if categories.categories[p.category] in dic:
                        dic[categories.categories[p.category]] += 1
                    else:
                        dic[categories.categories[p.category]] = 1
        print(dic)
        return dic