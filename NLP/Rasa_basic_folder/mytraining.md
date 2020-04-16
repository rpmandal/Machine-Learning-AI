## Generated Story -7784663708474390881
* greet
    - utter_greet
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_restaurant
    - slot{"location": "delhi"}
    - export

