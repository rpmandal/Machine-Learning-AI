## Generated Story 7611939191969964016
* greet
    - utter_ask_howcanhelp
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_check_location
    - slot{"location_match": "zero"}
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* send_email{"budget": "1"}
    - slot{"budget": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - slot{"location": "allahabad"}
    - utter_ask_restaurant_details_required
    - utter_ask_email_id
* send_email{"email": "upgrad.aiml20@gmail.com"}
    - slot{"email": "upgrad.aiml20@gmail.com"}
    - utter_email_sent
    - export

