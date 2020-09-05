from flask import Flask
from flask import request,redirect

app = Flask(__name__)

user_ips =[]

try:
    with open('myzan.txt','r')as file:
        zan = int(file.read())
except Exception as e:
    with open('myzan.txt','w')as file:
        file.write('0')
        zan = '0'

@app.route('/')
def index():
    ip = request.remote_addr
    if ip in user_ips:
        Lobel = '''<span calss = "zan"> +'''+str(zan)+'''</span>'''
    else:
        Lobel = '''<button style="color:red"> +'''+str(zan)+'''</button>'''

    return '''
    <h1>今日话题 </h1>
    <div>
        <form action="/savezan" method="post">
            <span class="topic">《复仇者联盟》is good!</span>''' + Lobel +'''
        </form>
    </div>
    '''

@app.route("/savezan",methods=['POST'])
def savezan():
    global zan
    ip = request.remote_addr
    if ip in user_ips:
        return "BAD REQUEST!"
    else:
        user_ips.append(ip)#添加这个新ip到列表中
        zan = zan + 1
        with open('myzan.txt','w') as file:
            file.write(str(zan))
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",post=5000)
