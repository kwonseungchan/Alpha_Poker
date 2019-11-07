
from pyzbar import pyzbar
import argparse
import cv2
 
# argument 파서를 생성하고 파싱을 한다.
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
help="path to input image")
args = vars(ap.parse_args())

# 입력 이미지를 로드
image = cv2.imread(args["image"])

#이미지에서 바코드를 찾고 각 바코드를 디코드한다.
barcodes = pyzbar.decode(image)

# 검출한 바코드(barcodes)를 위한 루프
for barcode in barcodes:
# 바코드의 영역을 추출하고 영역 그리기
# 이미지의 바코드 주변에 박스를 그림
(x, y, w, h) = barcode.rect
cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# 바코드 데이터는 바이트 객체이므로 이미지에 그리려면 문자열을 먼져 바꿔야 한다.
barcodeData = barcode.data.decode("utf-8")

barcodeType = barcode.type


# 바코드 데이터와 타입을 이미지에 그림
text = "{} ({})".format(barcodeData, barcodeType)
cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
0.5, (0, 0, 255), 2)

# 바코드타입과 데이터를 터미널에 출력
print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

# 출력 이미지를 보여 줌
cv2.imshow("Image", image)
cv2.waitKey(0)
