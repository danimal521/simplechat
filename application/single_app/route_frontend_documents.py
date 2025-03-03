# route_frontend_documents.py

from config import *
from functions_authentication import *
from functions_settings import *

def register_route_frontend_documents(app):
    @app.route('/documents', methods=['GET'])
    @login_required
    @user_required
    @enabled_required("enable_user_documents")
    def documents():
        user_id = get_current_user_id()
        
        if not user_id:
            print("User not authenticated.")
            return redirect(url_for('login'))
                
        return render_template('documents.html')
