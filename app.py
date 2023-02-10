from flask import Flask, render_template, request, redirect, url_for, session
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = "000d88cd9d90036ebdd237eb6b0db000"


# A sample list to store the registration data
registrations = [

]

# Hardcoded username and hashed password for the admin
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = hashlib.sha256("admin123".encode()).hexdigest()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Process the registration form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        # Add the data to the registration list
        registrations.append({
            'name': name,
            'email': email,
            'phone': phone
        })

        return redirect(url_for('home'))

    return render_template('register.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    return render_template('admin.html', registrations=registrations)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            return (f"Incorrect username or password")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
