import os
import dlib
import skimage
from skimage import io


class FaceFinder:
    # HOG face detector
    face_detector = dlib.get_frontal_face_detector()

    def __init__(self, imagePath):
        """
        """
        self.path=imagePath
        self.fileName=imagePath.split("/")[-1].split(".")[0]
        self.load_image()

    def load_image(self):
        """
        """
        # Load the image into an array
        self.image = io.imread(self.path)

    def showDetection(self):
        """
        """
        self.win = dlib.image_window()
        self.win.set_image(self.image)
        # Loop through each face we found in the image
        for face_rect in self.detected:
        	# rect : top, left, right and bottom
        	win.add_overlay(face_rect)
        #dlib.hit_enter_to_continue()

    def run(self):
        """
        """
        self.detected = self.face_detector(self.image, 1)
        facisize=len(self.detected)
        for n,face_rect in enumerate(self.detected):
            faceTarget=self.image[face_rect.top():face_rect.bottom(),
                                  face_rect.left():face_rect.right()]
            picPath="processing/{}_{}.jpg".format(n, self.fileName)
            io.imsave(picPath, faceTarget)
        print("[+] Found {} faces in  file {}".format(facisize, self.path))

    def getFaces(self):
        """
        """
        pass


############################################
if __name__ == "__main__":

    import argparse

    #load vars
    parser = argparse.ArgumentParser(description="Find faces using Hog")
    parser.add_argument("--image", "-i")
    args=parser.parse_args()

    #work
    facis=FaceFinder(args.image)
    facis.run()
    print("[+] Done processing image")
