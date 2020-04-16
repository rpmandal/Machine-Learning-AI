## Generated Story -2528105024397901646
* greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_restaurant_details_required
    - utter_ask_email_id
* send_email{"email": "upgrad.aiml19@gmail.com"}
    - slot{"email": "upgrad.aiml19@gmail.com"}
    - utter_email_sent
    - utter_goodbye
    - export

