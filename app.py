import flask
import random
from flask import request, jsonify, render_template, make_response
import os

file = os.path.join('home', 'athena', 'img')

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["UPLOAD_FOLDER"] = file

app.route('/', methods=["GET"])
def home():
	return """
	<body style=\"background-color:#36393f\">
	<h1>tbh right now I'm not sure what I'm going to do for here</h1>
	<br><p>hah ily soni</p>
	</body>
	"""

ist = '''
hmm not sure how I'm going to do this tbh
'''

mt = '''
<body style=\"background-color:#36393f\">
<style> 
	h1 {text-align: center}
	h3 {text-align: center}
	form {text-align: center}
	label {color: white}
</style>
<title>Send a message to the author of this API pack</title>
<h1 style=\"color:white\">Send a message to the author of the API pack</h1>
<form action=\"/msg/sub\">
	<label for=\"m\">Message:</label><br>
	<input type=\"text\" id=\"m\" name=\"m\">
	</input>
	<input type=\"Submit\" value=\"Submit\">
</form>
<h3 style=\"color:white\">
'''


stuff = '''<body style=\"background-color:#36393f\">
<style>
	h1 {text-align: center}
	h3 {text-align: center}
	form {text-align: center}
</style>
<title>
	Random number generator
</title>
<h1 style=\"color:white\">Your random number is:</h1>
<h3 style=\"color:white\">
'''##############

sn = '''
<form>
	<input type=\"button\" id=\"r\" name=\"r\" value=\"Redirect back\">
</form>
<script>
	document.getElementById('r').onclick = function() {
		window.location.replace('/rng')
	};
</script>
'''

se = '''<body style=\"background-color:#36393f\">
<style>
	h1 {text-align: center}
	h3 {text-align: center}
    form {text-align: center}
</style>
<title>
	Random number generator
</title>
<h1 style=\"color:white\">Error:</h1>
<br><h3 style=\"color:white\">
'''##############

######################################################
#####          random num generator       ############
######################################################

@app.route('/rng', methods=["GET"])
def rng():
	return '''
	<body style=\"background-color:#36393f\">
	<title>
		Random number generator
	</title>
	<style>
		h1 {color: white}
		h1 {text-align: center}
		p {color: white}
		p {text-align: center}
		form {text-align: center}
		label {color: white}
	</style>
	<h1>Input numbers for the random number generator</h1>
	<p>This generates a random number between the first input, and the second input</p><br><br><br>
	<form action=\"/rng/proc\"> 
		<label for=\"f\">First input:</label><br>
		<input type=\"text\" id=\"inp1\" name=\"inp1\"></input>
		<br><br>
		<label for=\"s\">Second input:</label><br>
		<input type=\"text\" id=\"inp2\" name=\"inp2\"><br>
		<input type=\"Submit\" value=\"Submit\"><br><br><br>
	</form>
	'''

@app.route('/rng/proc', methods=["GET"])
def rngproc():#stands for random number generator
	try:#try/except in the case there's a valueerror, which that means one of the request.args is a str or some crap
		inp1 = int(request.args['inp1'])
		inp2 = int(request.args['inp2'])
		if inp1 == 69 or inp2 == 69 or inp1 == 420 or inp2 == 420:#me being stupid
			return stuff +  f'hehe, funny number<br><br>{random.randint(inp1, inp2)}</h3><br><br><br>' + sn
		else:#actual serious code returning the random number
			return stuff + f'<br><br><br>{random.randint(inp1, inp2)}</h3><br><br><br>' + sn #oh god here we go with this crap
	except ValueError:#in the case that there's a valueerror this'll run
#		return 'testy'
		if not isinstance(request.args["inp1"], int):#inside these if-elses (making sure which one is wrong)
			return se + f'Expected int, got something else. Please make sure to correct your request arguments.</h3><br><br><br>' + sn
		elif not isinstance(request.args["inp2"], int):
			return se + f'Expected int, got something else. Please make sure to correct your request arguments.</h3><br><br><br>' + sn
		else:
			return se + 'Sorry! We couldn\'t parse your request, make sure both of your request arguments are numbers.<h3><br><br><br>' + sn
			#^^^fallback case

######################################################
############     ripoff doggo.ninja    ###############
######################################################

@app.route('/img', methods=["GET", "POST"])
def img():
	if 'k' in request.args:
		filename = os.path.join(app.config["UPLOAD_FOLDER"], 'image.png')
		return render_template('img.html', img = filename)
	else:
		return 'well you surely are dumb aren\'t you' 

#####################################################
###########    some stupid shit #####################
#####################################################

@app.route('/msg', methods=["GET"])
def msg():
	return mt + '<br><br><br><br>Please remember all messages/suggestions will be seen by the creator of this API<h3>'

@app.route('/msg/sub', methods=["GET"])
def msgsub():
	if 'm' in request.args:
		print(request.args["m"])
		with open('/home/athena/dev/python/soni/msg.txt', 'a') as f:
			#f.write(f"<br><br>{request.args['m']}")
			f.write("soni is great")
		return '''
		<body style=\"background-color:#36393f\">
		<meta http-equiv="Refresh" content="5; url='/msg'">
		<style>
			h1 {color: white}
			h1 {text-align: center}
			p {color: white}
			p {text-align: center}
		</style>
		<h1>Message recorded!</h1><br><br>
		<p>Zapping you back in 5...</p>
		'''
	else:
		return '''
		<body style=\"background-color:#36393f\">
		<style>
			h1 {color: white}
			h1 {text-align: center}
		</style>
		<h1>No request arguments. Please retry.</h1>
		'''

#####################################################
############# psuedo-bank ###########################
#####################################################

@app.route('/pb/li', methods=["GET"])
def pseudo_bank_login():
	return '''
	<style>
		form {text-align: center}
	</style>

	<form action="/pb/pr" method="POST>
		<div class="container">
			<label for="Name">Name:</label>
			<br>
			<input type="text" id="Name">
			<br><br><br>
			<label for="Email">Email</label>
			<br>
			<input type="text" id="Email"><br>
			<input type="submit" value="Submit.">
		</div>
	</form>
	'''

@app.route('/pb/pr', methods=["GET"])
def cookie():
	if request.method == "POST":
		user = request.form["Name"]
		rc = '''
		
		'''


if __name__ == "__main__":
	app.run(host="0.0.0.0", port="8080")
else: 
	pass
