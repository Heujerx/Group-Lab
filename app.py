from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.secret_key = 'top-secret'

@app.route('/Home')
def Home():
    return render_template('Home.html')

@app.route('/jeremiah')
def jeremiah():
    return render_template('jeremiah.html')

@app.route('/garrett', methods=['GET', 'POST'])
def garrett():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        inquiry = request.form.get('rel')
        # Here you could add code to handle the form data
        # For now, we'll just return the template with a success message
        return render_template('garrett.html', success=True)
    return render_template('garrett.html')

@app.route('/brent')
def brent():
    return render_template('brent.html')

@app.route('/')
def index():
    return redirect(url_for('Home'))


@app.route("/mason")
def mason():
    return render_template("mason.html",
        user={
            "name":"Mason Cable","role":"Dunwoody Student","company":"Dunwoody",
            "location":"Minneapolis, MN","email":"cabmass@dunwoody.edu",
            "website":"https://www.bing.com/ck/a?!&&p=cda631e5d9e62f11425f81d3ce6f86a18eaa9a5adae46b06af884b1dfc12d7acJmltdHM9MTc1OTM2MzIwMA&ptn=3&ver=2&hsh=4&fclid=3c770cdb-8e43-6301-36c2-1aa38f1c627c&u=a1L3ZpZGVvcy9yaXZlcnZpZXcvcmVsYXRlZHZpZGVvP3E9cmljaytyb2xsK3lvdXR1YmUrbGluayYmbWlkPTYyMjc4QTcyQzM5OTEzMzFBQTNBNjIyNzhBNzJDMzk5MTMzMUFBM0EmRk9STT1WQU1HWkM","avatar_url": "https://th.bing.com/th/id/OSK.HEROIAw8dKKjPgC6cEd1fX45yv5g3InX-MqH2mNBngeko80?w=472&h=280&c=13&rs=2&o=6&oif=webp&cb=12&dpr=1.3&pid=SANGAM",
            "about":"Dunwoody Student Focused on not failing Into to Hardware and Networking.",
            "verified":True,"available_for_hire":True,"updated_at":"Oct 2, 2025"
        },
        socials=[{"label":"GitHub","url":"https://github.com/MasonCable"},
                 {"label":"LinkedIn","url":"https://www.linkedin.com/in/masonscable/"}],
        stats=[{"label":"Known Birds","value":12},{"label":"Birds Owned","value":0},{"label":"Birds Sighted","value":3456}],
        skills=["Birds", "Chickens", "Turkeys", "Sparrow"],
        
        
        education=[{"institution":"Dunwoody College","degree":"B.S.","field":"Cybersecurity","start":"2025","end":None}],
        contact=[{"label":"Email Me","href":"mailto:jane@example.com"}],
        current_year=2025
    )
