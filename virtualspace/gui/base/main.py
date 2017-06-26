import sqlalchemy
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QWidget


class BaseMainView(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(BaseMainView, self).__init__(*args, **kwargs)
        self.setup_db()
        self.init_ui()
        self.show()

    def setup_db(self):
        # TODO: Fetch db from local settings.
        engine = sqlalchemy.create_engine('postgres+psycopg2://vs_dev:dev@localhost/virtualspace_dev', echo='debug')
        self.session = sqlalchemy.orm.sessionmaker(bind=engine)()

    def init_ui(self):
        # TODO: Prettify all of this.
        self.central_widget = QStackedWidget(self)
        self.setCentralWidget(self.central_widget)


class BaseWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(BaseWidget, self).__init__(*args, **kwargs)
        self.init_ui()

    @property
    def session(self):
        stacked_widget = self.parentWidget()
        main_window = stacked_widget.parentWidget()
        return main_window.session
