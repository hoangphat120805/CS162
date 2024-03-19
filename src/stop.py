class Stop:
    def __init__(self, stop):
        for key in stop:
            setattr(self, key, stop[key])
    
    @property
    