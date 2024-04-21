import wad.detection,sys

print(sys.getdefaultencoding())
det=wad.detection.Detector()
url=input('请输入：')
print(det.detect(url))