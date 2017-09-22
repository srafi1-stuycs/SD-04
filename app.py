#Shakil Rafi
#SoftDev1 pd7
#HW04 -- Fill up yer flask
#2017-09-22

from flask import Flask
app = Flask(__name__)

def link_to(num):
    link = str(num)
    return '<a href="/%s"> Go to %s</a>' % (link, link)

def gen_page_for(num):
    page = ''
    for i in range(1, 4):
        if i == num:
            continue
        page += link_to(i) + ' '
    return page

@app.route('/')
@app.route('/1')
def page1():
    return gen_page_for(1)
    
@app.route('/2')
def page2():
    return gen_page_for(2)
    
@app.route('/3')
def page3():
    return gen_page_for(3)
    
if __name__ == '__main__':
    app.run(debug=True)
