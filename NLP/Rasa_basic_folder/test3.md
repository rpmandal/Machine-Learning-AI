## Generated Story -5661422030107318830
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* 
* 
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_restaurant_details_required
* 
* affirm
    - utter_ask_email_id
* send_email{"email": "sharmavarun.2009@rediffmail.com"}
    - slot{"email": "sharmavarun.2009@rediffmail.com"}
    - action_send_email
    - export

## Generated Story 4322897975368422475
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* 
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - export

