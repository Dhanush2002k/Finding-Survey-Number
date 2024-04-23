import requests
from bs4 import BeautifulSoup

def get_survey_numbers(district, mandal, village):
    url = "https://dharani.telangana.gov.in/knowLandStatus"
    payload = {
        "data[dist_id]": district,
        "data[mandal_id]": mandal,
        "data[village_id]": village
    }
    
    # Fetch data from the website
    response = requests.post(url, data=payload)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract survey numbers if villageList select element exists
    village_list_select = soup.find("select", id="villageList")
    if village_list_select:
        survey_numbers = [option.text.strip() for option in village_list_select.find_all("option")]
        return survey_numbers
    else:
        return None

# Example usage
district = "Your District ID"
mandal = "Your Mandal ID"
village = "Your Village ID"

survey_numbers = get_survey_numbers(district, mandal, village)
if survey_numbers:
    print("Survey Numbers:")
    for num in survey_numbers:
        print(num)
else:
    print("No survey numbers found for the specified district, mandal, and village.")
