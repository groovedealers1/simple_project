from flask import Flask, render_template, request, redirect
from db.orm import insert_data, get_number, create_tables

app = Flask(__name__, template_folder='template')


@app.route("/", methods=['GET', 'POST'])
def application_for_recruitment():
    if request.method == 'POST':
        value = request.form['number']
        insert_data(value=value)
        return redirect('/')

    return render_template('home_page.html', value=get_number())


if __name__ == '__main__':
    create_tables()
    app.run(debug=True, host='0.0.0.0', port=5000)
