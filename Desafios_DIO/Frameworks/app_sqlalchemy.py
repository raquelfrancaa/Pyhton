from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    contas = relationship("Conta", back_populates="cliente")

class Conta(Base):
    __tablename__ = 'contas'
    id = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)
    saldo = Column(Float, nullable=False)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    cliente = relationship("Cliente", back_populates="contas")

engine = create_engine('sqlite:///bank.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

cliente1 = Cliente(nome="João Silva", idade=35)
conta1 = Conta(tipo="Corrente", saldo=1000.0, cliente=cliente1)
conta2 = Conta(tipo="Poupança", saldo=5000.0, cliente=cliente1)

session.add(cliente1)
session.add(conta1)
session.add(conta2)
session.commit()

clientes = session.query(Cliente).all()
for cliente in clientes:
    print(f"Cliente: {cliente.nome}, Idade: {cliente.idade}")
    for conta in cliente.contas:
        print(f"  Conta {conta.tipo} com saldo de {conta.saldo}")
