from flask import Flask,jsonify,request

app = Flask(__name__)

contacts=[
    {
      "Contact":"9487281699",
      "Name":"radha",
      "done":False,
      "id":1
    },
    {
      "Contact":"9487281699",
      "Name":"radha",
      "done":False,
      "id":1
    }
]

@app.route('/')
def main():
    return "this is my project 124"

@app.route('/add-data',methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'provide the data'
        },400)

    contact={
        "Contact":request.json.get('Contact',""),
        "Name":request.json['Name'],
        "done":False,
        "id":contacts[-1]['id']+1
    }

    contacts.append(contact)

    return jsonify({
        'status':'successful',
        'message':'data added successfully'
    })

@app.route('/get-data')
def get_data():
    return jsonify({
        'data':contacts
    })


if(__name__=="__main__"):
    app.run(debug=True)