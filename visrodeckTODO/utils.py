import uuid
from datetime import datetime

def generate_id():
    return str(uuid.uuid4())[:8]

def format_date(date_obj):
    return date_obj.strftime("%Y-%m-%d")

def get_now_iso():
    return datetime.now().isoformat()
