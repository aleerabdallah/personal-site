from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import Post
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from bs4 import BeautifulSoup
import time




def index(request):
	if request.htmx:
		db_start = time.time()
		posts = Post.objects.all()
		db_time = time.time() - db_start
		# print("Datebase lookup: ", db_time)
		context = {'posts': posts}

		return render(request, 'blog/home.html', context)
	db_start = time.time()
	posts = Post.objects.all()
	db_end = time.time()
	db_time = db_end - db_start
	print("Datebase lookup: ", db_time)
	context = {'posts': posts}

	return render(request, 'blog/home.html', context)




def posts(request):
	if request.htmx:
		if request.method == 'POST':
			email = request.POST['email']
			print(email)
			messages.add_message(request, messages.SUCCESS, "Thanks for Subscribing")
			# messages.success(request, "Profile details updated.")
			return render(request, 'blog/partials/message.html')

		posts = Post.objects.all()
		context = {'posts': posts}
		return render(request, 'blog/posts.html', context)
	posts = Post.objects.all()
	context = {'posts': posts}

	return render(request, 'blog/posts.html', context)


def post(request, slug):
	post = Post.objects.get(slug=slug)
	# comments = post.comments.filter(active=True)
	post_category = post.category
	
	# comments = post.get_comments
	related_posts = Post.objects.exclude(pk=post.id).filter(category=post_category.id)
	if request.method == 'POST':
		print("Hello")
	else:
		soup = BeautifulSoup(post.body, 'html.parser')
		toc_links = []
		for heading in soup.find_all(['h1', 'h2', 'h3']):
			# tag_name = heading.name
			heading["id"] = f"{heading.text.strip()}"
			# print(heading.attrs)
			if len(heading["id"]) > 10:
				toc_links.append({
					'id': heading["id"],
					'text': heading.text.strip()
				})
		
		post.body = str(soup)
		post.save()

		soup2 = BeautifulSoup(post.body, 'html.parser')
		for h2 in soup2.find_all(['h1', 'h2', 'h3']):
			print(h2.get("id"))

		# form = CommentForm()
		context = {'post': post, 'toc_links': toc_links, 'related_posts': related_posts}
		return render(request, 'blog/post.html', context)


def aboutUs(request):
	if request.htmx:
		return render(request, 'blog/about.html')
	return render(request, 'blog/about.html')


def contactUs(request):
	return render(request, 'blog/contact_us.html')



