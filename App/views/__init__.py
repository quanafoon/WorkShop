# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .login import login_views
from .auth import auth_views
from .signup import signup_views
from .home import home_views

views = [user_views, login_views, auth_views, signup_views, home_views] 
# blueprints must be added to this list