############################### CHATBOT CASE STUDY #######################################

Objective of Case Study :-

1.The main objective of the case study is to look for the restaurant based on the location cuisine type and budget provided by the user.

2.The extracted information from above input is sent to the user's email Id based on his consent.

Main Files used in the Project:-

1.Actions.py:- 

This file contains the entire codes various actions written for fetching the restaurant,Email sending, Location Validation.

2.restaurant_domain.yml :-

This is the domain file containing various intents,entity and utterance defined also contains various actions attached to each utterance.

3.Zomatopy.py:-

This file contains the zomato api's used for fetching the Restaurant.

4.Data.json Files:-

This File contains the trained data on rasa-nlu-trainer, Following Data has been used to train our Chatbot.

5.nlu_model.py File:-

This file is used to load the domain File.

6.train_init.py File:-

This file is used to train the model based on the data.json file also it is used for the compilation of the action.py file.

7.train_online.py file :-

This File is used for online training of the bot and rectifying the mistakes created by bot in action and intent classification.

8.Dialog_flow_management.py File :-

This File is used for testing the trained File .



Pre-Requisites for running the chatbot :-

1.A virtual Environment has been created for intsalling below mentioned packages.

absl-py==0.8.1
APScheduler==3.5.1
astor==0.8.0
attrs==19.2.0
Automat==0.7.0
beautifulsoup4==4.8.1
bleach==1.5.0
blis==0.4.1
boto3==1.9.249
botocore==1.12.249
certifi==2019.9.11
cffi==1.12.3
characteristic==14.3.0
chardet==3.0.4
Click==7.0
cloudpickle==1.2.2
colorama==0.4.1
coloredlogs==10.0
colorhash==1.0.2
ConfigArgParse==0.13.0
constantly==15.1.0
cycler==0.10.0
cymem==2.0.2
decorator==4.4.0
docopt==0.6.2
docutils==0.15.2
en-core-web-md==2.2.0
en-core-web-sm==2.2.0
fakeredis==0.10.3
fbmessenger==5.2.0
Flask==1.0.2
Flask-Cors==3.0.4
future==0.16.0
gast==0.3.2
gevent==1.4.0
graphviz==0.8.3
greenlet==0.4.15
grpcio==1.24.1
h5py==2.7.1
html5lib==0.9999999
humanfriendly==4.18
hyperlink==19.0.0
idna==2.6
importlib-metadata==0.23
incremental==17.5.0
itsdangerous==1.1.0
Jinja2==2.10.3
jmespath==0.9.4
joblib==0.14.0
jsonpickle==0.9.6
jsonschema==3.1.1
Keras==2.1.6
Keras-Applications==1.0.8
Keras-Preprocessing==1.1.0
kiwisolver==1.1.0
klein==19.6.0
Markdown==3.1.1
MarkupSafe==1.1.1
matplotlib==3.1.1
mattermostwrapper==2.1
more-itertools==7.2.0
murmurhash==1.0.2
networkx==2.1
numpy==1.14.3
packaging==19.2
pandas==0.25.2
pathlib==1.0.1
plac==0.9.6
preshed==3.0.2
protobuf==3.10.0
pycparser==2.19
PyHamcrest==1.9.0
PyJWT==1.7.1
pykwalify==1.6.0
pypandoc==1.4
pyparsing==2.4.2
pyreadline==2.1
pyrsistent==0.15.4
PySocks==1.7.1
python-crfsuite==0.9.6
python-dateutil==2.8.0
python-telegram-bot==10.1.0
pytz==2019.3
PyYAML==5.1.2
rasa-core==0.10.1
rasa-nlu==0.12.3
redis==2.10.6
requests==2.18.4
ruamel.yaml==0.15.37
s3transfer==0.2.1
scikit-learn==0.19.1
scipy==1.3.1
simplejson==3.16.0
six==1.11.0
sklearn-crfsuite==0.3.6
slackclient==1.2.1
soupsieve==1.9.4
spacy==2.2.1
srsly==0.1.0
tabulate==0.8.5
tensorboard==1.8.0
tensorflow==1.8.0
termcolor==1.1.0
thinc==7.1.1
tqdm==4.23.3
Tubes==0.2.0
twilio==6.14.0
Twisted==19.7.0
typing==3.6.4
tzlocal==2.0.0
urllib3==1.22
wasabi==0.2.2
websocket-client==0.54.0
Werkzeug==0.16.0
wincertstore==0.2
zipp==0.6.0
zomatopy==1.0.10
zope.interface==4.6.0


Manner of running the Chatbot :-
1.Open an Annaconda prompt with administrator priviledges.
2.Move to the location where the action.py file and nlu_model.py file along with train_int.py and train_online.py is kept.
3.Enter into virtual environment created.
4.Run the nlu_model.py file for loading the domain file.
5.Run the chatbot through Dialog_Flow_management_model.py File.




