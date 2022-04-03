from flask import Flask, render_template, request, redirect, url_for, flash, jsonify


app = Flask(__name__)

#settings
app.secret_key = 'mysecretkey'
@app.route('/')
def index():
    contacts = (('1', 'Juan', '12345678', '@mail.com'),)
    # contacts = ({'id': '1', 'name': 'John', 'phone': '123', 'email': 'john@example.com'}, ) tambien se puede con diccionarios
    


    return render_template('index.html', contacts=contacts)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        # print(name, phone, email)
        flash('Contact added successfully')
        return redirect(url_for('index'))
    # return '<h1>Add Contact</h1>'

@app.route('/edit_contact')
def edit_contact():
    return '<h1>Edit Contact</h1>'

@app.route('/delete_contact')
def delete_contact():
    return '<h1>Delete Contact</h1>'
if __name__ == '__main__':
    app.run(port=5000, debug=True)