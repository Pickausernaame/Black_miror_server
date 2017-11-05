from socket import *
import numpy as np
import cv2

host = "127.0.0.1"
port = 4096
buf = 1024
addr = (host, port)
fName = 'img.jpg'
timeOut = 0.05
face_casc = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")


def foo():
    while True:
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind(addr)
	print("Bind socker")
        data, address = s.recvfrom(buf)
        f = open(data, 'wb')
	print("Recieve some data")
        data, address = s.recvfrom(buf)
	print("Try to handle it")
        try:
	    print("We in try, brah")
            while(data):
		print("Bezishodnost")
                f.write(data)
                s.settimeout(timeOut)
                data, address = s.recvfrom(buf)
        except timeout:
            f.close()
            s.close()
	print("Fname",fName)
        image = cv2.imread(fName)
	print(image)
	print("Start recognition")
        """ Do some processing right here"""
        """faces = face_casc.detectMultiScale(image, 1.3, 5)
	print("Start loop")
    	for idx, (x, y, w, h) in enumerate(faces):
            max_area = area(faces)
            if idx == max_area:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                roi_face = image[y:y + h, x:x + w]
        print("Check faces")
	if len(faces) != 0:
            print("Faces on frame!")
        else:
            print("Faces not find!")"""
	"""Some processing end """
	cv2.imshow('recv', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    foo()
cv2.destroyAllWindows()
