from . import app    # For application discovery by the 'flask' command. 
from . import views  # For import side-effects of setting up routes. 
from . import db_models
from . import sql_settings

from . import forms


if __name__ == "__main__":
    app.run()
    

