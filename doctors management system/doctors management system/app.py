from flask import Flask, render_template, redirect, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'tamil'

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Vishak46?'  # Replace with your actual password
app.config['MYSQL_DB'] = 'doctor_db'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/doctor')
def doctor():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM doctordetails")
    doctor_info = cur.fetchall()
    cur.close()
    return render_template('doctor.htm', doctors=doctor_info)

@app.route('/search', methods=['POST', 'GET'])
def search():
    search_results = []
    if request.method == "POST":
        search_term = request.form.get('doctorid')  # Use .get() to avoid KeyError
        cur = mysql.connection.cursor()
        query = "SELECT * FROM doctordetails WHERE id LIKE %s"
        cur.execute(query, ('%' + search_term + '%',))
        search_results = cur.fetchall()  # Use fetchall() to get all results
        cur.close()
        return render_template('doctor.htm', doctors=search_results)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        id_data = request.form.get('doctorid')  # Corrected to use .get()
        name = request.form.get('name')         # Corrected to use .get()
        email = request.form.get('email')       # Corrected to use .get()
        specialty = request.form.get('specialty')  # Corrected to use .get()

        # Check if all fields are provided
        if not all([id_data, name, email, specialty]):
            return render_template('doctor.htm', error="All fields are required.")

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO doctordetails (id, name, email, specialty) VALUES (%s, %s, %s, %s)",
                    (id_data, name, email, specialty))
        mysql.connection.commit()
        return redirect(url_for('doctor'))

@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM doctordetails WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('doctor'))

@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form.get('doctorid')  # Corrected to use .get()
        name = request.form.get('name')         # Corrected to use .get()
        email = request.form.get('email')       # Corrected to use .get()
        specialty = request.form.get('specialty')  # Corrected to use .get()

        # Check if all fields are provided
        if not all([id_data, name, email, specialty]):
            return render_template('doctor.htm', error="All fields are required for update.")

        # If specialty is not provided, set it to 'Unknown'
        if not specialty:
            specialty = 'Unknown'

        cur = mysql.connection.cursor()
        cur.execute("UPDATE doctordetails SET name=%s, email=%s, specialty=%s WHERE id=%s", 
                    (name, email, specialty, id_data))
        mysql.connection.commit()
        return redirect(url_for('doctor'))

if __name__ == "__main__":
    app.run(debug=True)
