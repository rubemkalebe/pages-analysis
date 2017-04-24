import numpy
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

class GenerateWordcloud(object):
    '''
    classdocs
    '''


    def __init__(self, source):
        '''
        Constructor
        '''
        self.__SHAPE_PATH = 'res/facebook-letter.png' 
        self.__source = source
        
        facebook_mask = numpy.array(Image.open(self.__SHAPE_PATH))
        self.__wc = WordCloud(background_color = "white", max_words = 7000,
                            mask = facebook_mask, stopwords = STOPWORDS)
        
    def generate(self):
        return self.__wc.generate_from_frequencies(self.__source)
    
    def save_to_file(self, OUTPUT_PATH = 'wordcloud.png'):
        self.__wc.to_file(OUTPUT_PATH)