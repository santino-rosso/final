from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import bcrypt

# Configuración de la base de datos SQLite
engine = create_engine('sqlite:///FourInLine.db')

# Definición de la base para los modelos
Base = declarative_base()

# Definición de la clase Usuario (que incluye las columnas y restricciones)

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    partidas_ganadas = Column(Integer, default=0)
    partidas_perdidas = Column(Integer, default=0)
    partidas_empatadas = Column(Integer, default=0)

# Crear todas las tablas en la base de datos si no existen
Base.metadata.create_all(engine)

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)


#Clase para el hash de la contrasena
class HashPassword:
    def hash_password(password: str) -> str:
        """Genera un hash de la contraseña."""
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def verify_password(stored_hash: str, password: str) -> bool:
        """Verifica si la contraseña ingresada coincide con el hash almacenado."""
        return bcrypt.checkpw(password.encode(), stored_hash.encode())




