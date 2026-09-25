from sqlalchemy import create_engine, String, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship, joinedload

# 1. Setup the new DB and Classes
engine = create_engine('sqlite:///final.db')

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))

class Category(Base):
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    products: Mapped[list["Product"]] = relationship(back_populates="category")

class Product(Base):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    category: Mapped["Category"] = relationship(back_populates="products")

# Create the tables in the database automatically
Base.metadata.drop_all(engine) # Reset for testing
Base.metadata.create_all(engine)

if __name__ == '__main__':
    with Session(engine) as session:
        # 2. Create and Add Data
        tech_cat = Category(name='Tech')
        food_cat = Category(name='Food')
        
        laptop = Product(name='Laptop', category=tech_cat)
        apple = Product(name='Apple', category=food_cat)
        
        user1 = User(username='hero')
        
        session.add_all([tech_cat, food_cat, laptop, apple, user1])
        session.commit()
        
        # 3. Read (Eager Loading)
        print("\n--- Capstone Output ---")
        stmt = select(Category).options(joinedload(Category.products))
        categories = session.execute(stmt).scalars().unique().all()
        for cat in categories:
            for prod in cat.products:
                print(f"Category: {cat.name} | Product: {prod.name}")
