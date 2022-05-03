import models.model
import math
import controllers.controller
from flask import Flask, render_template, request, redirect, url_for, flash
from user import MyUser
from werkzeug.security import generate_password_hash, check_password_hash

# controllers.controller.select_main_page()
# controllers.controller.select_by_city("New York")

app = Flask(__name__)


@app.route('/', defaults={'user': 'Anonimus'}, methods=["GET", "POST"])
@app.route('/<user>', methods=["GET", "POST"])
def index(user):
    if request.method == "POST":
        if request.form['marketname']:
            result = models.model.select_by_name(request.form['marketname'])
            return render_template("index.html", result=result, user=user)
        else:
            return redirect("/")
    else:
        result = models.model.select_by_name()
        return render_template("index.html", result=result, user=user)


@app.route('/details/<id>/<x>/<y>', methods=["GET", "POST"])
def details(id, x, y):
    if request.method == "POST":
        if request.form['range']:
            result = models.model.select_by_name()
            result_filtered = []
            for item in result:
                if item[-2] and item[-1] and x and y:
                    radius = math.sqrt(pow((float(item[-2]) - float(x)), 2) + pow((float(item[-1]) - float(y)), 2))
                    if radius <= float(request.form['range']):
                        result_filtered.append(item)
            return render_template("index.html", result=result_filtered)
    result = models.model.select_details_page(id)
    rows = (
        "FMID", "MarketName", "Website", "Facebook", "Twitter", "Youtube", "OtherMedia", "street", "city", "County",
        "State", "zip", "Season1Date", "Season1Time", "Season2Date", "Season2Time", "Season3Date", "Season3Time",
        "Season4Date", "Season4Time", "x", "y", "Location", "Credit", "WIC", "WICcash", "SFMNP", "SNAP", "Organic",
        "Bakedgoods", "Cheese", "Crafts", "Flowers", "Eggs", "Seafood", "Herbs", "Vegetables", "Honey", "Jams", "Maple",
        "Meat", "Nursery", "Nuts", "Plants", "Poultry", "Prepared", "Soap", "Trees", "Wine", "Coffee", "Beans",
        "Fruits", "Grains", "Juices", "Mushrooms", "PetFood", "Tofu", "WildHarvested", "updateTime")
    rows = (i.capitalize() for i in rows)
    rows_dict = dict(zip(rows, result[0]))
    product_list = ["Organic", "Bakedgoods", "Cheese", "Crafts", "Flowers", "Eggs", "Seafood", "Herbs", "Vegetables",
                    "Honey", "Jams", "Maple", "Meat", "Nursery", "Nuts", "Plants", "Poultry", "Prepared", "Soap",
                    "Trees", "Wine", "Coffee", "Beans", "Fruits", "Grains", "Juices", "Mushrooms", "PetFood", "Tofu",
                    "WildHarvested"]

    contact_list = ["Website", "Facebook", "Twitter", "Youtube", "Othermedia"]
    return render_template("details.html", result=rows_dict, plist=product_list, clist=contact_list)


@app.route('/reviewadded')
def reviewadded():
    return render_template("reviewadded.html")


@app.route('/addreview/<id>', defaults={'user': 'Anonimus', 'email': 'empty@empty.com'}, methods=["GET", "POST"])
@app.route('/addreview/<id>/<user>/<email>', methods=["GET", "POST"])
def addreview(id, user, email):
    if request.method == "POST":
        models.model.insert_review(request.form['comments'], request.form['rating'], id, email)
        return redirect(url_for('reviewadded'))
    if user == 'Anonimus':
        return redirect(f'/login/{id}')
    else:
        return render_template('addreview.html')


@app.route('/login/<id>', methods=["GET", "POST"])
def login(id):
    if request.method == "POST":
        try:
            user_exist = models.model.select_user(request.form["email"])
            if user_exist and check_password_hash(user_exist[0][2], request.form["password"]):
                user = MyUser(user_exist[0][0], user_exist[0][1], request.form["password"])
                return redirect(f"/addreview/{id}/{user.usernamne}/{user.email}")
        except ValueError as e:
            flash(str(e))
        # return render_template("register.html")
    return render_template("login.html")


@app.route('/listreviews/<id>')
def listreviews(id):
    result = models.model.select_reviews_page(id)
    return render_template("listreviews.html", result=result)


@app.route('/filter', methods=["GET", "POST"])
def filter():
    if request.method == "POST":
        if request.form['city']:
            result = models.model.select_by_city(request.form['city'])
            return render_template("index.html", result=result)
        if request.form['state']:
            result = models.model.select_by_state(request.form['state'])
            return render_template("index.html", result=result)
    else:
        result_city = models.model.select_city()
        result_state = models.model.select_state()
        return render_template("filter.html", result_city=result_city, result_state=result_state)


@app.route('/register/', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            user = MyUser(request.form["email"], request.form["username"], request.form["password"])
            models.model.inserst_user(user.email, user.usernamne, user.password_hash)
        except ValueError as e:
            flash(str(e))
            # return render_template("register.html")
        # return render_template("login.html")
        return redirect(f'/')
    return render_template("register.html")


if __name__ == '__main__':
    app.run()
