import cv2 as cv
import numpy as np

from numpy_version import NumpyConway
from opencv_ui_adapter import OpencvUiConwayAdapter


class OpencvConway(NumpyConway):
    def _make_initial_state(self):
        """Return an opencv image with random noise"""
        img = np.zeros((self.height, self.width, 1), dtype=np.uint8)
        return cv.randu(img, 0, 2)


if __name__ == '__main__':
    ui_adapter = OpencvUiConwayAdapter()
    app = OpencvConway(1080, 1000)
    app.set_ui_adapter(ui_adapter)
    app.run()
