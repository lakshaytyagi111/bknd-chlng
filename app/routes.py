from flask import Blueprint, request, render_template, jsonify

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET'])
def index():
    error = ''
    return render_template('home.html', error=error)

@routes.route('/check-prime', methods=['GET'])
def check_prime():
    try: 
        number = request.args.get('number')
        number = int(number)
        if number is None:
            return jasonify({'error': 'An Integer parameter should be passed.'}), 400
        if (number%2==0):
            result = 'Even'
            return jsonify({'number':number, 'result':result}), 200
        else:
            result = 'Odd'
            return jsonify({'number':number, 'result':result}), 200
    except Exception as error:
        return render_template('home.html', error=error), 500



