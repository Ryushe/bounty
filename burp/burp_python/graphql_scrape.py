# go to site w/ graphql
# optional - filter to only be the domain you want -> not going to include in script

import json
from burp import IBurpExtender
from pyscripterer import BaseScript as Script
args = [extender, callbacks, helpers, toolFlag, messageIsRequest, messageInfo, macroItems]
script = Script(*args)

if messageIsRequest:
	reqbytes = messageInfo.getRequest()
	req = helpers.analyzeRequest(reqbytes)
	headers = req.getHeaders()
	parameters = reqbytes[(req.getBodyOffset()):].decode("utf-8)
	clean_perams = perameters.strip("\n")


try:
	parameters_dict = json.loads(parameters)
 		print("Extracted Dictionary:", parameters_dict)
except json.JSONDecodeError as e:
	print("Failed to decode JSON:", e)