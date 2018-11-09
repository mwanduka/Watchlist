import unittest
from app.models import Review

class ReviewTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Review class
    '''

    def setUp(self):
        '''
        Set up method will run before of the  class
        '''
        self.new_review = Movie(1234,'Python Must Be Crazy','A thrilling new Pyhton series','https://poster.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))

if __name__ == '__main__':
    unittest.main()
