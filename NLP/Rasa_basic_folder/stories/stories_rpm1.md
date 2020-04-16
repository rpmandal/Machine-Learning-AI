## Generated Story 4076876483073748030
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_restaurant_details_required
* send_email{"email": "upgrad.aiml20@gmail.com"}
    - slot{"email": "upgrad.aiml20@gmail.com"}
    - utter_email_sent
    - utter_goodbye
    - export

