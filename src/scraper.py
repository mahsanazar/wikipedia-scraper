import requests
from bs4 import BeautifulSoup
import json




class WikipediaScraper:
    """A class for scraping leader data from the Country Leaders API"""

    def __init__(self) -> None:
        self.base_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"
        self.leaders_data = []
        self.countries = []
        self.cookie = None
        self.leaders_per_country={}
        self.leader_info_list=[]



    def refresh_cookie(self) -> object:
        """ Placeholder for refreshing cookie logic"""
        # get cookies
        cookies_response = requests.get(self.base_url+ self.cookies_endpoint)

        self.cookie = cookies_response.cookies


    def get_countries(self) -> list:
        """returns a list of the supported countries from the API"""
        #testurl= "https://country-leaders.onrender.com/status"
        #r = requests.get (testurl)
        #print(r)

        self.refresh_cookie() #refresh cookies
        response = requests.get(self.base_url + self.country_endpoint, cookies=self.cookie) #send request  to get countries
          # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the list of countries from the response JSON
            self.countries = response.json()
            # Print the list of countries
            print(self.countries)
            
        else:
            # Print an error message if the request was not successful
            print(f"Failed to retrieve countries. Status code: {response.status_code}")
    

    def get_leaders(self) -> None:
        """populates the leader_data object with the leaders of a
           country retrieved from the API"""
        
        try:
            self.refresh_cookie()
            for country in self.countries:
                response = requests.get(self.base_url + self.leaders_endpoint, cookies=self.cookie,
                                        params={'country': country}) # send request to extract leaders based on  countries
                if response.status_code == 200: #check if request is successful
                    self.leaders_per_country[country] = response.json()
                    print(f"Leaders of {country}:")
                    for leader in self.leaders_per_country[country]:# it creats a dictionary  of leaders information
                        leader_info = {
                            "first_name":leader['first_name'],
                            "last_name": leader['last_name'],
                            "wikipedia_url": leader['wikipedia_url'],
                             "country": {country}
                        }
                        self.leader_info_list.append(leader_info)  # Store leader info in the list
                        print(f"Leader: {leader['first_name']} {leader['last_name']}, Country:{country} Wikipedia Link: {leader['wikipedia_url']}")
                        print()  # Add a blank line between countries to be more readable in output
                        
                else:
                    print(f"Failed to retrieve leaders for {country}. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"An error occurred during the request: {e}")

         
    def get_first_paragraph(self) -> None:
        """returns the first paragraph (defined by the HTML tag <p>)
              with details about the leader"""
         
      
        try:
                for leader_info in self.leader_info_list:# based on dictionary of leaders info, extract wikipedi_url for each leader one by one
                    wikipedia_url = leader_info['wikipedia_url']
                    last_name= leader_info ['last_name']
                    first_name= leader_info['first_name']
                    country=leader_info['country']
                  
                    response = requests.get(wikipedia_url)# it sent request for each leader's wikipedia url
                    if response.status_code == 200:# check if it is successful
                        soup = BeautifulSoup(response.text, 'html.parser')# after request, it request to parse it for each leader's wikipedia_url
                        first_paragraph = soup.find('p').get_text() # extract the first paragraph with tag p 
                        print(f" Leader is :{first_name} {last_name} , Country :{country},  wikipedia_url is:  {wikipedia_url}: First paragpraph from this URL is : {first_paragraph}")
                    else:
                        print(f"Failed to fetch page content for {wikipedia_url}")
        except requests.RequestException as e:
                print(f"An error occurred during the request: {e}")
        
    def to_json_file(self, filepath: str) -> None:
        #"""stores the data structure into a JSON file"""
        with open(filepath, 'w') as json_file:
            json.dump(self.leader_info_list, json_file, default=self.serialize)

    def serialize(self, obj):
       """
       Custom serialization function.

        Parameters: - obj: The object to be serialized.
        Returns:
       - Serialized object: The serialized form of the input object.

        Raises:
       - TypeError: If the input object is not JSON serializable.

        This method provides custom serialization logic for objects that are not directly JSON serializable. 
        By default, it converts sets to lists. Additional custom serialization logic can be added as needed.
        """
       if isinstance(obj, set):
            return list(obj)
        # Add more custom serialization logic here if needed
       raise TypeError(f"Object of type {type(obj)} is not JSON serializable")




