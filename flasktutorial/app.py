from flask import Flask,  url_for, request, redirect, render_template
from utility import Utility

#float url need to have a decimal in the url

app = Flask(__name__)

@app.route("/") #This is the home page
def hello():
    return """
    <html>
    <h1> Welcome to the home page </h1>
    <p> This is a paragraph </p>
    <img src="https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940">
    </html>
    """

@app.route("/products") #To open the page go to localhost:5000/products
def products():
    return """
    <html>
    <h1> Products </h1>
    <p> List of products </p>
    <ul>
        <li> Product 1 </li>
        <li> Product 2 </li>
        <li> Product 3 </li>
    </ul>
    </html>
    """

@app.route("/hello/<name>") #To open the page go to localhost:5000/hello/<name>
def sayHello(name):
    return f"""
    <html>
        <h1> Hello {name} </h1>
    </html>
    """

# @app.route("/simpleInterest/<principal>/<rate>/<time>")
@app.route("/simpleInterest/<int:principal>/<int:rate>/<int:time>")
@app.route("/simpleInterest/<int:principal>", defaults={"rate": 6, "time": 1})
@app.route("/simpleInterest/<int:principal>/<int:rate>", defaults={"time": 1})
def calculateSimpleInterest(principal, rate, time):
    # intrest = (int(principal) * int(rate) * int(time)) / 100
    intrest = (principal * rate * time) / 100
    return f"""
    <html>
        <head> <title> Simple Interest Calculator </title> </head>
        <body>
            <h2> Principal: {principal} </h2>
            <h2> Rate: {rate} </h2>
            <h2> Time: {time} </h2>
            <hr class="solid">
            <h2> Simple Interest: {intrest} </h2>
    </html>
    """
@app.route("/sayhi/<string:code>/<string:name>")
def sayhi(code, name):
    return f"""
    <html>
        <head> <title> Say hi</title> </head>
        <body>
            <h1> Hello: {name} </h1>
            <p> Code: {code} </p>
        </body>
    </html>
    """

@app.route("/geturls", methods=["GET"])
def geturls():
    return f"""
    <html>
        <head> <title> Links </title> </head>
        <body>
            <ol>
                <li> <a href="{url_for('hello')}"> Home </a> </li>
                <li> <a href="/products"> Products </a> </li>
                <li> <a href="/hello/J0hn"> Hello </a> </li>
                <li> <a href="{url_for('sayhi', code='123', name='John')}"> Say hi </a> </li>
                <li> <a href="{url_for('calculateSimpleInterest', principal=1000, rate=5, time=2)}"> Simple Interest </a> </li>
                <li> <a href="{url_for('login')}"> Login </a> </li>
            </ol>
        </body>
    </html>
    """

@app.route("/login")
def login():
    return f"""
    <html>
        <head> <title> Login </title> </head>
        <body>
            <h1> Login </h1>
            <form name="login" method="POST" action="/dologin">
                <input type="text" name="email" placeholder="Email" size="50">
                <input type="password" name="password" placeholder="Password" size="20">
                <input type="submit" name="submit" value="Login">
            </form>
        </body>
    </html>
    """
@app.route("/dologin", methods=["POST"])
def dologin():
    email = request.form["email"]
    password = request.form["password"]

    # Validate fields
    if not email or not password:
        return """
        <html>
            <h1> Error: Both email and password are required! </h1>
            <a href="/login">Go back to login</a>
        </html>
        """

    # Connect to the database
    db = Utility.dbConnect()
    cursor = db.cursor(dictionary=True)

    # Query the user
    try:
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        user = cursor.fetchone()

        if user:
            return f"""
            <html>
                <head> <title> Dashboard </title> </head>
                <body>
                    <h1> Welcome, {email}! </h1>
                    <p> You have successfully logged in! </p>
                </body>
            </html>
            """
        else:
            return """
            <html>
                <h1> Invalid credentials. Please try again. </h1>
                <a href="/login">Go back to login</a>
            </html>
            """
    finally:
        cursor.close()
        db.close()

    
    # Optionally, validate against a database or predefined values
    if email == "test@example.com" and password == "password123":
        return f"""
        <html>
            <head> <title> Dashboard </title> </head>
            <body>
                <h1> Welcome, {email}! </h1>
                <p> You have successfully logged in! </p>
            </body>
        </html>
        """
    else:
        return """
        <html>
            <h1> Invalid credentials. Please try again. </h1>
            <a href="/login">Go back to login</a>
        </html>
        """

@app.route("/dashboard")
def dashboard():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Connect to the database
        db = Utility.dbConnect()
        cursor = db.cursor()

        # Insert user into the database
        try:
            query = "INSERT INTO users (email, password) VALUES (%s, %s)"
            cursor.execute(query, (email, password))
            db.commit()
            return f"""
            <html>
                <h1> Registration successful for {email}! </h1>
                <a href="/login">Go to login</a>
            </html>
            """
        except mysql.Error as err:
            return f"""
            <html>
                <h1> Error: {err} </h1>
                <a href="/register">Go back to registration</a>
            </html>
            """
        finally:
            cursor.close()
            db.close()

    return """
    <html>
        <head> <title> Register </title> </head>
        <body>
            <h1> Register </h1>
            <form name="register" method="POST">
                <input type="text" name="email" placeholder="Email" size="50">
                <input type="password" name="password" placeholder="Password" size="20">
                <input type="submit" name="submit" value="Register">
            </form>
        </body>
    </html>
    """






# if __name__ == "__main__":
#     app.run()