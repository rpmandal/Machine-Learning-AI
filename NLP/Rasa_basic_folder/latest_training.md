## Generated Story 6442115427898973804
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "dili"}
    - slot{"location": "dili"}
    - utter_ask_price
* restaurant_search
    - utter_default
* restaurant_search{"location": "rs.300"}
    - slot{"location": "rs.300"}
    - action_restaurant
    - slot{"location": "rs.300"}
    - utter_goodbye
    - utter_goodbye
    - export

