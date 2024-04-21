import wad.detection,sys

#wad库获取网站使用的技术
print(sys.getdefaultencoding())
det=wad.detection.Detector()
url=input('请输入：')
print(det.detect(url))
