import requests

# Vervang de volgende waarden door je eigen LinkedIn API-clientgegevens
CLIENT_ID = ""
CLIENT_SECRET = ""
access_token = ""

# Functie om LinkedIn-token te verkrijgen
def get_access_token():
    url = 'https://www.linkedin.com/oauth/v2/accessToken'
    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(url, data=data)
    print(response.json())
    access_token = ''
    return access_token

# Functie om LinkedIn-zoekopdracht uit te voeren
def search_jobs(access_token, keywords, locations):
    url = 'https://api.linkedin.com/v2/jobSearch'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0'
    }
    params = {
        'jobTitle': keywords,
        'location': f'[{",".join(locations)}]',
        'remote': 'true',
        'contractType': 'C'
    }
    response = requests.get(url, headers=headers, params=params)
    jobs = response.json()['elements']
    return jobs

# Hoofdprogramma
def main():
    # Verkrijg toegangstoken
    access_token = get_access_token()

    # Definieer trefwoorden en locaties
    keywords = 'devops OR SRE OR platform engineer'
    locations = ['latam', 'us', 'europe']

    # Zoek naar vacatures
    jobs = search_jobs(access_token, keywords, locations)

    # Toon de gevonden vacatures
    for job in jobs:
        print(f"Titel: {job['title']}")
        print(f"Werkgever: {job['company']}")
        print(f"Locatie: {job['locationName']}")
        print(f"Type contract: {job['contractType']}")
        print(f"Beschrijving: {job['description']}")
        print("------------------------------")

if __name__ == '__main__':
    main()