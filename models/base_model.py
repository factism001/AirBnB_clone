import uuid
from datetime import datetime


class BaseModel:
    """
    Base Model class that defines all common attributes/methods for other classes
    """
    def __init__(self):
        """
        Constructor to initialize instance variables
        """
        self.id = str(uuid.uuid4())  # generate a unique ID and convert to string
        self.created_at = datetime.now() # set created_at to current datetime
        self.updated_at = self.created_at  # set updated_at to current datetime
    
    def __str__(self):
        """
        Returns a string representation of the object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        dic = self.__dict__.copy()  # make a copy of the instance's __dict__
        new_dict = {}
        new_dict['created_at'] = self.created_at.isoformat()  # convert created_at to isoformat string
        new_dict['updated_at'] = self.updated_at.isoformat()  # convert updated_at to isoformat string
        new_dict['__class__'] = self.__class__.__name__  # add class name to dictionary
        return new_dict
