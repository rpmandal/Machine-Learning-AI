from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-793688093472-780908249922-795906404374-ff18d8982c087f826935a9e6833f8ff3', #app verification token
							'xoxb-793688093472-793703104645-7aOsO08P1kffVckUFOrimvwG', # bot verification token
							'0vxg06gitFzxPsedUcUDuaib', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
