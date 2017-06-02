import openface
import cv2

class FaceFront:
    """
    """
    # http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
    predictor_model = "training/shape_predictor_68_face_landmarks.dat"
    face_aligner = openface.AlignDlib(predictor_model)
    face_pose_predictor = dlib.shape_predictor(predictor_model)

    def __init__(self, faceImagePath):
        """
        """
        self.path=faceImagePath
        self.load_image()

    def load_image(self):
        """
        """
        # Load the image into an array
        self.image = cv2.imread(self.path)
