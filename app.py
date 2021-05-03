from flask import Flask, render_template, request, jsonify
from neo_db.query_graph import query,get_KGQA_answer,get_answer_profile
from KGQA.ltp import get_target_array
## 第一部分：初始化：所有的Flask都必须创建程序实例，程序实例是Flask的对象，一般情况下使用如下方法实例化
app = Flask(__name__)  # Flask类只有一个必须指定的参数，即程序主模块或者包的名字，__name__是系统变量，该变量指的是本py文件的文件名

## 第二部分：路由和视图函数
# 客户端发送url给web服务器，web服务器将url转发给flask程序实例，程序实例需要知道对于每一个url请求启动的那一部分代码，所以保存了一个url和python函数的映射关系
# 处理url和函数之间关系的程序称为路由
# 在flask中，使用程序实例的app.route装饰器，把装饰的函数注册为路由
@app.route('/', methods=['GET', 'POST'])


@app.route('/index', methods=['GET', 'POST'])
def index(name=None):
    return render_template('index.html', name = name)  # render_template()是flask函数，它从模版文件夹templates中呈现给定的模板上下文。


@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')


@app.route('/KGQA', methods=['GET', 'POST'])  # 在点击“人物关系问答”之后加载问答界面
def KGQA():
    return render_template('KGQA.html')
@app.route('/get_profile',methods=['GET','POST'])
def get_profile():
    name = request.args.get('character_name')
    json_data = get_answer_profile(name)
    return jsonify(json_data)

@app.route('/KGQA_answer', methods=['GET', 'POST'])  # 人物关系问答系统：贾宝玉的奶奶的儿子是谁？
def KGQA_answer():
    question = request.args.get('name')
    json_data = get_KGQA_answer(get_target_array(str(question)))
    return jsonify(json_data)

@app.route('/search_name', methods=['GET', 'POST'])
def search_name():
    name = request.args.get('name')
    json_data=query(str(name))
    return jsonify(json_data)

@app.route('/get_all_relation', methods=['GET', 'POST'])
def get_all_relation():
    return render_template('all_relation.html')




## 第三部分：程序实例用run()方法启动flask集成开发的web服务器
# __name__ = '__main__'是python常用的方法，表示只有直接启动本脚本时，才使用app.run()方法
# 如果是其他脚本电泳本脚本，程序假定父级脚本会启用不同的服务器，因此不用执行app.run()
# 服务器启动后，会启动轮询，等待并处理请求。轮询会一直请求直到程序停止
if __name__ == '__main__':
    app.debug=True
    app.run()
