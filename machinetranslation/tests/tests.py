import unittest 
from translator import english_to_french, french_to_english
class testTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('car'),'voiture')
        self.assertEqual(english_to_french('Home'),'Accueil')
    
    def test_french_to_english(self):
        self.assertEqual(french_to_english('voiture'),'car')
        self.assertEqual(french_to_english('Accueil'),'Home')

if __name__=='__main__':
    unittest.main()
    