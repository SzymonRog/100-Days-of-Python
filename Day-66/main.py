from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns if column.name != "id" }



with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe =random.choice(cafes).to_dict()
    cafe = {
        "cafe" : random_cafe
    }
    return jsonify(cafe)

@app.route("/all")
def get_all_cafes():
    cafes = db.session.query(Cafe).all()

    cafes = {
        "cafe" : [cafe.to_dict() for cafe in cafes]
    }
    return jsonify(cafes)


@app.route("/search")
def search_cafe():
    loc = request.args.get("loc")

    if not loc:
        return jsonify({"error": "No location provided."}), 400

    filtered_cafes = db.session.query(Cafe).filter_by(location=loc.capitalize()).all()
    if filtered_cafes:
        cafes = {
            "cafe" : [cafe.to_dict() for cafe in filtered_cafes]
        }
        return jsonify(cafes)
    return jsonify({"error": "No cafes found in that location."})

@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    map_url = request.form.get("map_url")
    img_url = request.form.get("img_url")
    location = request.form.get("location")
    has_sockets = bool(request.form.get("has_sockets"))
    has_toilet = bool(request.form.get("has_toilet"))
    has_wifi = bool(request.form.get("has_wifi"))
    can_take_calls = bool(request.form.get("can_take_calls"))
    seats = request.form.get("seats")
    coffee_price = request.form.get("coffee_price")

    cafe = Cafe(
        name=name,
        map_url=map_url,
        img_url=img_url,
        location=location,
        has_sockets=has_sockets,
        has_toilet=has_toilet,
        has_wifi=has_wifi,
        can_take_calls=can_take_calls,
        seats=seats,
        coffee_price=coffee_price
    )

    db.session.add(cafe)
    db.session.commit()
    return jsonify({"success": "Cafe added successfully."})

@app.route("/update-price/<int:id>", methods=["PATCH"])
def update_price(id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).filter_by(id=id).first()
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify({"success": "Price updated successfully."})
    return jsonify({"error": "Cafe not found."}), 404

@app.route("/report-closed/<int:id>", methods=["DELETE"])
def report_closed(id):
    api_key = request.args.get("api_key")
    if not api_key == "TopSecretAPIKey":
        return jsonify({"error": "Invalid API key. You are not allowed here"}), 403

    cafe = db.session.query(Cafe).filter_by(id=id).first()
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify({"success": "Cafe deleted successfully."})
    return jsonify({"error": "Cafe not found."}), 404


if __name__ == '__main__':
    app.run(debug=True)
