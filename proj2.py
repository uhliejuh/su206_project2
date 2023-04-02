from bs4 import BeautifulSoup
import re
import os
import csv
import unittest
#who am I: ELijah Cantu
#who did you work with: Syeda Reza, 
# IMPORTANT NOTE:
"""
If you are getting "encoding errors" while trying to open, read, or write from a file, 
add the following argument to any of your open() functions:

    encoding="utf-8-sig"

An example of that within the function would be:
    open("filename", "r", encoding="utf-8-sig")

There are a few special characters present from Airbnb that aren't defined in standard UTF-8 
(which is what Python runs by default). 
This is beyond the scope of what you have learned so far in this class, 
so we have provided this for you just in case it happens to you. Good luck!
"""
#syeda
def get_listings_from_search_results(html_file):
    pass

#syeda
def get_listing_information(listing_id):
    """
    Write a function to return relevant information in a tuple from an Airbnb listing id.
    NOTE: Use the static files in the html_files folder, do NOT send requests to the actual website.
    Information we're interested in:
        string - Policy number: either a string of the policy number, "Pending", or "Exempt"
            This field can be found in the section about the host.
            Note that this is a text field the lister enters, this could be a policy number, or the word
            "pending" or "exempt" or many others. Look at the raw data, decide how to categorize them into
            the three categories.
        string - Place type: either "Entire Room", "Private Room", or "Shared Room"
            Note that this data field is not explicitly given from this page. Use the
            following to categorize the data into these three fields.
                "Private Room": the listing subtitle has the word "private" in it
                "Shared Room": the listing subtitle has the word "shared" in it
                "Entire Room": the listing subtitle has neither the word "private" nor "shared" in it
        int - Nightly rate: cost of airbnb per night
.
    (
        policy number,
        place type,
        nightly rate
    )
    """
    pass
    

#eljiah
def get_detailed_listing_database(html_file):
    """
    Write a function that calls the above two functions in order to return
    the complete listing information using the functions you’ve created.
    This function takes in a variable representing the location of the search results html file.
    The return value should be in this format:


    [
        (Listing Title 1,Number of Reviews 1,Listing ID 1,Policy Number 1,Place Type 1,Nightly Rate 1),
        (Listing Title 2,Number of Reviews 2,Listing ID 2,Policy Number 2,Place Type 2,Nightly Rate 2),
        ...
    ]
    """
    pass
        

#elijah
def write_csv(data, filename):
    """
    Write a function that takes in a list of tuples (called data, i.e. the
    one that is returned by get_detailed_listing_database()), sorts the tuples in
    ascending order by cost, writes the data to a csv file, and saves it
    to the passed filename. The first row of the csv should contain
    "Listing Title", "Number of Reviews", "Listing ID", "Policy Number", "Place Type", "Nightly Rate",
    respectively as column headers. For each tuple in data, write a new
    row to the csv, placing each element of the tuple in the correct column.

    When you are done your CSV file should look like this:

    Listing Title,Number of Reviews,Listing ID,Policy Number,Place Type,Nightly Rate
    title1,num_reviews1,id1,policy_number1,place_type1,cost1
    title2,num_reviews2,id2,policy_number2,place_type2,cost2
    title3,num_reviews3,id3,policy_number3,place_type3,cost3
    ...

    In order of least cost to most cost.

    This function should not return anything.
    """
    pass
    
    

#syeda
def check_policy_numbers(data):
    """
    Write a function that takes in a list of tuples called data, (i.e. the one that is returned by
    get_detailed_listing_database()), and parses through the policy number of each, validating the
    policy number matches the policy number format. Ignore any pending or exempt listings.
    Return the listing numbers with respective policy numbers that do not match the correct format.
        Policy numbers are a reference to the business license San Francisco requires to operate a
        short-term rental. These come in two forms, where # is a number from [0-9]:
            20##-00####STR
            STR-000####
    .
    Return value should look like this:
    [
        listing id 1,
        listing id 2,
        ...
    ]

    """
 


    answer = []
    for item in data:
        if item[3]  == "Exempt" or item[3] == "Pending":
            continue
        else:
            if(re.search('20\d{2}-00\d{4}STR', item[3]) or re.search('STR-000\d{4}', item[3])):
                continue
            else:
                answer.append(item[2])
                
    return answer
                



def google_scholar_searcher(query):
    """
    EXTRA POINT

    Parameter: query (str)

    Return: a list of titles in the first page (list)
    ---

    Write a function that imports requests library of Python
    and sends a request to google scholar with the passed query.
    Using BeautifulSoup, 
    find all titles and return the list of titles you see on page 1. 
    (that means, you do not need to scrape results on other pages)

    You do not need to write test cases for this question.
    """
    import requests

    # YOUR ANSWER HERE

#syeda and elijah
class TestCases(unittest.TestCase):

    def test_get_listings_from_search_results(self):
        # call get_listings_from_search_results("html_files/search_results.html")
        # and save to a local variable
        listings = get_listings_from_search_results("html_files/search_results.html")
        # check that the number of listings extracted is correct (18 listings)
        self.assertEqual(len(listings), 18)
        # check that the variable you saved after calling the function is a list
        self.assertEqual(type(listings), list)
        # check that each item in the list is a tuple
        for item in listings:
            self.assertEqual(type(item), type(tuple()))
        # check that the first title, number of reviews, and listing id tuple is correct (open the search results html and find it)
        self.assertEqual(listings[0], ('Loft in Mission District', 422, '1944564'))

        # check that the last title is correct (open the search results html and find it)
        self.assertEqual(listings[17][0],  "Guest suite in Mission District")

    def test_get_listing_information(self):
        html_list = ["467507",
                     "1944564",
                     "4614763",
                     "16204265",
                     "47705504"]
        # call get_listing_information for i in html_list:
        listing_informations = [get_listing_information(id) for id in html_list]
        # check that the number of listing information is correct (5)
        self.assertEqual(len(listing_informations), 5)
        for listing_information in listing_informations:
            # check that each item in the list is a tuple
            self.assertEqual(type(listing_information), tuple)
            # check that each tuple has 3 elements
            self.assertEqual(len(listing_information), 3)
            # check that the first two elements in the tuple are string
            self.assertEqual(type(listing_information[0]), str)
            self.assertEqual(type(listing_information[1]), str)
            # check that the third element in the tuple is an int
            self.assertEqual(type(listing_information[2]), int)
        # check that the first listing in the html_list has the correct policy number
        self.assertEqual(listing_informations[0][0], 'STR-0005349')
        

        # check that the last listing in the html_list has the correct place type
        self.assertEqual(listing_informations[2][1], 'Entire Room')

        # check that the third listing has the correct cost
        self.assertEqual(listing_informations[-2][2], 127)

        pass

    def test_get_detailed_listing_database(self):
        # call get_detailed_listing_database on "html_files/search_results.html"
        # and save it to a variable
        detailed_database = get_detailed_listing_database("html_files/search_results.html")
        # check that we have the right number of listings (18)
        self.assertEqual(len(detailed_database), 18)
        for item in detailed_database:
            # assert each item in the list of listings is a tuple
            self.assertEqual(type(item), tuple)
            # check that each tuple has a length of 6
            self.assertEqual(len(item), 6)

        # check that the first tuple is made up of the following:
        # 'Loft in Mission District', 422, '1944564', '2022-004088STR', 'Entire Room', 181
        self.assertEqual(detailed_database[0], ('Loft in Mission District', 422, '1944564', '2022-004088STR', 'Entire Room', 181))

        # check that the last tuple is made up of the following:
        # 'Guest suite in Mission District', 324, '467507', 'STR-0005349', 'Entire Room', 165
        self.assertEqual(detailed_database[-1], ('Guest suite in Mission District', 324, '467507', 'STR-0005349', 'Entire Room', 165))

        pass

    def test_write_csv(self):
        # call get_detailed_listing_database on "html_files/search_results.html"
        # and save the result to a variable
        detailed_database = get_detailed_listing_database("html_files/search_results.html")
        # call write csv on the variable you saved
        write_csv(detailed_database, "test.csv")
        # read in the csv that you wrote
        csv_lines = []
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.csv'), 'r') as f:
            csv_reader = csv.reader(f)
            for i in csv_reader:
                csv_lines.append(i)
        # check that there are 19 lines in the csv
        self.assertEqual(len(csv_lines), 19)
        # check that the header row is correct
        self.assertEqual(csv_lines[0], ['Listing Title','Number of Reviews','Listing ID','Policy Number','Place Type','Nightly Rate'])

        # check that the next row is Private room in Mission District,198,23672181,STR-0002892,Private Room,109
        self.assertEqual(csv_lines[1], ['Private room in Mission District','198','23672181','STR-0002892','Private Room','109'])
    
        # check that the last row is Guest suite in Mission District,70,50010586,STR-0004717,Private Room,310
        self.assertEqual(csv_lines[-1], ['Guest suite in Mission District','70','50010586','STR-0004717','Private Room','310'])

        pass

    def test_check_policy_numbers(self):
        # call get_detailed_listing_database on "html_files/search_results.html"
        # and save the result to a variable
        detailed_database = get_detailed_listing_database("html_files/search_results.html")
        # call check_policy_numbers on the variable created above and save the result as a variable
        invalid_listings = check_policy_numbers(detailed_database)
        # check that the return value is a list
        self.assertEqual(type(invalid_listings), list)
        # check that there is exactly one element in the string
        self.assertEqual(len(invalid_listings), 1)
        # check that the element in the list is a string
        self.assertEqual(type(invalid_listings[0]), str)

        # check that the first element in the list is '16204265'
        self.assertEqual(invalid_listings[0],'16204265' )
        pass


if __name__ == '__main__':
    database = get_detailed_listing_database("html_files/search_results.html")
    write_csv(database, "airbnb_dataset.csv")
    non_valid_airbnbs = check_policy_numbers(database)
    unittest.main(verbosity=2)
