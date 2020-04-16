## Generated Story -6637167219802834446
* greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "italian", "location": "chandigarh"}
    - slot{"cuisine": "italian"}
    - slot{"location": "chandigarh"}
    - utter_ask_price
* send_email{"budget": "3"}
    - slot{"budget": "3"}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - utter_ask_restaurant_details_required
    - utter_ask_email_id
* send_email{"email": "upgrad.aiml20@gmail.com"}
    - slot{"email": "upgrad.aiml20@gmail.com"}
    - utter_email_sent
    - utter_goodbye
    - export

