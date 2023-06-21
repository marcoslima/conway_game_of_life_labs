import cv2 as cv

from basic_conway_ui_adapter import BasicUiConwayAdapter


class OpencvUiConwayAdapter(BasicUiConwayAdapter):
    def __del__(self):
        cv.destroyAllWindows()

    def update_screen(self, data):
        img = cv.threshold(data, 0, 255, cv.THRESH_BINARY)[1]
        cv.imshow(self.window, img)
        cv.waitKey(1)

    def __init__(self):
        super().__init__()
        self.window = 'Conway'
        cv.namedWindow(self.window, cv.WINDOW_AUTOSIZE)
