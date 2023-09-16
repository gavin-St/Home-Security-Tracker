import uuid
from flask import jsonify, request
from blueprints.camera.bp import Camera
from sql.data_models import Camera
from extensions import db

@camera.route('/<user_id>/cameras/<camera_id>/create-snapshot', methods=['POST'])
def create_snapshot(user_id, camera_id):
    if camera_id:
        user_id = camera_id
        
    camera_instance = Camera.query.filter_by(user_id=user_id).filter_by(camera_id=camera_id).first()
    if not camera_instance:
        return jsonify({'status': 'error', 'message': 'Camera not found'}), 404
    
    data = request.get_json()
    snapshot = data.get('snapshot')
    if not data or not snapshot:
        return jsonify({'status': 'error', 'message': 'No snapshot provided'}), 400
    
    namespace_uuid = uuid.uuid4()

    c = Camera()
    c.camera_id = camera_id
    c.snapshot = data.get('snapshot')
    c.snapshot_title = data.get('snapshot_title')

    try:
        c.save()
    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error inserting record: {str(e)}'}), 500
    return jsonify({'status':'success', 'snapshot': c.as_dict()}), 201