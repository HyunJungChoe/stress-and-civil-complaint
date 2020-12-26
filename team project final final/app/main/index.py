from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
import pickle
# 추가할 모듈이 있다면 추가

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
from numpy import linalg
 
main = Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=['POST','GET'])
def first():
      testData = 'testData array'
      #x= request.args.get('gun')
      #y=request.args.get('weather')
      #model = pickle.load(open('/pyclass/team project/gunsu.pkl', 'rb'))
      #result = model.predict([[int(x),int(y)]])
      #result = {'x' : x, 'y' : y }
      #return render_template('/main/index.html', result = result)
      return render_template('/main/index2.html', testDataHtml=testData)
 
@main.route('/index', methods=['POST','GET'])
def index():
      #testData = 'testData array'
      x= request.args.get('gun')
      y= request.args.get('weather')
      model = pickle.load(open('/pyclass/team project/gunsu.pkl', 'rb'))
      #result = {'x' : x, 'y' : y }
      #result = model.predict([[int(x),int(y)]])
      c = model.predict([[int(x),int(y)]])
      c = (', '.join(map(str,c)))
      multiply = c.replace('[','').replace(']','')

      return render_template('/main/index.html', result = multiply)

@main.route('/charts', methods=['GET'])
def chart():
      return render_template('/main/charts.html')

@main.route('/charts2', methods=['GET'])
def chart2():
      return render_template('/main/charts2.html')

@main.route('/charts3', methods=['GET'])
def chart3():
      return render_template('/main/charts3.html')

@main.route('/charts4', methods=['GET'])
def chart4():
      return render_template('/main/charts4.html')

@main.route('/charts5', methods=['GET'])
def chart5():
      return render_template('/main/charts5.html')

@main.route('/charts6', methods=['GET'])
def chart6():
      return render_template('/main/charts6.html')
      
@main.route('/blank', methods=['GET'])
def blank():
      return render_template('/main/blank.html')