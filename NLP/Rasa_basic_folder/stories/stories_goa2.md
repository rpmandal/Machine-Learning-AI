## Generated Story 961456570262971987
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "goa"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "goa"}
    - utter_ask_price
* restaurant_search{"budget": "2"}
    - slot{"budget": "2"}
    - action_restaurant
    - slot{"location": "goa"}
    - utter_ask_restaurant_details_required
    - utter_no_email_sent
    - utter_goodbye
    - export

