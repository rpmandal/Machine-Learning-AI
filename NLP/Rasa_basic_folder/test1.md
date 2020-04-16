## Generated Story -9166541132250410666
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_ask_cuisine
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_restaurant
    - slot{"location": "rishikesh"}
    - utter_ask_restaurant_details_required
    - utter_ask_email_id
    - utter_ask_email_id
    - utter_ask_email_id
    - utter_ask_email_id
    - utter_ask_email_id
    - utter_ask_email_id
    - utter_ask_email_id
* 
* 
* send_email{"email": "varun.sharma017@gmail.com"}
    - slot{"email": "varun.sharma017@gmail.com"}
    - action_send_email
    - export

