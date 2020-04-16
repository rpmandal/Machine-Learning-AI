## Generated Story 3660541233946105343
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "pondicherry"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "pondicherry"}
    - utter_ask_price
    - utter_ask_price
* restaurant_search{"budget": "2"}
    - slot{"budget": "2"}
    - action_restaurant
    - slot{"location": "pondicherry"}
    - utter_ask_restaurant_details_required
    - utter_no_email_sent
    - utter_goodbye
    - export

