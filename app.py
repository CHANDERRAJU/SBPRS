#from cgitb import text
from operator import index
from flask import Flask,render_template,request
import model 
app = Flask('__name__')

valid_userid = ['00sab00','1234','zippy','zburt5','joshua','dorothy w','rebecca','walker557','samantha','raeanne','kimmie','cassie','moore222']
@app.route('/')
def index():
    #return render_template('index.html')
    recommended_products = ['p1','p2','p3','p4','p5']
    return render_template('index.html',recommended_products=recommended_products)

@app.route('/recommend',methods=['POST'])
def recommend_top5():
    print(request.method)
    user_name = request.form['user_name']
    print('User name=',user_name)
    
    if  user_name in valid_userid:
            top20_products = model.recommend_products(user_name)
           #print(top20_products.head())
            get_top5 = model.top5_products(top20_products)

            print(get_top5)
            recommended_products = get_top5['name'].to_list()
            print(recommended_products)
            return render_template('index.html',recommended_products=recommended_products)

            
    else:
        return render_template('index.html',text='No Recommendation found for the user')
   

if __name__ == '__main__':
    app.debug=True

    app.run()
