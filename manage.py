from flask_migrate import Migrate
from app import create_app, db
from app.models import *

app = create_app('default')

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)