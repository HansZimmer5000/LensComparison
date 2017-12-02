from CrawledLens import CrawledLens

#\\\\\\\\\\\\\\\\\\\\\\\\\
#	TESTDATA_CRAWLED_LENSES
#/////////////////////////

TESTDATA_CRAWLED_LENS1 = CrawledLens({
	'_id': 'Nikon 1 NIKKOR VR 10-30mm 3.5-5.6 PD-Zoom', \
	'Focal Length': '10-30mm', \
	'Aperture': '1:3.5-1:5.6', \
	'Filtersize': "", \
	'Magnification': "", \
	'Minimal Focus': "0.20m", \
 	'Mount': 'Nikon 1, Canon EF', \
	'Sensor compatibility': 'Nikon CX', \
 	'Weight': '85g', \
	'Size': '58x28mm'})

TESTDATA_CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT = CrawledLens({
	'_id': 'Nikon 1 NIKKOR VR 10-30mm 3.5-5.6 PD-Zoom', \
	'Focal Length': '10-30mm', \
	'Aperture': '1:3.5-1:5.6', \
	'Filtersize': "", \
	'Magnification': "", \
	'Minimal Focus': "0.20m", \
 	'Mount': '', \
	'Sensor compatibility': 'Nikon CX', \
 	'Weight': '', \
	'Size': '58x28mm'})

TESTDATA_CRAWLED_LENS1_OLD_MOUNT = CrawledLens({
	'_id': 'Nikon 1 NIKKOR VR 10-30mm 3.5-5.6 PD-Zoom', \
	'Focal Length': '10-30mm', \
	'Aperture': '1:3.5-1:5.6', \
	'Filtersize': "", \
	'Magnification': "", \
	'Minimal Focus': "0.20m", \
 	'Mount': 'Nikon 1', \
	'Sensor compatibility': 'Nikon CX', \
 	'Weight': '85g', \
	'Size': '58x28mm'})

TESTDATA_CRAWLED_LENS1_NEW_MOUNT = CrawledLens({
	'_id': 'Nikon 1 NIKKOR VR 10-30mm 3.5-5.6 PD-Zoom', \
	'Focal Length': '10-30mm', \
	'Aperture': '1:3.5-1:5.6', \
	'Filtersize': "", \
	'Magnification': "", \
	'Minimal Focus': "0.20m", \
 	'Mount': 'Canon EF', \
	'Sensor compatibility': 'Nikon CX', \
 	'Weight': '85g', \
	'Size': '58x28mm'})

TESTDATA_CRAWLED_LENS2 = CrawledLens({
	'_id': 'Canon Objektiv CN-E 35mm T1.5 L F', \
	'Focal Length': '35mm', \
	'Aperture': '1:1.5', \
	'Filtersize': "", \
	'Magnification': "", \
	'Minimal Focus': "", \
 	'Mount': 'Canon EF', \
	'Sensor compatibility': 'APS-C/ Kleinbild', \
 	'Weight': '', \
	'Size': ''		
})

TESTDATA_CRAWLED_LENS2_WITHOUT_SENSOR = CrawledLens({
	'_id': 'Canon Objektiv CN-E 35mm T1.5 L F', \
	'Focal Length': '35mm', \
	'Aperture': '1:1.5', \
	'Filtersize': "", \
	'Magnification': "", \
	'Minimal Focus': "", \
 	'Mount': 'Canon EF', \
	'Sensor compatibility': '', \
 	'Weight': '', \
	'Size': ''		
})

print(TESTDATA_CRAWLED_LENS2_WITHOUT_SENSOR.lens_dict)
print(TESTDATA_CRAWLED_LENS2.lens_dict)

TESTDATA_CRAWLED_LENS3 = CrawledLens({
	'_id': '', \
	'Focal Length': '25mm', \
	'Aperture': '1:0.95', \
	'Filtersize': "52mm", \
	'Magnification': "", \
	'Minimal Focus': "0.17m", \
 	'Mount': 'Micro-Four-Thirds', \
	'Sensor compatibility': 'Four-Thirds', \
 	'Weight': '410g',\
	'Size': '58.4x70mm'
})

TESTDATA_CRAWLED_LENS2_NAME = 'Canon Objektiv CN-E 35mm T1.5 L F'

TESTDATA_ALL_CRAWLED_LENSES_WITH_MISSING_INFO = {
	'Nikon 1 NIKKOR VR 10-30mm 3.5-5.6 PD-Zoom': TESTDATA_CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT,
	'Canon Objektiv CN-E 35mm T1.5 L F': TESTDATA_CRAWLED_LENS2_WITHOUT_SENSOR
}

TESTDATA_ALL_CRAWLED_LENSES_WITH_FULL_INFO = {
	'Nikon 1 NIKKOR VR 10-30mm 3.5-5.6 PD-Zoom': TESTDATA_CRAWLED_LENS1_WITHOUT_MOUNT_AND_WEIGHT,
	'Canon Objektiv CN-E 35mm T1.5 L F': TESTDATA_CRAWLED_LENS2_WITHOUT_SENSOR,
	'': TESTDATA_CRAWLED_LENS3
}
