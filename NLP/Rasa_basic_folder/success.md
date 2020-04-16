## Generated Story 5196509395573119231
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_restaurant_details_required
* affirm
    - utter_ask_email_id
* send_email{"email": "upgrad.aiml20@gmail.com"}
    - slot{"email": "upgrad.aiml20@gmail.com"}
    - action_send_email
    - export

