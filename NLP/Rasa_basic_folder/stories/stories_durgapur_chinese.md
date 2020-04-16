## Generated Story -4098869035717337936
* greet
    - utter_greet
* restaurant_search{"location": "durgapur"}
    - slot{"location": "durgapur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search
    - utter_ask_price
* restaurant_search{"budget": "600"}
    - slot{"budget": "600"}
    - action_restaurant
    - slot{"location": "durgapur"}
    - utter_ask_restaurant_details_required
    - utter_ask_email_id
* send_email{"email": "upgrad.aiml20@gmail.com"}
    - slot{"email": "upgrad.aiml20@gmail.com"}
    - utter_email_sent
    - utter_goodbye
    - export

