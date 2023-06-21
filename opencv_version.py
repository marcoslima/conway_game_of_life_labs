import numpy as np
import cv2 as cv

from basic_conway import BasicConway


class OpencvConway(BasicConway):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.screen = self._make_initial_state()
        self.window = 'Conway'
        cv.namedWindow(self.window, cv.WINDOW_NORMAL)

    def __del__(self):
        cv.destroyAllWindows()

    def show(self):
        img = cv.threshold(self.screen, 0, 255, cv.THRESH_BINARY)[1]
        cv.imshow(self.window, img)
        cv.waitKey(1)

    def tick(self):
        somas = np.array([np.roll(y, r2, axis=1)
                          for y in np.array([np.roll(self.screen, r1, axis=0)
                                             for r1 in [-1, 0, 1]])
                          for r2 in [-1, 0, 1]]).sum(axis=0) - self.screen

        self.screen = np.bitwise_or(somas == 3,
                                    np.bitwise_and(self.screen,
                                                   somas == 2))

    def _make_initial_state(self):
        """Return an opencv image with random noise"""
        img = np.zeros((self.height, self.width, 1), dtype=np.uint8)
        return cv.randu(img, 0, 2)


if __name__ == '__main__':
    app = OpencvConway(1920, 1080)
    app.run()
