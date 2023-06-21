class BasicUiConwayAdapter:
    def update_screen(self, data):
        raise NotImplementedError


class UiConwayPort:
    def __init__(self):
        self.ui_adapter = None

    def set_ui_adapter(self, ui):
        self.ui_adapter = ui

    def update_screen(self, data):
        self.ui_adapter.update_screen(data)
