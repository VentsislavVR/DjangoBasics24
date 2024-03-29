
from django.http import HttpResponse
from django.shortcuts import render

from django101.tasks.models import Task


# Create your views here.
# def index(request):
#     name = request.GET.get("name", "No name")
#     content = f"<h1>Hello, world. You're at {name}.</h1>"
#     return http.HttpResponse(
#         content)

    # headers =
    # 'Content-Type: application/json',

def index(request):
    # title_filter = request.GET.get("filter", None)
    # tasks = Task.objects.all()
    # if title_filter:
    #     tasks = tasks.filter(title__icontains=title_filter)
    #
    # if not tasks:
    #     return HttpResponse(
    #     "<h1>No tasks!!!</h1>"
    # )
    # result = []
    # for task in tasks:
    #     result.append(f"""
    #     <li>
    #     <h2>{task.title}</h2>
    #     <p>{task.description}</p>
    #     </li>
    #     """
    #     )
    # ul = f"<ul>{''.join(result)}</ul>"
    #
    # content = f"""
    # <h1>{len(tasks)}</h1>
    # {ul}
    # """
    title_filter = request.GET.get("title_filter", '')
    tasks = Task.objects.all()
    if title_filter:
        tasks = tasks.filter(title__icontains=title_filter)
    context = {
        'title': 'Hello World this is THE TASKS APP',
        'tasks': tasks,
        'task_count': tasks.count(),
        'title_filter': title_filter
    }

    # return HttpResponse(content)
    return render(request,
                  "tasks/index.html",
                  context
                  )