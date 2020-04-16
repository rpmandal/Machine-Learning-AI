## Generated Story 902787536834655839
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"budget": "<300"}
    - slot{"budget": "<300"}
    - action_restaurant
    - slot{"location": "kolkata"}
    - utter_ask_restaurant_details_required
    - utter_ask_email_id
* send_email{"email": "rpmandal@gmail.com"}
    - slot{"email": "rpmandal@gmail.com"}
    - utter_email_sent
    - utter_goodbye
    - export

