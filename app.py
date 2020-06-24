from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'OK!'

@app.route("/upload", methods=['POST'])
def handle_request():
    	# img = request.get_json()
    	# mongo.db.images.insert(dict(img))
    	# img = dict(img)
    	# with open("imageToSave.png", "wb") as fh:
    	#     fh.write(base64.b64decode(str(img["key"])))
	return "ok"

if __name__ == "__main__":
	app.run()

