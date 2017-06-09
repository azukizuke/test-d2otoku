def addCounterKey(argdict,key):
	if key in argdict:
		argdict[key]+=1
	else:
		argdict[key]=1

	return argdict

def addCounterPlayerName(argdict,key):
	if key in argdict:
		argdict[key]+=1
	else:
		argdict[key]=1

	return argdict
