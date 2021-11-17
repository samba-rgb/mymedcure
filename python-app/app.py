from flask import Flask
import json
import matplotlib
matplotlib.use('Agg')
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from flask import Flask, send_from_directory

import urllib
import pyrebase
# import request
from flask import request
app = Flask(__name__)
newrc = {'figure.figsize': (12.0, 15.0),
         'figure.facecolor': (1, 1, 1, 0),
         'figure.edgecolor': (1, 1, 1, 0),
         'font.size': 10,
         'figure.dpi': 72,
         'figure.subplot.bottom': 0.325}

import matplotlib.pyplot as plt
plt.rcParams.update(newrc)

@app.route("/")
def showHomePage1():
    return 

@app.route("/samba")
def showHomePage():
    return """
    <!DOCTYPE html>

<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title></title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<body>
    <form action="/post-smth" method="POST" enctype="multipart/form-data">
        <div>
            <label for="csvfile1">Upload Your File1 Here: </label>
            <input type="file" id="csvfile1" name = "csvfile1">
        </div>
        <br>
        <div>
            <label for="csvfile2"> Upload Your File2 Here: </label>
            <input type="file" id="csvfile2" name = "csvfile2">
        </div>

        <script src="" async defer></script>
        <br>
        <button> Submit</button>
    </form>

</body>

</html>
    """

@app.route("/post-smth",methods = ["POST"])
def sam():
    file1 = request.files['csvfile1']
    file2= request.files['csvfile2']
    if not os.path.isdir('static'):
        os.mkdir('static')
    filepath = os.path.join('static',"test.csv")
    filepath2 = os.path.join('static','complete.csv')
    file1.save(filepath)
    file2.save(filepath2)
    tab = pd.read_csv('static/test.csv')
    total = pd.read_csv('static/complete.csv')
    def tablet_date(date):
        return k[date[-4:-1]]
    k = {'Mon':'monday','Tue':'tuesday','Wed':'wednessday','Thu':'thursday','Fri':'friday','Sat':'saturday','Sun':'sunday'}
    tab['tablet_date'] = tab['tablet_date'].apply(tablet_date)
    result = total.to_json(orient="records")
    items = json.loads(result)
    df = tab
    df['morning_actual'] = 0
    df['afternoon_actual'] = 0
    df['evening_actual'] = 0
    df['night_actual'] = 0

    def search_morning(name,day):
        for keyval in items:
            if name.lower() == keyval['sname'].lower():

                return keyval[day+ '_morning']
    def search_afternoon(name,day):
        for keyval in items:
            if name.lower() == keyval['sname'].lower():

                return keyval[day+ '_afternoon']
    def search_evening(name,day):
        for keyval in items:
            if name.lower() == keyval['sname'].lower():

                return keyval[day+ '_evening']
    def search_night(name,day):
        for keyval in items:
            if name.lower() == keyval['sname'].lower():

                return keyval[day+ '_night']
    for i in range(len(df)) :
        name = df.loc[i,'tablet_name']
        day = df.loc[i,'tablet_date']
        df.loc[i,'morning_actual'] = search_morning(name,day)
        df.loc[i,'afternoon_actual'] = search_afternoon(name,day)
        df.loc[i,'evening_actual'] = search_evening(name,day)
        df.loc[i,'night_actual'] = search_night(name,day)
    df["morning"] = df["morning"].astype(str).astype(int)
    df["afternoon"] = df["afternoon"].astype(str).astype(int)
    df["evening"] = df["evening"].astype(str).astype(int)
    df["night"] = df["night"].astype(str).astype(int)
    df["morning_actual"] = df["morning_actual"].astype(float).astype(int)
    df["afternoon_actual"] = df["afternoon_actual"].astype(float).astype(int)
    df["evening_actual"] = df["evening_actual"].astype(float).astype(int)
    df["night_actual"] = df["night_actual"].astype(float).astype(int)
    tab_name = list(df['tablet_name'].unique())
    plotting2(tab_name,df)
    return send_from_directory('./static/' , 'multipage.pdf')








@app.route("/outbug",methods = ["POST"])
def outbug():
    k = {'Mon':'monday','Tue':'tuesday','Wed':'wednessday','Thu':'thursday','Fri':'friday','Sat':'saturday','Sun':'sunday'}
    text = request.form["tablet"]
    pattern = request.form["pattern"]
    print(text)

    final_dictionary = eval(text)
    l = final_dictionary['CONTACTDETAILS']
    patt_dic = eval(pattern)
    items = patt_dic['CONTACTDETAILS']
    print(items)
    df = pd.DataFrame(columns=['ID','NAME', 'DATE', 'morning', 'afternoon',
       'evening', 'night'])
    for i in range(0,len(l)):
        df = df.append(l[i], ignore_index = True)
    def tablet_date(date):
        return k[date[-4:-1]]
    df['DATE'] = df['DATE'].apply(tablet_date)
    df['morning_actual'] = 0
    df['afternoon_actual'] = 0
    df['evening_actual'] = 0
    df['night_actual'] = 0
    
    def search_morning(name,day):
        for keyval in items:
            if name.lower() == keyval['NAME'].lower():
                
                return keyval[day+ '_morning']
    def search_afternoon(name,day):
        for keyval in items:
            if name.lower() == keyval['NAME'].lower():
                
                return keyval[day+ '_afternoon']
    def search_evening(name,day):
        for keyval in items:
            if name.lower() == keyval['NAME'].lower():
                
                return keyval[day+ '_evening']
    def search_night(name,day):
        for keyval in items:
            if name.lower() == keyval['NAME'].lower():
                
                return keyval[day+ '_night']
        
    for i in range(len(df)) :
        name = df.loc[i,'NAME']
        day = df.loc[i,'DATE']
        df.loc[i,'morning_actual'] = search_morning(name,day)
        df.loc[i,'afternoon_actual'] = search_afternoon(name,day)
        df.loc[i,'evening_actual'] = search_evening(name,day)
        df.loc[i,'night_actual'] = search_night(name,day)
    df["morning"] = df["morning"].astype(str).astype(int)
    df["afternoon"] = df["afternoon"].astype(str).astype(int)
    df["evening"] = df["evening"].astype(str).astype(int)
    df["night"] = df["night"].astype(str).astype(int)
    df["morning_actual"] = df["morning_actual"].astype(str).astype(int)
    df["afternoon_actual"] = df["afternoon_actual"].astype(str).astype(int)
    df["evening_actual"] = df["evening_actual"].astype(str).astype(int)
    df["night_actual"] = df["night_actual"].astype(str).astype(int)
    
    cor = df.corr(method ='kendall')
    day = ['morning','afternoon','evening','night']
    a= 0
    for i in day:
        a  += cor[i][i + '_actual']*100
    
    try:
        ting = str(int(a//4))
    except:
        ting = "0"
    return ting

@app.route("/debug", methods=["POST"])
def debug():
    k = {'Mon':'monday','Tue':'tuesday','Wed':'wednessday','Thu':'thursday','Fri':'friday','Sat':'saturday','Sun':'sunday'}
    text = request.form["tablet"]
    pattern = request.form["pattern"]
    print(text)

    final_dictionary = eval(text)
    l = final_dictionary['CONTACTDETAILS']
    patt_dic = eval(pattern)
    items = patt_dic['CONTACTDETAILS']
    df = pd.DataFrame(columns=['ID','NAME', 'DATE', 'morning', 'afternoon',
       'evening', 'night'])
    for i in range(0,len(l)):
        df = df.append(l[i], ignore_index = True)
    def tablet_date(date):
        return k[date[-4:-1]]
    df['DATE'] = df['DATE'].apply(tablet_date)
    df['morning_actual'] = 0
    df['afternoon_actual'] = 0
    df['evening_actual'] = 0
    df['night_actual'] = 0
    
    def search_morning(name,day):
        for keyval in items:
            if name.lower() == keyval['NAME'].lower():
                
                return keyval[day+ '_morning']
    def search_afternoon(name,day):
        for keyval in items:
            if name.lower() == keyval['NAME'].lower():
                
                return keyval[day+ '_afternoon']
    def search_evening(name,day):
        for keyval in items:
            if name.lower() == keyval['NAME'].lower():
                
                return keyval[day+ '_evening']
    def search_night(name,day):
        for keyval in items:
            if name.lower() == keyval['NAME'].lower():
                
                return keyval[day+ '_night']
        
    for i in range(len(df)) :
        name = df.loc[i,'NAME']
        day = df.loc[i,'DATE']
        df.loc[i,'morning_actual'] = search_morning(name,day)
        df.loc[i,'afternoon_actual'] = search_afternoon(name,day)
        df.loc[i,'evening_actual'] = search_evening(name,day)
        df.loc[i,'night_actual'] = search_night(name,day)
    df["morning"] = df["morning"].astype(str).astype(int)
    df["afternoon"] = df["afternoon"].astype(str).astype(int)
    df["evening"] = df["evening"].astype(str).astype(int)
    df["night"] = df["night"].astype(str).astype(int)
    df["morning_actual"] = df["morning_actual"].astype(str).astype(int)
    df["afternoon_actual"] = df["afternoon_actual"].astype(str).astype(int)
    df["evening_actual"] = df["evening_actual"].astype(str).astype(int)
    df["night_actual"] = df["night_actual"].astype(str).astype(int)
    
    tab_name = list(df['NAME'].unique())
    plotting(tab_name,df)

    path = uploadfirebase()
    print(path)
    
    return path
     
def plotting(tab_name,df):
    mock = {
    'name' : 'k',
    'your_medication' : 1,
    'actual_medication' : 0
    }
    pp = PdfPages('multipage.pdf')
    day_time = ['morning','afternoon','evening','night']
    df1 = pd.DataFrame(columns=['name','your_medication', 'actual_medication'])
    for j in tab_name:
        df3 =  df[df.NAME==j]
        for i in day_time:
            temp= df3
            temp_exp = temp[i].sum()
            temp_real = temp[i+'_actual'].sum()
            df2 = {'name': i, 'your_medication': temp_exp, 'actual_medication': temp_real}
            df1 = df1.append(df2, ignore_index = True)
        


        ax = df1.plot(x="name", y="actual_medication", kind="bar")
        # plotting age on the same axis
        df1.plot(x="name", y="your_medication", kind="bar", ax=ax, color="maroon")
        
        plt.title(j)
        plt.savefig(pp, format='pdf',bbox_inches='tight')
        df1 = pd.DataFrame(columns=['name','your_medication', 'actual_medication'])

    pp.close()
    
    return df1 
def plotting2(tab_name,df):
    mock = {
    'name' : 'k',
    'your_medication' : 1,
    'actual_medication' : 0
    }
    pp = PdfPages('./static/multipage.pdf')
    day_time = ['morning','afternoon','evening','night']
    df1 = pd.DataFrame(columns=['name','your_medication', 'actual_medication'])
    for j in tab_name:
        df3 =  df[df.tablet_name==j]
        for i in day_time:
            temp= df3
            temp_exp = temp[i].sum()
            temp_real = temp[i+'_actual'].sum()
            df2 = {'name': i, 'your_medication': temp_exp, 'actual_medication': temp_real}
            df1 = df1.append(df2, ignore_index = True)
        


        ax = df1.plot(x="name", y="actual_medication", kind="bar")
        # plotting age on the same axis
        df1.plot(x="name", y="your_medication", kind="bar", ax=ax, color="maroon")
        
        plt.title(j)
        plt.savefig(pp, format='pdf',bbox_inches='tight')
        df1 = pd.DataFrame(columns=['name','your_medication', 'actual_medication'])

    pp.close()
    
    return df1 

def uploadfirebase():
    firebaseConfig={"apiKey": "AIzaSyA7UG0BvkKydcUny8LJehQwvW76ea9C_xI",
    "authDomain": "my-medicure.firebaseapp.com",
    "databaseURL":"https://my-medicure-default-rtdb.firebaseio.com",
    "projectId":  "my-medicure",
    "storageBucket": "my-medicure.appspot.com",
    "messagingSenderId": "579161691477",
    "appId": "1:579161691477:web:f55d2612a24fb8433a0bdc",
    "measurementId":  "G-SYHE33YY03"}

    firebase=pyrebase.initialize_app(firebaseConfig)
    storage=firebase.storage()
    from datetime import datetime
    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    file='multipage.pdf'
    cloudfilename= 'pdf_' + date + '.pdf'
    storage.child(cloudfilename).put(file)
   # print(storage.child(cloudfilename).get_url(None))
    path=storage.child(cloudfilename).get_url(None)
    return path

if __name__ == "__main__":
  app.run(host="192.168.149.90")