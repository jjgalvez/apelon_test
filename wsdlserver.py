from flask import Flask
from flask import request, render_template, make_response

app = Flask(__name__)

@app.route('/soap/DtsQueryDaoWS')
def wsdl():
    if 'wsdl' in request.args:
        res = make_response(render_template('DtsQueryDaoWS_wsdl'))
    elif int(request.args.get('xsd', 0)) == 1:
        res = make_response(render_template('DtsQueryDaoWS_xsd1'))
    elif int(request.args.get('xsd', 0)) == 2:
        res = make_response(render_template('DtsQueryDaoWS_xsd2'))
    elif int(request.args.get('xsd', 0)) == 3:
        res = make_response(render_template('DtsQueryDaoWS_xsd3'))
    else:
        return ""

    res.headers['Content-Type'] = 'text/xml; charset=utf-8'
    return res


if __name__ == '__main__':
    app.run(port=5000, debug=True)
