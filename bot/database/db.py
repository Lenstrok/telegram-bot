from sqlalchemy import create_engine


DB = create_engine("sqlite:///example.db", echo=True, future=True)

# with engine.connect() as conn:
#     result = conn.execute(text("select 'hello world'"))
#     print(result.all())
