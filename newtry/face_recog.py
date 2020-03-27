# face_recog.py

import face_recognition
import cv2
import camera
import os
import numpy as np

hisname='Unknown'
def face() :
    class FaceRecog():
        def __init__(self):
            # Using OpenCV to capture from device 0. If you have trouble capturing
            # from a webcam, comment the line below out and use a video file
            # instead.
            self.camera = camera.VideoCamera() #카메라 모듈에서 만들어논 videocamera클래스를 작동

            self.known_face_encodings = []
            self.known_face_names = []

            # Load sample pictures and learn how to recognize it.
            dirname = 'knowns'
            files = os.listdir(dirname) #os.listdir를 사용하면 해당 디렉터리에 있는 파일들의 리스트를 구할 수 있다
            for filename in files:
                name, ext = os.path.splitext(filename) #확장자만 따로 분류하여 ext에 저장하고 filename은 name에 저장한다.
                if ext == '.jpg': 
                    self.known_face_names.append(name) #self.know_face_name에 name을 받아와 저장한다.
                    pathname = os.path.join(dirname, filename) #경로에 dirname과 filename 을 추가하여 새로운 경로생성
                    img = face_recognition.load_image_file(pathname)#pathname에 있는 이미지를 img에 넣고
                    face_encoding = face_recognition.face_encodings(img)[0] #그 img를 인코딩한다
                    self.known_face_encodings.append(face_encoding)

            # Initialize some variables
            self.face_locations = []
            self.face_encodings = []
            self.face_names = []
            self.process_this_frame = True

        def __del__(self): #소멸자메소드
            del self.camera

        def get_frame(self):
            # Grab a single frame of video
            frame = self.camera.get_frame()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            #이미지를 BGR 색상 (OpenCV에서 사용)에서 RGB 색상 (face_recognition에서 사용)으로 변환
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time 다른 모든 비디오 프레임 만 처리하여 시간을 절약
            if self.process_this_frame:
                # Find all the faces and face encodings in the current frame of video 현재 비디오 프레임에서 모든 얼굴 및 얼굴 인코딩 찾기
                self.face_locations = face_recognition.face_locations(rgb_small_frame) #얼굴위치찾아서 저장
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations) #얼굴위치 인코딩해서 저장

                self.face_names = []
                for face_encoding in self.face_encodings:
                    # See if the face is a match for the known face(s) selfknowfaceencoding과 faceencoding 비교
                    distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                    min_value = min(distances) #min()은 받는 인자값중 가장 작은 값을 내보내는것

                    # tolerance: How much distance between faces to consider it a match. Lower is more strict.
                    # 0.6 is typical best performance.
                    global hisname
                    name = "Unknown"
                    if min_value < 0.6:
                        index = np.argmin(distances)
                        name = self.known_face_names[index]
                        hisname=name

                    self.face_names.append(name)
                    

            self.process_this_frame = not self.process_this_frame

            # Display the results
            for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                # 4분의1로 줄여놨으니 다시 백업
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            return frame

        def get_jpg_bytes(self):
            frame = self.get_frame()
            # We are using Motion JPEG, but OpenCV defaults to capture raw images,
            # so we must encode it into JPEG in order to correctly display the
            # video stream.
            ret, jpg = cv2.imencode('.jpg', frame)
            return jpg.tobytes()


    face_recog = FaceRecog()
    print(face_recog.known_face_names)
    while True:
        frame = face_recog.get_frame()  # 출력되는 카메라 없이 스레드로 이걸 켜서 얼굴을 인식시켜 그 값을 전달하기 위해 카메라는 껐다.

        # show the frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if hisname=='yoo' :
            print(hisname)  # yoo가 인식되면 yoo를 출력하고 카메라를 종료시킨다. unknown이 나와도 종료되도록 elif를 만들고 그 값을 그대로 전달해 unknown이 아니면 범죄자 알림을 보내자.
            break

    # do a bit of cleanup
    cv2.destroyAllWindows()
    print('finish')
