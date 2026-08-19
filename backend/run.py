from flask import Flask, jsonify, request
from flask_cors import CORS
app=Flask(__name__)
CORS(app)

DESTINATIONS=[
 {"id":1,"name":"Goa","tag":"Beach escape","country":"India","image":"https://images.unsplash.com/photo-1512343879784-a960bf40e7f2"},
 {"id":2,"name":"Kashmir","tag":"Mountain retreat","country":"India","image":"https://images.unsplash.com/photo-1595815771614-ade9d652a65d"},
 {"id":3,"name":"Kerala","tag":"Tropical paradise","country":"India","image":"https://images.unsplash.com/photo-1602216056096-3b40cc0c9944"},
 {"id":4,"name":"Rajasthan","tag":"Royal getaway","country":"India","image":"https://images.unsplash.com/photo-1477587458883-47145ed94245"},
 {"id":5,"name":"Bali","tag":"Island escape","country":"Indonesia","image":"https://images.unsplash.com/photo-1537996194471-e657df975ab4"},
 {"id":6,"name":"Dubai","tag":"Luxury break","country":"UAE","image":"https://images.unsplash.com/photo-1512453979798-5ea266f8880c"}]

PACKAGES=[
 {"id":1,"title":"Goa Weekend Escape","destination":"Goa","duration":"3 Days / 2 Nights","price":12999,"old":16999,"image":"https://images.unsplash.com/photo-1512343879784-a960bf40e7f2","rating":4.8},
 {"id":2,"title":"Kashmir Paradise","destination":"Kashmir","duration":"6 Days / 5 Nights","price":24999,"old":31999,"image":"https://images.unsplash.com/photo-1595815771614-ade9d652a65d","rating":4.9},
 {"id":3,"title":"Kerala Backwaters","destination":"Kerala","duration":"5 Days / 4 Nights","price":19999,"old":25999,"image":"https://images.unsplash.com/photo-1602216056096-3b40cc0c9944","rating":4.8},
 {"id":4,"title":"Royal Rajasthan","destination":"Rajasthan","duration":"7 Days / 6 Nights","price":28999,"old":36999,"image":"https://images.unsplash.com/photo-1477587458883-47145ed94245","rating":4.7},
 {"id":5,"title":"Bali Island Holiday","destination":"Bali","duration":"5 Days / 4 Nights","price":42999,"old":49999,"image":"https://images.unsplash.com/photo-1537996194471-e657df975ab4","rating":4.9},
 {"id":6,"title":"Dubai Premium Break","destination":"Dubai","duration":"4 Days / 3 Nights","price":35999,"old":42999,"image":"https://images.unsplash.com/photo-1512453979798-5ea266f8880c","rating":4.8}]

@app.get('/api/health')
def health(): return jsonify(status='ok')
@app.get('/api/destinations')
def destinations(): return jsonify(DESTINATIONS)
@app.get('/api/packages')
def packages(): return jsonify(PACKAGES)
@app.post('/api/bookings')
def booking():
 data=request.get_json(silent=True) or {}
 required=['name','email','travel_date','guests','package_id']
 missing=[x for x in required if not data.get(x)]
 if missing: return jsonify(error='Missing: '+', '.join(missing)),400
 return jsonify(message='Booking confirmed',booking=data,status='confirmed'),201
@app.post('/api/auth/register')
def register(): return jsonify(message='Registration endpoint ready'),201
@app.post('/api/auth/login')
def login(): return jsonify(message='Login successful',token='demo-token')
if __name__=='__main__': app.run(debug=True,port=5000)
