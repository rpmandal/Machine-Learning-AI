## Generated Story -4973828491974642606
* greet
    - utter_ask_howcanhelp
* inform
    - utter_ask_location
* inform{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* 
* 
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* inform{"budget": "700"}
    - slot{"budget": "700"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_restaurant_details_required
* 
* 
* affirm
    - utter_ask_email_id
* restaurant_search{"email": "sharmavarun.2009@rediffmail.com"}
    - slot{"email": "sharmavarun.2009@rediffmail.com"}
    - action_send_email
    - export

