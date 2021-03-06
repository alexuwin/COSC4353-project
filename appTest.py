""" 
CONTRIBUTIONS:
Mohamed Farah - login/registration tests (lines 13~44)
Alex Nguyen - profile tests (lines 45~158)
Justin Lam - fuel quote tests (lines 166~371)

COVERAGE REPORT:
Name         Stmts   Miss  Cover
--------------------------------
app.py         218     76    65%
appTest.py     198      6    97%
--------------------------------
TOTAL          416     82    80%
"""

from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    #LOGIN/REGISTRATION TESTING
    #ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200) #request is successful
    
    #ensure that the login page loads correctly
    def test_profile_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Login' in response.data) #check if loaded with the name of page

    #ensure registration behaves correctly given valid field inputs
    def test_correct_form(self):
        tester = app.test_client(self)
        response = tester.post('/register',
            data=dict(email="username@gmail.com",
                    username= "root",
                    password= "123456"
                ))
        self.assertTrue(b'You are now registered and can log in' in response.data)
    
    #ensure login behaves correctly given invalid field inputs
    def test_incorrect_form(self):
        tester = app.test_client(self)
        response = tester.get('/login',
            data=dict(username= "root",
                    password= '126'
                ))
        self.assertTrue(b'Username not found' in response.data)
    
    #PROFILE TESTING
    #ensure that flask was set up correctly
    def test_profile(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                # Modify the session in this context block.
                sess["username"] = "alex"
            response = tester.get('/profile', content_type='html/text')
            self.assertEqual(response.status_code, 200) #request is successful


    #ensure that the profile page loads correctly
    def test_profile_loads(self):
         with app.test_client() as tester:
            with tester.session_transaction() as sess:
                # Modify the session in this context block.
                sess["username"] = "alex"
            response = tester.get('/profile', content_type='html/text')
            self.assertTrue(b'Client Profile Management' in response.data) #check if loaded with the name of page
   
    #ensure profile behaves correctly given valid field inputs
    def test_correct_form(self):
         with app.test_client() as tester:
            with tester.session_transaction() as sess:
                # Modify the session in this context block.
                sess["username"] = "alex"
            response = tester.post('/profile',
                data=dict(name="alex",
                    address1="5832 broadway street",
                    address2="1976 broadway street",
                    city="houston",
                    state="TX",
                    zip="89935"))
            self.assertTrue(b'Profile Completed!' in response.data)

    def test_address2optional_form(self):
         with app.test_client() as tester:
            with tester.session_transaction() as sess:
                # Modify the session in this context block.
                sess["username"] = "alex"
            response =tester.post('/profile',
                data=dict(name="alex",
                    address1="5832 broadway street",
                    address2="",
                    city="houston",
                    state="TX",
                    zip="89935"),
                follow_redirects=True
            )
            self.assertTrue(b'Profile Completed!' in response.data)
       
    def test_zipcodeLength_form(self):
         with app.test_client() as tester:
            with tester.session_transaction() as sess:
                # Modify the session in this context block.
                sess["username"] = "alex"
            response =tester.post('/profile',
                data=dict(name="alex",
                    address1="5832 broadway street",
                    address2="",
                    city="houston",
                    state="TX",
                    zip="89"),
                follow_redirects=True
            )
            self.assertTrue(b'zipcode is required' in response.data)
    
    def test_nameRequirement_form(self):
         with app.test_client() as tester:
            with tester.session_transaction() as sess:
                # Modify the session in this context block.
                sess["username"] = "alex"
            response =tester.post('/profile',
                data=dict(name="",
                    address1="5832 broadway street",
                    address2="1976 broadway street",
                    city="houston",
                    state="TX",
                    zip="89935"),
                follow_redirects=True
            )
            self.assertTrue(b'name is required' in response.data)
    
    def test_addressRequirement_form(self):
         with app.test_client() as tester:
            with tester.session_transaction() as sess:
                # Modify the session in this context block.
                sess["username"] = "alex"
            response =tester.post('/profile',
                data=dict(name="alex",
                    address1="",
                    address2="1976 broadway street",
                    city="houston",
                    state="TX",
                    zip="89935"),
                follow_redirects=True
            )
            self.assertTrue(b'address is required' in response.data)
    
    def test_cityRequirement_form(self):
         with app.test_client() as tester:
            with tester.session_transaction() as sess:
                # Modify the session in this context block.
                sess["username"] = "alex"
            response =tester.post('/profile',
                data=dict(name="alex",
                    address1="5832 broadway street",
                    address2="1976 broadway street",
                    city="",
                    state="TX",
                    zip="89935"),
                follow_redirects=True
            )
            self.assertTrue(b'city is required' in response.data)

    #FUEL QUOTE TESTING

    #Note: Basic profile fields such as name, address 1, address 2, city, state, zip, etc. are already covered by profile management (profileBackend.py / profileTest.py)
    #-and thus do not need to be tested in fuelquoteBackend.py / fuelquoteTest.py

    #ensure that flask was set up correctly
    def test_fuelquote(self):
         with app.test_client() as tester:
            with tester.session_transaction() as sess:
                # Modify the session in this context block.
                sess["username"] = "alex"
            response = tester.get('/fuelquote', content_type='html/text')
            self.assertEqual(response.status_code, 200) #request is successful

    #ensure that page loaded correctly
    def test_fuelquoteform_loads(self):
         with app.test_client() as tester:
            with tester.session_transaction() as sess:
                # Modify the session in this context block.
                sess["username"] = "alex"
            response = tester.get('/fuelquote', content_type='html/text')
            self.assertTrue(b'Fuel Quote Form' in response.data)
    
    #tests gallons empty (invalid)
    def test_gallons_empty_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "alex"
            response = tester.post('/fuelquote', 
                data=dict(gallons = ""))

    #tests gallons negative (invalid)
    def test_gallons_negative_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "alex"
            response = tester.post('/fuelquote', 
                data=dict(gallons = "-5"))

    #tests gallons zero (invalid)
    def test_gallons_zero_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "alex"
            response = tester.post('/fuelquote', 
                data=dict(gallons = "0"))

    #tests delivery_date empty (invalid)
    def test_delivery_date_empty_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "alex"
            response = tester.post('/fuelquote', 
                data=dict(delivery_date = ""))
    
    #tests delivery_date past (invalid)
    def test_delivery_date_past_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "alex"
            response = tester.post('/fuelquote', 
                data=dict(delivery_date = "2022-03-11"))

    #tests delivery_date present (valid)
    def test_delivery_date_present_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "alex"
            response = tester.post('/fuelquote', 
                data=dict(delivery_date = "2022-04-28"))

    #tests delivery_date future (valid)
    def test_delivery_date_future_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "alex"
            response = tester.post('/fuelquote', 
                data=dict(delivery_date = "2023-04-13"))

    #tests gallons (invalid) and delivery_date empty date (invalid)
    def test_both_empty_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "alex"
            response = tester.post('/fuelquote', 
                data=dict(gallons = "", delivery_date = ""))

    #tests gallons positive (valid)
    def test_gallons_positive_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "alex"
            response = tester.post('/fuelquote', 
                data=dict(gallons = "5"))

    #tests gallons negative (invalid) and delivery_date past date (invalid)
    def test_both_invalid_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "alex"
            response = tester.post('/fuelquote', 
                data=dict(gallons = "-6", delivery_date = "2000-03-10"))

    #tests gallons zero (invalid) and delivery_date past date (invalid)
    def test_both_invalid_2_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "alex"
            response = tester.post('/fuelquote', 
                data=dict(gallons = "0", delivery_date = "2000-03-09"))

    #tests gallons positive (valid) and delivery_date future date (valid), handles valid gallons and date (in-state, first-time)
    def test_both_valid_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "alex"
            response = tester.post('/fuelquote', 
                data=dict(gallons = "9", state = "TX", delivery_date = "2055-03-15"))

    #tests gallons positive (valid) and delivery_date past date (invalid)
    def test_valid_invalid_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "alex"
            response = tester.post('/fuelquote', 
                data=dict(gallons = "9", state = "TX", delivery_date = "1999-03-01"))

    #tests gallons zero (invalid) and delivery_date future date (valid)
    def test_invalid_valid_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "alex"
            response = tester.post('/fuelquote', 
                data=dict(gallons = "0", state = "TX", delivery_date = "2222-05-05"))

    #tests gallons negative (invalid) and delivery_date future date (valid)
    def test_invalid_valid_2_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "alex"
            response = tester.post('/fuelquote', 
                data=dict(gallons = "-999", state = "TX", delivery_date = "2223-01-01"))

    #tests valid gallons, in-state, valid date (returning user)
    def test_both_valid_2_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "alex"
            response = tester.post('/fuelquote', 
                data=dict(gallons = "1500", state = "TX", delivery_date = "2333-01-01"))
    
    #new user: justin 
    #ensure that flask was set up correctly

    #valid gallons and date, in-state (first time)
    def test_justin_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "justin"
            response = tester.post('/fuelquote', 
                data=dict(gallons = "1500", state = "TX", delivery_date = "2333-01-01"))

    #valid gallons over 1000 and date, in-state (returning)
    def test_justin_2_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "justin"
            response = tester.post('/fuelquote', 
                data=dict(gallons = "70000", state = "TX", delivery_date = "2333-01-02"))

    #valid gallons under 1000 and date, in-state (returning)
    def test_justin_3_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "justin"
            response = tester.post('/fuelquote', 
                data=dict(gallons = "57", state = "TX", delivery_date = "2333-01-03"))

    #valid gallons over 1000 and date, out-state (returning)
    def test_justin_4_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "justin"
            response = tester.post('/fuelquote', 
                data=dict(gallons = "1500", state = "CA", delivery_date = "2333-01-01"))

    #valid gallons under 1000 and date, out-state (returning)
    def test_justin_5_form(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                sess["username"] = "justin"
            response = tester.post('/fuelquote', 
                data=dict(gallons = "1", state = "CA", delivery_date = "2335-01-23"))

    #HISTORY TESTING
    #ensure that flask was set up correctly
    def test_history(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                # Modify the session in this context block.
                sess["username"] = "alex"
            response = tester.get('/history', content_type='html/text')
            self.assertEqual(response.status_code, 200) #request is successful

    #ensure that page loaded correctly
    def test_history_loads(self):
        with app.test_client() as tester:
            with tester.session_transaction() as sess:
                # Modify the session in this context block.
                sess["username"] = "alex"
            response = tester.get('/history', content_type='html/text')
            self.assertTrue(b'Fuel Quote History' in response.data)

if __name__ == '__main__':
    unittest.main()