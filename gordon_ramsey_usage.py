import sys
from gzip import GzipFile
from base64 import b64decode

if sys.version_info[0] < 3:
  from cStringIO import StringIO
else:
  from io import BytesIO as StringIO

image_data = """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
	lQl6uUIAAA=="""

if(len(sys.argv) < 2):
  string_img_file = GzipFile(mode='r', fileobj=StringIO(b64decode(image_data)))
  image = string_img_file.read()
  string_img_file.close()

  print(image.decode('utf-8'))

  print("\n\n\nNOT ENOUGH ARGUMENTS YOU DUNCE")
  exit()

