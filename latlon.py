from flask import Flask, request
import csv

app = Flask(__name__)


@app.route('/loginn',methods = ['POST', 'GET'])
def loginn():
	if request.method == 'POST':
		lat = request.form['fname']
		lon = request.form['lname']
		
		with open('/root/Desktop/persons.csv', 'wb') as csvfile:
		    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		    filewriter.writerow([lat,lon])	

		return "latitude = "+ lat + "longitude = "+ lon
		

#def login():
#  if request.method == 'POST':
#    user = request.form['nm']


if __name__ == '__main__':
	app.run(debug = True)
