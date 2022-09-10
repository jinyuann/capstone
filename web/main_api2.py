import json
from flask import Flask
from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/")
def home():
  return "<h1>ICT3102 rocks~</h1>"

@app.route("/sort", methods=['GET'])
def sort():
  if request.method == "GET":
    unsorted = (request.args.get("unsorted_list"))
    unsorted = unsorted.replace('[', '')
    unsorted = unsorted.replace(']', '')

    unsorted = list(unsorted.split(","))
    unsorted = [int(i) for i in unsorted]
    unsorted.sort()
    return (json.dumps(unsorted))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)