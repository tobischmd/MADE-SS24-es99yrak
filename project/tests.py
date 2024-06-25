import unittest
import os
import sqlite3

class TestDataPipeline(unittest.TestCase):
    
    def test_database_is_created(self):
        if os.path.exists('./data/population.sqlite'):
            os.remove('./data/population.sqlite')
            
        os.system('sh ./project/pipeline.sh')
        
        self.assertTrue(os.path.exists('./data/population.sqlite'))
        
        
    def test_database_not_empty(self):
        if os.path.exists('./data/population.sqlite'):
            os.remove('./data/population.sqlite')
            
        os.system('sh ./project/pipeline.sh')
        
        self.assertTrue(os.path.exists('./data/population.sqlite'))
        
        conn = sqlite3.connect('./data/population.sqlite')
        
        cur = conn.cursor()
        
        cur.execute("SELECT COUNT(*) FROM population")
        rows = cur.fetchall()
        self.assertTrue(rows[0][0] > 0)
        
        cur.execute("SELECT COUNT(*) FROM polution")
        rows = cur.fetchall()
        self.assertTrue(rows[0][0] > 0)
        
        cur.execute("SELECT COUNT(*) FROM finalData")
        rows = cur.fetchall()
        self.assertTrue(rows[0][0] > 0)
        conn.close()
        
        
        
if __name__ == '__main__':
    unittest.main()