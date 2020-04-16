## Generated Story -2528105024397901646
* greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_price
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_restaurant_details_required
    - utter_ask_email_id
* send_email{"email": "upgrad.aiml19@gmail.com"}
    - slot{"email": "upgrad.aiml19@gmail.com"}
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -3057019063228234566
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_restaurant_details_required
    - utter_ask_email_id
* send_email{"email": "upgrad.aiml20@gmail.com"}
    - slot{"email": "upgrad.aiml20@gmail.com"}
    - utter_email_sent
    - utter_goodbye
    - export

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

## Generated Story 4076876483073748030
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_restaurant_details_required
* send_email{"email": "upgrad.aiml20@gmail.com"}
    - slot{"email": "upgrad.aiml20@gmail.com"}
    - utter_email_sent
    - utter_goodbye
    - export

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

## Generated Story 902787536834655839
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"budget": "<300"}
    - slot{"budget": "<300"}
    - action_restaurant
    - slot{"location": "kolkata"}
    - utter_ask_restaurant_details_required
    - utter_ask_email_id
* send_email{"email": "rpmandal@gmail.com"}
    - slot{"email": "rpmandal@gmail.com"}
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story 2595074074290278050
* greet
* restaurant_search{"cuisine": "mexican", "location": "hyderabad"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "hyderabad"}
    - utter_ask_price
* restaurant_search{"budget": "300-1000"}
    - slot{"budget": "300-1000"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - utter_ask_restaurant_details_required
    - utter_ask_email_id
* send_email{"email": "upgrad.aiml20@gmail.com"}
    - slot{"email": "upgrad.aiml20@gmail.com"}
    - utter_email_sent
    - utter_goodbye
    - export
	
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
	
## Generated Story 2155450018862087804
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "goa"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "goa"}
    - utter_ask_price
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_restaurant
    - slot{"location": "goa"}
    - utter_ask_restaurant_details_required
    - utter_ask_email_id
* send_email{"email": "upgrad.aiml20@gmail.com"}
    - slot{"email": "upgrad.aiml20@gmail.com"}
    - utter_email_sent
    - utter_goodbye
    - export
	
## Generated Story -4098869035717337936
* greet
    - utter_greet
* restaurant_search{"location": "durgapur"}
    - slot{"location": "durgapur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search
    - utter_ask_price
* restaurant_search{"budget": "600"}
    - slot{"budget": "600"}
    - action_restaurant
    - slot{"location": "durgapur"}
    - utter_ask_restaurant_details_required
    - utter_ask_email_id
* send_email{"email": "upgrad.aiml20@gmail.com"}
    - slot{"email": "upgrad.aiml20@gmail.com"}
    - utter_email_sent
    - utter_goodbye
    - export
	
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

