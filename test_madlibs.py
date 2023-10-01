import unittest
from madlibs import app
from stories import story

class TestMadlibsApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_ask_questions(self):
        with self.client:
            response = self.client.get('/')
            self.assertIn(b'place', response.data)  

    def test_show_story(self):
        with self.client:
            response = self.client.get('/story', query_string={"place": "forest", "noun": "bear", "verb": "dance", "adjective": "happy", "plural_noun": "trees"})
            self.assertIn(b'Once upon a time in a long-ago forest', response.data)
            

if __name__ == "__main__":
    unittest.main()
