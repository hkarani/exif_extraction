from PIL import Image
from PIL.ExifTags import TAGS
import json

def extract_exif_data():
    pass

imagename = 'DSCN0010.jpg'
image = Image.open(imagename)
exif_data = image.getexif()

 
filename = image.filename if image.filename is not None else "Null"
fileformat = image.format if image.format is not None else "Null"
imagesize = image.size if image.size is not None else "Null"
bitspersample = exif_data.get(258) if exif_data.get(258) is not None else "Null"
datetimeoriginal = exif_data.get(36867) if exif_data.get(36867) is not None else "Null"
exposuretime = exif_data.get(33434) if exif_data.get(33434) is not None else "Null"
isanimated = getattr(image, "is_animated", False)
imageheight = image.height if image.height is not None else "Null"
imagewidth = image.width if image.width is not None else "Null"
yresolution = exif_data.get(283) if exif_data.get(283) is not None else "Null"
xresolution = exif_data.get(282) if exif_data.get(282) is not None else "Null"
model = exif_data.get(272) if exif_data.get(272) is not None else "Null"
make = exif_data.get(271) if exif_data.get(271) is not None else "Null"
datecreated = exif_data.get(306) if exif_data.get(306) is not None else "Null"
orientation = exif_data.get(274) if exif_data.get(274) is not None else "Null"
imagedescription = exif_data.get(270) if exif_data.get(270) is not None else "Null"
ycbcrsubsampling = exif_data.get(530) if exif_data.get(530) is not None else "Null"
software = exif_data.get(305) if exif_data.get(305) is not None else "Null"
flash = exif_data.get(37385) if exif_data.get(37385) is not None else "Null"
gpslatitude = exif_data.get(2) if exif_data.get(2) is not None else "Null"
gpslatituderef = exif_data.get(1) if exif_data.get(1) is not None else "Null"
gpslongitude = exif_data.get(4) if exif_data.get(4) is not None else "Null"
gpslongituderef = exif_data.get(3) if exif_data.get(3) is not None else "Null"
# print(filename)
# print(fileformat)
# print(imagesize)
# print(bitspersample)
# print(datetimeoriginal)
# print(exposuretime)
# print(isanimated)
# print(imageheight)
# print(imagewidth)
# print(yresolution)
# print(xresolution)
# print(model)
# print(make)
# print(datecreated)
# print(orientation)
# print(imagedescription)
# print(ycbcrsubsampling)
# print(software)
# print(flash)
# print(gpslatituderef)
# print(gpslatitude)
# print(gpslongitude)
# print(gpslongituderef)

exif_data_dictionary = {
    "filename": filename,
    "fileformat": fileformat,
    "imagesize": str(imagesize),
    "bitspersample": bitspersample,
    "datetimeoriginal": datetimeoriginal,
    "exposuretime": str(exposuretime),
    "isanimated": isanimated,
    "imageheight": imageheight,
    "imagewidth": imagewidth,
    "xresolution": str(xresolution),
    "yresolution": str(yresolution),
    "model": model,
    "make": make,
    "datecreated": datecreated,
    "orientation": orientation,
    "imagedescription": imagedescription,
    "ycbcrsubsampling": ycbcrsubsampling,
    "software": software,
    "gps" : {
        "gpslatituderef": gpslatituderef,
        "gpslatitude": str(gpslatitude),
        "gpslongituderef": gpslongituderef,
        "gpslongitude": str(gpslongitude)        
    }
    
}
exif_json = json.dumps(exif_data_dictionary)
print(exif_json)