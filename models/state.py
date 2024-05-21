#!/usr/bin/python3
"""A state class that inherits from BaseModel"""


from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel"""

    name = ""

    @classmethod
    def all(cls):
        """Returns a dictionary of all State instances"""
        from models import storage

        return ([obj for obj in storage.all().values()
                if isinstance(obj, cls)])

    @classmethod
    def show(cls, obj_id):
        """Returns an instance of State by Id"""
        from models import storage

        all_instances = storage.all()
        for instance in all_instances.values():
            if isinstance(instance, cls) and instance.id == obj_id:
                return (instance)
        return (None)
