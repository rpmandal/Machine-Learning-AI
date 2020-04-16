## Generated Story 2155450018862087804
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "goa"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "goa"}
    - utter_ask_price
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_restaurant
    - slot{"location": "goa"}
    - utter_ask_restaurant_details_required
    - utter_ask_email_id
* send_email{"email": "upgrad.aiml20@gmail.com"}
    - slot{"email": "upgrad.aiml20@gmail.com"}
    - utter_email_sent
    - utter_goodbye
    - export

