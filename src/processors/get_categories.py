from ..helpers import categories

class GetCategories(object):
    '''
    classdocs
    '''


    @staticmethod
    def get_as_string(udao, location = 'Natal'):
        cs = ''
        for u in udao.fetchall():
            if location in u.location:
                for p in u.pages:
                    cs += (categories.categories_no_space[p.category] + ' ')
        return cs


    @staticmethod
    def get_as_dict(udao, location = 'Natal'):
        dic = {}
        for u in udao.fetchall():
            if location in u.location:
                for p in u.pages:
                    if categories.categories_with_spaces[p.category] in dic:
                        dic[categories.categories_with_spaces[p.category]] += 1
                    else:
                        dic[categories.categories_with_spaces[p.category]] = 1
        return dic
