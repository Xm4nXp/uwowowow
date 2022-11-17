from flask import Flask,render_template,request,url_for
import requests,random,string,time,os
from selectorlib import Extractor
app = Flask(__name__)

list_apikey = ['manz']
@app.route('/')
def favicon():
    return render_template('404-1.html')
@app.route('/ip/<ipad>')
def get_ip(ipad):
    try:
        ab = request.args['apikey']
        resul = f'{ab} and API {ipad}'
        if ab in list_apikey:
          ac = private().main_url(ipad)
          return ac
        else:
            return render_template('404-1.html')
    except:
        return render_template('404.html')
class private():
    def __init__(self):
        self.oke = []
        self.url = 'https://www.pagesinventory.com/ip/{ips}-{next}.html'
        self.hd = ''
    def main_url(self,param):
        getting = requests.Session()
        ab = Extractor.from_yaml_file('a.yaml')
        for i in range(20):
            get2 = getting.get(self.url.format(ips=param,next=f'{i}'))
            res = ab.extract(get2.text)
            if res['x'] == None:
                break
            else:
                for i in range(len(res['x'])):
                    uwo = res['x']
                    self.oke.append(uwo[i])
        return self.oke
@app.route('/check')
def generate():
    try:
        ab = request.args['cek']
        if ab in list_apikey:
            return data_json(ab)
        else:
            return data_json(ab)
    except:
        return render_template('404-1.html')

def data_json(nama):
    if nama == list_apikey[0]:
        dicts = {
            'nama':'manzx',
            'Create':'17-11-2022',
            'count':'UNLIMITED'

        }
    else:
        dicts = {
            'nama':'-',
            'Create':'KIAMAT',
            'count':'GAK ADA BLOK !'

        }
    return dicts

def generate2():
    letters = string.ascii_uppercase
    result_str = ''.join((random.choice('ABCDOOWK1234847') for i in range(5)))
    result_str2 = ''.join((random.choice('ABCDOOWQOWJK1234847') for i in range(5)))
    result_str3 = ''.join((random.choice('ABCDOOWK12348JOFB447') for i in range(5)))
    kk = 'Xm4nXp'
    return result_str,result_str2,result_str3,kk
if __name__ == '__main__':
    app.run(threaded=True, port=5000)