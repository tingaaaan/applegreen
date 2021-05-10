#$env:FLASK_APP="app.py" 執行flask
from flask import Flask , request,abort,session;
from flask import render_template,make_response;
from flask import redirect,url_for;
import numpy as np;
import cv2;
from werkzeug.utils import secure_filename;
import os;
import time;



app = Flask(__name__,static_folder="media")
@app.route('/',methods =['post','get']) 
def index(): 
	if request.method =='POST':
		if request.values['send']=='送出':
			return render_template('index.html',name=request.values['user'])
	return render_template('index.html',name="")


@app.route('/全部商品.html',methods =['post','get']) 
def items(): 
	return render_template('全部商品.html')

@app.route('/門市資訊.html',methods =['post','get']) 
def retail(): 
	return render_template('門市資訊.html')

@app.route('/企業責任.html',methods =['post','get']) 
def duty(): 
	return render_template('企業責任.html')

@app.route('/品牌故事.html',methods =['post','get']) 
def story(): 
	return render_template('品牌故事.html')

@app.route('/加入我們.html',methods =['post','get']) 
def join(): 
	return render_template('加入我們.html')

@app.route('/客服專區.html',methods =['post','get']) 
def service(): 
	return render_template('客服專區.html')