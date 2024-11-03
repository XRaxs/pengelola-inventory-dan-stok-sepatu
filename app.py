from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Contoh data inventory sepatu dengan nama yang lebih realistis
inventory = {
    "1": {"name": "Nike Air Max 270", "price": 2000000, "stock": 20, "size": [38, 39, 40, 41, 42]},
    "2": {"name": "Adidas Ultraboost 21", "price": 2500000, "stock": 15, "size": [40, 41, 42, 43]},
    "3": {"name": "Puma RS-X3", "price": 1800000, "stock": 10, "size": [39, 40, 41, 42]},
    "4": {"name": "Converse Chuck Taylor", "price": 900000, "stock": 25, "size": [39, 40, 41, 42, 43]},
    "5": {"name": "Vans Old Skool", "price": 750000, "stock": 50, "size": [38, 39, 40, 41, 42]},
    "6": {"name": "New Balance 574", "price": 1200000, "stock": 12, "size": [40, 41, 42, 43, 44]},
    "7": {"name": "Reebok Classic Leather", "price": 950000, "stock": 30, "size": [38, 39, 40, 41, 42]},
    "8": {"name": "ASICS Gel-Kayano 27", "price": 1600000, "stock": 15, "size": [40, 41, 42, 43]},
    "9": {"name": "Timberland 6-Inch Boots", "price": 2200000, "stock": 8, "size": [39, 40, 41, 42]},
    "10": {"name": "Dr. Martens 1460", "price": 2100000, "stock": 20, "size": [39, 40, 41, 42, 43]},
    "11": {"name": "Under Armour HOVR Phantom", "price": 1700000, "stock": 40, "size": [38, 39, 40, 41, 42]},
    "12": {"name": "Saucony Jazz Original", "price": 800000, "stock": 18, "size": [40, 41, 42, 43]},
    "13": {"name": "Fila Disruptor II", "price": 900000, "stock": 22, "size": [38, 39, 40, 41, 42]},
    "14": {"name": "Nike Air Force 1", "price": 1300000, "stock": 12, "size": [40, 41, 42, 43]},
    "15": {"name": "Adidas Stan Smith", "price": 1100000, "stock": 6, "size": [39, 40, 41, 42]},
    "16": {"name": "Reebok Zig Kinetica", "price": 1400000, "stock": 24, "size": [39, 40, 41, 42, 43]},
    "17": {"name": "New Balance 990v5", "price": 2200000, "stock": 45, "size": [38, 39, 40, 41, 42]},
    "18": {"name": "ASICS Gel-Lyte III", "price": 1400000, "stock": 16, "size": [40, 41, 42, 43]},
    "19": {"name": "Puma Suede Classic", "price": 850000, "stock": 28, "size": [38, 39, 40, 41, 42]},
    "20": {"name": "Converse One Star", "price": 800000, "stock": 14, "size": [40, 41, 42, 43]}
}

class InventoryList(Resource):
    def get(self):
        return jsonify(inventory)

class InventoryDetail(Resource):
    def get(self, shoe_id):
        shoe = inventory.get(shoe_id)
        if shoe:
            return jsonify(shoe)
        return {"message": "Shoe not found"}, 404

class AddShoe(Resource):
    def post(self):
        new_id = str(len(inventory) + 1)
        data = request.get_json()
        inventory[new_id] = {
            "name": data["name"],
            "price": data["price"],
            "stock": data["stock"],
            "size": data.get("size", [])
        }
        return {"message": "Shoe added", "shoe": inventory[new_id]}, 201

class UpdateShoe(Resource):
    def put(self, shoe_id):
        if shoe_id in inventory:
            data = request.get_json()
            inventory[shoe_id].update(data)
            return {"message": "Shoe updated", "shoe": inventory[shoe_id]}
        return {"message": "Shoe not found"}, 404

class DeleteShoe(Resource):
    def delete(self, shoe_id):
        if shoe_id in inventory:
            deleted_shoe = inventory.pop(shoe_id)
            return {"message": "Shoe deleted", "shoe": deleted_shoe}
        return {"message": "Shoe not found"}, 404

# Menambahkan endpoint ke API
api.add_resource(InventoryList, '/inventory')
api.add_resource(InventoryDetail, '/inventory/<string:shoe_id>')
api.add_resource(AddShoe, '/inventory/add')
api.add_resource(UpdateShoe, '/inventory/update/<string:shoe_id>')
api.add_resource(DeleteShoe, '/inventory/delete/<string:shoe_id>')

if __name__ == '__main__':
    app.run(debug=True)
