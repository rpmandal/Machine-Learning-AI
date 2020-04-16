## Generated Story -3057019063228234566
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_restaurant_details_required
    - utter_ask_email_id
* send_email{"email": "upgrad.aiml20@gmail.com"}
    - slot{"email": "upgrad.aiml20@gmail.com"}
    - utter_email_sent
    - utter_goodbye
    - export

