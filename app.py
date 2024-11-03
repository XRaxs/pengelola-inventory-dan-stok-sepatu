from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Sample data for shoes inventory
shoes = {
    "1": {
        "brand": "Nike",
        "model": "Air Max 270",
        "quantity": 50,
        "price": 200000,
        "size": 42,
        "color": "Black",
        "category": "Sports"
    },
    "2": {
        "brand": "Adidas",
        "model": "UltraBoost",
        "quantity": 30,
        "price": 250000,
        "size": 40,
        "color": "White",
        "category": "Running"
    },
    "3": {
        "brand": "Puma",
        "model": "RS-X",
        "quantity": 25,
        "price": 180000,
        "size": 41,
        "color": "Blue",
        "category": "Casual"
    },
    "4": {
        "brand": "Reebok",
        "model": "Classic Leather",
        "quantity": 40,
        "price": 150000,
        "size": 43,
        "color": "Gray",
        "category": "Lifestyle"
    },
    "5": {
        "brand": "Converse",
        "model": "Chuck Taylor All Star",
        "quantity": 60,
        "price": 120000,
        "size": 38,
        "color": "Red",
        "category": "Casual"
    }
}

# Classes for CRUD functionality
class ShoeList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "Success",
            "count": len(shoes),
            "shoes": shoes
        }

class ShoeDetail(Resource):
    def get(self, shoe_id):
        if shoe_id in shoes:
            return {
                "error": False,
                "message": "Success",
                "shoe": shoes[shoe_id]
            }
        return {"error": True, "message": "Shoe not found"}, 404

class AddShoe(Resource):
    def post(self):
        data = request.get_json()
        shoe_id = str(len(shoes) + 1)
        new_shoe = {
            "brand": data.get("brand"),
            "model": data.get("model"),
            "quantity": data.get("quantity"),
            "price": data.get("price"),
            "size": data.get("size"),
            "color": data.get("color"),
            "category": data.get("category")
        }
        shoes[shoe_id] = new_shoe
        return {
            "error": False,
            "message": "Shoe added successfully",
            "shoe": new_shoe
        }, 201

class UpdateShoe(Resource):
    def put(self, shoe_id):
        if shoe_id in shoes:
            data = request.get_json()
            shoe = shoes[shoe_id]
            shoe["brand"] = data.get("brand", shoe["brand"])
            shoe["model"] = data.get("model", shoe["model"])
            shoe["quantity"] = data.get("quantity", shoe["quantity"])
            shoe["price"] = data.get("price", shoe["price"])
            shoe["size"] = data.get("size", shoe["size"])
            shoe["color"] = data.get("color", shoe["color"])
            shoe["category"] = data.get("category", shoe["category"])
            return {
                "error": False,
                "message": "Shoe updated successfully",
                "shoe": shoe
            }
        return {"error": True, "message": "Shoe not found"}, 404

class DeleteShoe(Resource):
    def delete(self, shoe_id):
        if shoe_id in shoes:
            deleted_shoe = shoes.pop(shoe_id)
            return {
                "error": False,
                "message": "Shoe deleted successfully",
                "shoe": deleted_shoe
            }
        return {"error": True, "message": "Shoe not found"}, 404

api.add_resource(ShoeList, '/shoes')
api.add_resource(ShoeDetail, '/shoes/<string:shoe_id>')
api.add_resource(AddShoe, '/shoes/add')
api.add_resource(UpdateShoe, '/shoes/update/<string:shoe_id>')
api.add_resource(DeleteShoe, '/shoes/delete/<string:shoe_id>')

if __name__ == '__main__':
    app.run(debug=True)
