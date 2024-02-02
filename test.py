from PIL import Image
from PIL.ExifTags import TAGS
# from exif import Image

# exif_tags = ['image_description', 'make', 'model', 'orientation', 'x_resolution', 'y_resolution', 
#              'resolution_unit', 'software', 'datetime', 'y_and_c_positioning', '_exif_ifd_pointer',
#              '_gps_ifd_pointer', 'compression', 'jpeg_interchange_format', 'jpeg_interchange_format_length',
#              'exposure_time', 'f_number', 'exposure_program', 'photographic_sensitivity', 'exif_version', 
#              'datetime_original', 'datetime_digitized', 'components_configuration', 'exposure_bias_value',
#              'max_aperture_value', 'metering_mode', 'light_source', 'flash', 'focal_length', 'maker_note', 
#              'user_comment', 'flashpix_version', 'color_space', 'pixel_x_dimension', 'pixel_y_dimension', 
#              '_interoperability_ifd_Pointer', 'file_source', 'scene_type', 'custom_rendered', 'exposure_mode',
#              'white_balance', 'digital_zoom_ratio', 'focal_length_in_35mm_film', 'scene_capture_type',
#              'gain_control', 'contrast', 'saturation', 'sharpness', 'subject_distance_range', 
#              'gps_latitude_ref', 'gps_latitude', 'gps_longitude_ref', 'gps_longitude', 'gps_altitude_ref',
#              'gps_timestamp', 'gps_satellites', 'gps_img_direction_ref', 'gps_map_datum', 'gps_datestamp'
# ]

# with open('Arbitro.tiff', 'rb') as image_file:
#     my_image = Image(image_file)
#     #my_image.get("model")
#     exif_keys = my_image.list_all()
#     # for exif_key in exif_keys:
        
#     print(exif_keys)

# import exifread
# # Open image file for reading (must be in binary mode)
# f = open('Arbitro.tiff', 'rb')

# # Return Exif tags
# tags = exifread.process_file(f)
# for tag in tags.keys():
#     # if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
#     #     print("Key: %s, value %s" % (tag, tags[tag]))
#     print(tag)
imagename = 'Arbitro.tiff'
image = Image.open(imagename)


# getting the basic metadata from the image
info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1)
}

for label,value in info_dict.items():
    print(f"{label:25}: {value}")


exifdata = image.getexif()
print("###############")
print("")
# iterating over all EXIF data fields
for tag_id in exifdata:
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")