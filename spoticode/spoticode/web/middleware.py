# Project
from spoticode.web.routers import set_current_db

class DatabaseSelectorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        db_choice = request.session.get("db_choice")
        if db_choice:
            set_current_db(db_choice)
        response = self.get_response(request)
        return response
