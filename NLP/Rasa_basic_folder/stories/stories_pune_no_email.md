## Generated Story 13626589825782500
* greet
    - utter_ask_howcanhelp
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"budget": "300-800"}
    - slot{"budget": "300-800"}
    - action_restaurant
    - slot{"location": "pune"}
    - utter_ask_restaurant_details_required
* deny
    - utter_no_email_sent
    - utter_goodbye
    - export

