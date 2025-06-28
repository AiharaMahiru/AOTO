from flask import Blueprint, request, jsonify
from app import db
from app.models import Anniversary

anniversary_bp = Blueprint('anniversary_bp', __name__)

@anniversary_bp.route('/api/anniversaries', methods=['GET'])
def get_anniversaries():
    anniversaries = Anniversary.query.all()
    return jsonify([anniversary.to_dict() for anniversary in anniversaries])

@anniversary_bp.route('/api/anniversaries', methods=['POST'])
def create_anniversary():
    data = request.get_json()
    if not data or not 'name' in data or not 'date' in data or not 'user_id' in data:
        return jsonify({'error': 'Missing data'}), 400
    
    new_anniversary = Anniversary(
        name=data['name'],
        date=data['date'],
        is_lunar=data.get('is_lunar', False),
        user_id=data['user_id']
    )
    db.session.add(new_anniversary)
    db.session.commit()
    
    return jsonify(new_anniversary.to_dict()), 201

@anniversary_bp.route('/api/anniversaries/<int:id>', methods=['PUT'])
def update_anniversary(id):
    anniversary = Anniversary.query.get_or_404(id)
    data = request.get_json()
    
    anniversary.name = data.get('name', anniversary.name)
    anniversary.date = data.get('date', anniversary.date)
    anniversary.is_lunar = data.get('is_lunar', anniversary.is_lunar)
    
    db.session.commit()
    return jsonify(anniversary.to_dict())

@anniversary_bp.route('/api/anniversaries/<int:id>', methods=['DELETE'])
def delete_anniversary(id):
    anniversary = Anniversary.query.get_or_404(id)
    db.session.delete(anniversary)
    db.session.commit()
    return '', 204