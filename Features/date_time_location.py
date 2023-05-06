# from datetime import datetime
# import pytz
# from time import sleep
# from Body.speak import speak

# import requests
# import json
# from playsound import playsound

# # def track_location():
# #     # Use a third-party service to get the user's IP address
# #     url = 'https://api.ipify.org/'
# #     response = requests.get(url)
# #     ip_address = response.text

# #     # Use Google Maps API to get the user's location
# #     url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={ip_address}&key=YOUR_API_KEY'
# #     response = requests.get(url)
# #     data = json.loads(response.text)

# #     # Extract the user's address information from the response
# #     area = None
# #     locality = None
# #     if data['status'] == 'OK':
# #         results = data['results']
# #         if len(results) > 0:
# #             result = results[0]
# #             address_components = result['address_components']
# #             for component in address_components:
# #                 if 'administrative_area_level_2' in component['types']:
# #                     area = component['long_name']
# #                 elif 'locality' in component['types']:
# #                     locality = component['long_name']

# #     return area, locality

# # # Call the function to get the user's location and speak it out loud
# # def get_location():
# #     area, locality = track_location()
# #     if area and locality:
# #         message = f"You are currently in {locality}, {area}"
# #     else:
# #         message = "Sorry, I couldn't determine your location"
# #     print(message)
# #     speak(message)



# def get_date():
#     """
#     Gets current date and speaks it out
#     """
#     # Get current date in IST
#     timezone = pytz.timezone('Asia/Kolkata') # IST timezone
#     current_date = datetime.now(timezone).strftime("%d-%m-%Y")

#     # Speak the current date
#     speak(f"Today is {current_date}")

# def get_time():
#     """
#     Gets current time and speaks it out
#     """
#     # Get current time in IST
#     timezone = pytz.timezone('Asia/Kolkata') # IST timezone
#     current_time = datetime.now(timezone).strftime("%I:%M %p")

#     # Speak the current time
#     speak(f"The time is {current_time}")

# def get_day():
#     """
#     Gets current day and speaks it out
#     """
#     # Get current day in IST
#     timezone = pytz.timezone('Asia/Kolkata') # IST timezone
#     current_day = datetime.now(timezone).strftime("%A")

#     # Speak the current day
#     speak(f"Today is {current_day}")

# def get_year():
#     """
#     Gets the current year and speaks it out
#     """
#     # Get current year in IST
#     timezone = pytz.timezone('Asia/Kolkata') # IST timezone
#     current_year = datetime.now(timezone).strftime("%Y")

#     # Speak the current year
#     speak(f"The current year is {current_year}")

# # Example usage
# # get_location()
# # get_date()
# # get_time()
