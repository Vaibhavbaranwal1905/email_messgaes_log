import os
from django.conf import settings



def remove_files():
	file_list = [os.path.join("%s" % settings.EMAIL_FILE_PATH,d) for d in os.listdir('%s' % settings.EMAIL_FILE_PATH) if not os.path.isdir(d)]
	file_list = sorted(file_list, key=lambda x: os.path.getctime(x), reverse=True)
	files_to_keep = file_list[:settings.KEEP_FILES_COUNT]
	rest_files = [i for i in file_list if i not in files_to_keep]
	if rest_files:
		for each_files in rest_files:
			os.remove(each_files)