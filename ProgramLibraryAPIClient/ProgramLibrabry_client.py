import requests
import config

BASE_URL = config.PROGRAM_LIBRARY_API_SERVER

class ClientCalls:
    def call_programs_api(self):
        response = requests.get(BASE_URL + "api/v1/programs")
        print("\nJson response for Programs:")
        print(response.json())

    def call_sections_api(self):
        response = requests.get(BASE_URL + "api/v1/programs/sections/1")
        print("\nJson response for Sections:")
        print(response.json())

    def call_activities_api(self):
        response = requests.get(BASE_URL + "api/v1/programs/activities/1")
        print("\nJson response for Activities:")
        print(response.json())

    def call_activity_questionnaires_api(self):
        response = requests.get(BASE_URL + "api/v1/programs/activity_questionnaires/1")
        print("\nJson response for Questionnaires:")
        print(response.json())


if __name__ == "__main__":
    client = ClientCalls()
    client.call_programs_api()
    client.call_sections_api()
    client.call_activities_api()
    client.call_activity_questionnaires_api()