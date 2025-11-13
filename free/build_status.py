from datetime import datetime
import requests
from constants import STATUS_ENDPOINT


class BuildStatus:
    @staticmethod
    def build_date() -> str:
        return datetime.utcnow().isoformat()
    
    @classmethod
    def notify(cls, merge_request_id, status):
        build_status = {
            "id": merge_request_id,
            "status": status,
            "build_at": cls.build_date(),
        }
        response = requests.post(STATUS_ENDPOINT, json=build_status)
        response.raise_for_status()
        return response