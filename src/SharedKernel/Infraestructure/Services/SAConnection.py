from sqlalchemy import create_engine, Engine
import os

class SAConnection:
    _instance: "SAConnection | None" = None
    _engine: Engine | None = None
    
    def __new__(cls, *args, **kwargs): # pyright: ignore[reportUnknownParameterType, reportMissingParameterType]
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
    
    
    def get_engine(self):
        if self._engine is not None: return self._engine
        
        db_url = os.getenv("DATABASE_URL")
        assert db_url is not None
        self._engine = create_engine(db_url)
        return self._engine