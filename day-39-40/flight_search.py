import os
import requests
import time

auth_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
city_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
flight_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"


class FlightSearch:

    def __init__(self):
        self._api_key = os.environ["AMADEUS_KEY"]
        self._api_secret = os.environ["AMADEUS_SECRET"]
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }

        response = requests.post(url=auth_endpoint, headers=header, data=body)
        response.raise_for_status()
        return response.json()['access_token']
        
    def get_destination_code(self, city_name, retries=5):

        headers = {"Authorization": f"Bearer {self._token}"}

        query = {
            "keyword": city_name,
            "max": "1",
            "include": "AIRPORTS",
        }
        for attempt in range(retries):
            try:
                response = requests.get(
                    url=city_endpoint,
                    headers=headers,
                    params=query
                )
                response.raise_for_status()

                data = response.json()
                print(
                    f"Status code {response.status_code}. Airport IATA: {data}")

                # Check if data is found
                if "data" not in data or not data["data"]:
                    print(f"No data found for {city_name}.")
                    return "Not Found"

                # Extract IATA code from the first result
                code = data["data"][0].get("iataCode", "Not Found")
                return code

            except requests.exceptions.HTTPError as e:
                print(f"Attempt {attempt + 1} failed for {city_name}: {e}")
                if attempt < retries - 1:
                    time.sleep(4)
                    continue
                print(
                    f"Max retries reached for {city_name}. Returning 'Not Found'.")
                return "Not Found"
            except (KeyError, IndexError) as e:
                print(f"Error parsing response for {city_name}: {e}")
                return "Not Found"
            
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url=flight_endpoint,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()
