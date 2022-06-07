# -*- coding: utf-8 -*-
from config.settings import ProductionConfig

from private import (create_app, db,)
from private.models import (User, Right)


app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db, 'User': User, 'Right': Right,
    }

if __name__ == "__main__":
    app.run()
