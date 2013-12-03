import os
from django.conf import settings
from django.shortcuts import render_to_response, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def email_messages_listing(request):
	page = request.GET.get('page')
	if request.GET.get('fname'):
		file_name = request.GET.get('fname')
		return render_to_response('%s' % (file_name), locals(),context_instance=RequestContext(request))
	else:
		file_list_objs = [os.path.join("%s" % settings.EMAIL_FILE_PATH,d) for d in os.listdir('%s' % settings.EMAIL_FILE_PATH) if not os.path.isdir(d)]
		file_list_objs = sorted(file_list_objs, key=lambda x: os.path.getctime(x), reverse=True)[:settings.KEEP_FILES_COUNT]

		for each_file_list in file_list_objs:
			file_ext = each_file_list.split('.')
			if each_file_list.endswith(".log"):
				file_ext[1] = 'html'
				file_ext = ".".join(file_ext)
				os.rename('%s' % (each_file_list),'%s' % (file_ext))
		paginator = Paginator(file_list_objs, settings.LIST_EMAIL_MESSAGES_PER_PAGE)
		try:
			file_list = paginator.page(page)
		except PageNotAnInteger:
	        # If page is not an integer, deliver first page.
			file_list = paginator.page(1)
		except EmptyPage:
	        # If page is out of range (e.g. 9999), deliver last page of results.
			file_list = paginator.page(paginator.num_pages)
		return render_to_response('email_messages_log/temp_email_message.html', locals(),context_instance=RequestContext(request))

