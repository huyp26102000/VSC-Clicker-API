from package import *
from function import *
import ast
app = Flask("Google Login App")


@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		if request.form['submit_button'] == 'login':
			return redirect(url_for('login'))
	else: return render_template('login.html')

@app.route('/demo', methods=['GET', 'POST'])
def demo():
    data = request.data
    uuid = ast.literal_eval(data.decode("UTF-8"))['uuid']
    stdID = getStudentIDbyUUID(uuid)
    return stdID

if __name__ == "__main__":
    app.run(debug=True)
