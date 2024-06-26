#!/usr/bin/python3
"""A City class that inherits from BaseModel"""


from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization method of an instance of City"""

        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get("state_id", "")
        self.name = kwargs.get("name", "")

    @classmethod
    def all(cls):
        """Returns a dictionary of all City instances"""
        from models import storage

        return ([obj for obj in storage.all().values()
                if isinstance(obj, cls)])

    @classmethod
    def show(cls, obj_id):
        """Returns an instance of City by id"""
        from models import storage

        all_instances = storage.all()
        for instance in all_instances.values():
            if isinstance(instance, cls) and instance.id == obj_id:
                return (instance)
        return (None)

    @classmethod
    def destroy(cls, obj_id):
        """Destroys an instance of City by ID"""
        from models import storage

        key = f"{cls.__name__}.{obj_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
            return (True)
        return (False)

    @classmethod
    def update(cls, obj_id, obj_dict):
        """Updates an instance of City by ID"""
        from models import storage

        instance = storage.all()[f'{cls.__name__}.{obj_id}']
        if instance:
            for key, value in obj_dict.items():
                if hasattr(instance, key):
                    attr_type = type(getattr(instance, key))
                    setattr(instance, key, attr_type(value))
                else:
                    setattr(instance, key, value)
            instance.save()
            return (True)
        return (False)
