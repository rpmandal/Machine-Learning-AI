## Generated Story 2595074074290278050
* greet
* restaurant_search{"cuisine": "mexican", "location": "hyderabad"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "hyderabad"}
    - utter_ask_price
* restaurant_search{"budget": "300-1000"}
    - slot{"budget": "300-1000"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - utter_ask_restaurant_details_required
    - utter_ask_email_id
* send_email{"email": "upgrad.aiml20@gmail.com"}
    - slot{"email": "upgrad.aiml20@gmail.com"}
    - utter_email_sent
    - utter_goodbye
    - export

