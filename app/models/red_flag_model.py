from app.models.user_model import user


class incident:

    def __init__(self, red_flag_dict):
        self.incident_id = red_flag_dict.get("incident_id")
        self.created_on = red_flag_dict.get("createdOn")
        self.created_by = red_flag_dict.get("createdBy")
        self.incident_type = red_flag_dict.get("incident_type")
        self.location = red_flag_dict.get("location")
        self.status = red_flag_dict.get("status")
        self.images = red_flag_dict.get("images")
        self.videos = red_flag_dict.get("videos")
        self.comment = red_flag_dict.get("comment")

    def creat_red_flag(self):
        return {
            "incident_id": self.incident_id,
            "created_on": self.created_on,
            "createdBy": self.created_by,
            "incident_type": self.incident_type,
            "location": self.location,
            "status": self.status,
            "images": self.images,
            "vidoes": self.videos,
            "comment": self.comment
        }