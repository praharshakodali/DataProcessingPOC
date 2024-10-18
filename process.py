from flask import Flask,request,render_template
import os
import pandas as pd
import gridfs
from pymongo import MongoClient
from werkzeug.datastructures import FileStorage
app = Flask(__name__,template_folder='./template')

try:
    client=MongoClient('mongodb+srv://praharsha4123:sweety4123@cluster0.l1brd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
except:
    print('Error connecting to mongodb cluster!')

@app.route('/',methods=['POST','GET'])
def home():
    return render_template('home.html')

@app.route('/process_data',methods=['POST','GET'])
def process_data():
    if request and request.files:
        file=request.files['file']
        if file.filename:
            filename=file.filename
            file_ext = os.path.splitext(filename)[1]
            if file_ext !='.csv':
                return render_template('home.html',message="please upload csv file only!")
            #file processing logic
            database=client['users']
            collection_customers=database['customers']
            collection_representatives=database['representatives']
            data=pd.read_csv(file)
            for row in range(data.shape[0]):
                if 'CR' in data.iloc[row]['ID']:
                    collection_customers.insert_one(data.iloc[row].to_dict())
                if 'RP' in data.iloc[row]['ID']:
                    collection_representatives.insert_one(data.iloc[row].to_dict())
            return render_template('home.html',message="processed "+filename+" file successfully!")
        return render_template('home.html',message="please upload file with valid name!")
    return render_template('home.html',message="please upload a file to process!")

if __name__ == '__main__':
    app.run()
