from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Welcome to my Flask framework"


@app.route("/brand/<brand_id>", methods=["GET"])
def get_brand_by_id(brand_id):

    # E.g. Welcome to brand and the type is clothes
    type = request.args.get("type")
    condition = request.args.get("condition")
    return f"my brand id is:{brand_id},type:{type},condition {condition}"
    # Should be able to filter by condition of the article and should display the condition on the screen


# Route 2


@app.route("/product/<product_id>", methods=["GET"])
def get_product_by_id(product_id):
    return f"my product id is:{product_id}"


# Route 3
@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    return f"searching for: {query}"


if __name__ == "__main__":
    app.run(debug=True, port=6060)
