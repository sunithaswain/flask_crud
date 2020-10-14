import logging
logging.basicConfig(level=logging.WARNING)
import pandas as pd
from pandas import DataFrame
from flask import jsonify
import ast,bson
from flask import Flask, jsonify, request,json,redirect
from flask import Flask, request, render_template,url_for
from flask import Blueprint, render_template, redirect, url_for, request, flash
#from flask.ext.login import login_user
from bson.objectid import ObjectId
from flask import request
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

#############addede######
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
from itertools import islice
#client = MongoClient('mongodb://localhost:27017')
db = client.admin
#db = client['admin']
mycol = db["customers"]
@app.route("/", methods=['GET','POST'])
def home_user():
    logging.debug("user details")
    return render_template("base.html")
@app.route("/table", methods=['GET','POST'])
def table():
    data=""
    ##getting the data from the postman and creating
    requestdata=request.args
    #print (requestdata,"eeee")
    dic=dict()
    #dic["age"]=requestdata.get("age")
    #dic["test"]=requestdata.get("test")
    #print(dic,"[[[[[[[[[[[[[")
    records_updated=mycol.find({})
    #print ("hellonew")
    #print (records_updated)
    addlist=list()
    for obj in records_updated:
        #print (obj["age"])
        addlist.append(obj)
    #print (addlist)
    logging.debug(addlist)
    return render_template("table.html",data=addlist,message="success")
@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    logging.debug("test data")
    return render_template('add_displaying.html')
@app.route('/reback_data/<e_id>/', methods=['GET', 'POST'])
def reback_data(e_id):
    #print (e_id,"iiii")
    alldata=[]
    records_updated = mycol.find({"_id":ObjectId(e_id)})
    print (records_updated)
    for e in records_updated:
        age=(e["Age"])
        id=(e["_id"])
        #technology=(e["Technology"])
        #desgination = (e["Desgination"])
        alldata.append(e)
        logging.debug(alldata)
    return render_template('edit_displaying.html',agedata = age,iddetials=id)

@app.route('/fetching',methods=['GET', 'POST'])
def fetching():
    data=""
    #print("testdata")
    if request.method=="POST":
        print(request.form,"fffff")
        iddata=request.form.get("id")
        agedata = request.form.get("age")
        Technologydata=request.form.get("technology")
        desginationdata=request.form.get("desgination")
        customerinsertdata = db["customers"]
        customerinsertdata.insert({"id":iddata,'Age':agedata,'Technology':Technologydata,'Desgination':desginationdata})
        return redirect("/table")
    else:
        return "test data"
@app.route("/replacingdata",methods=['GET','POST'])
def replacingdata():
    if request.method=="POST":
        #print ("coming")
        iddata=request.form.get("id")
        agedata = request.form.get("age")
        #print (iddata,agedata,"rrrrrrrrr")
        newlist=db["customers"]
        newlist.update_one({"_id":ObjectId(iddata)},{"$set":{"Age":agedata}})
        #print (type(newlist))
        return redirect("/table")
    else:
        #print("it is not editing")
        return "it is not editing"
@app.route("/delete", methods=['GET','POST'])
def delete():
    if request.method == "POST":
        fetcheddata=request.form
        id=[]
        age=[]
        tech=[]
        finallist = []
        #length_to_split = [4, 4]
        sendlist=list()
        for dat in fetcheddata:
            newli = list()
            stpdata= dat.split("  ")
            stpdata=[ x.strip() for x in stpdata]
            #print (type(stpdata))
            for e in stpdata:
                if "\n" in e:
                    n1=e.split("\n")
                    #print (n1)
                    finallist.extend(n1)
                else:
                    finallist.append(e)
        #print (finallist,"LLLLLLLLL")
        final=int(len(finallist)/4)
        #print (final,"fffff")
        length_to_split=[4 for x in range(final)]
        #print (length_to_split,"ppppppppppppp")
        finalli=iter(finallist)
        Output = [list(islice(finalli, elem)) for elem in length_to_split]
        print(Output,"{{{{{{{{{{{{{{{{{{{{{{{{")
        frstdata=Output[0]
        frstdata=frstdata[0]
        #print (frstdata,"fffff")
        seconddata=Output[1]
        seconddata=seconddata[0]
        #print (seconddata,"sssss")
        sendlist.append(frstdata)
        sendlist.append(seconddata)
        thirddata=Output[2]
        thirddata=thirddata[0]
        sendlist.append(thirddata)
        #print (thirddata,"[[[")
        print (sendlist)
        newlist = db["customers"]
        newlist.delete_many({"_id":ObjectId(frstdata)})
        newlist.delete_many({"_id":ObjectId(seconddata)})
        newlist.delete_many({"_id": ObjectId(thirddata)})
        print ("records deleted")
        return redirect("/table")

    else:
        print ("not valid")
    return redirect("/table")
@app.route("/signupdata",methods=['GET','POST'])
def signupdata():
    message=""
    print("login")
    if request.method == "POST":
        print("hello")
        firstdata = request.form.get("firstname")
        lastdata= request.form.get("lastname")
        emaildata = request.form.get("email")
        passworddata = request.form.get("password")
        print(firstdata,lastdata,emaildata, passworddata,"SSSSSS")
        if emaildata:
            try:
                print (emaildata,"ppppppp")
                newlist = db["customers"]
                test = newlist.find({"email": emaildata})
                for ea in test:
                    print(ea,"[[[[")
                    try:
                        if ea:
                            message="user already exist"
                            print (message,"mmmmmmmmmm")
                            return render_template('page-register.html',mess=message)
                        else:
                            print ("middle")
                            newlist = db["customers"]
                            newlist.insert_many(
                                {"firstname": firstdata, "lastname": lastdata, "email": emaildata, "password": passworddata})
                        return render_template('login_page.html')
                    except:
                        return render_template('page-register.html', mess=message)
            except:
                newlist = db["customers"]
                newlist.insert_many(
                    {"firstname": firstdata, "lastname": lastdata, "email": emaildata, "password": passworddata})
            return render_template('login_page.html')

        else:
            print("ending")
            newlist = db["customers"]
            newlist.insert_many(
                {"firstname": firstdata, "lastname": lastdata, "email": emaildata, "password": passworddata})
            return render_template('login_page.html')
    else:
        print ("not valid")
    return render_template('page-register.html')

@app.route("/logindata",methods=['GET','POST'])
def logindata():
    message=""
    print("login")
    if request.method == "POST":
        print ("not valid posts")
        emaildata = request.form.get("email")
        password = request.form.get("password")
        print (emaildata,password,"ppppppppp")
        try:
            if emaildata and password:
                newlist = db["customers"]
                chnewlist = newlist.find({"email": emaildata, "password": password})
                for eac in chnewlist:
                    print (eac,"eeee")
                    if eac:
                        print ("correct details")
                        return render_template('table.html')
                    else:
                        return render_template('login_page.html')
        except:
            print ("details exist")
            return render_template('login_page.html')
        else:
            print ("username and password is wrong")
            return render_template('login_page.html')

    else:
        print ("not statement")
        return render_template('login_page.html')
@app.route("/alldb_data",methods=['GET','POST'])
def alldb_data():
    chnewlist=""
    print("login")
    if request.method == "POST":
        emaildata = request.form.get("email")
        password = request.form.get("password")
        frstname=request.form.get("firstname")
        lastname=request.form.get("lastname")
        print (emaildata,password,frstname,lastname)
        newlist = db["customers"]
        chnewlist = newlist.find({"email": emaildata, "password": password,"firstname":frstname,"lastname":lastname})
        print (chnewlist,"pppp")
    return chnewlist
@app.route("/convet_excel",methods=['GET','POST'])
def convet_excel():
    fidata=list()
    secdata=list()
    src="F:/pandas/excel/annual-enterprise-survey-2018-financial-year-provisional-csv - Copy.csv"
    src1="F:/pandas/excel/annual-enterprise-survey-2018-financial-year2-csv.csv"
    read=pd.read_csv(src,nrows=3)
    df=DataFrame(read)
    products_list = df.values.tolist()
    file=open("F:/pandas/excel/table.html","w")
    file.write("<html>")
    file.write("<head>")
    file.write("<title>")
    file.write("Displaying table format")
    file.write("</title>")
    file.write("</head>")
    file.write("<body>")
    file.write('<center><table border="5" width = 1200>')
    file.write("<table border=10>")
    for ea in products_list:
        for e in ea:
            try:
                if type(e)=="int":
                    print (e,"pppp")
            except:
                pass
            file.write('<tr><th><td><b><font color="blue">' + e+ '</font></td></th></tr>')
    file.write("<tr></tr>")
    file.write("</table>")
    file.write("</body>")
    file.write("</html>")
    file.close
    return "test cases"

if __name__ == '__main__':
    app.run(port="5002", debug=True)