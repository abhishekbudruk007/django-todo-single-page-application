from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.http import HttpResponse ,HttpResponseRedirect
from django.urls import reverse ,reverse_lazy
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django_datatables_view.base_datatable_view import BaseDatatableView
import json

from .forms import TodoTaskForm
from .models import TodoTask
from .serializers import ToDoTaskSerializer

#Class to Display HomePage and Create Tasks
class HomePage (generic.View):
    def get(self, request, *args, **kwargs):
        template_name = 'myproject/myapp/index.html'
        form = TodoTaskForm()
        context = {'form':form}
        return render(request,template_name, context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name','')
        # print("This is Post",name)
        model = TodoTask()
        model.name=name
        model.save()
        return HttpResponse(json.dumps({"status":"success","message":"Task Saved" }))





#This class is to get all Todo Tasks
class GetAllTasks(BaseDatatableView):
    model = TodoTask
    serializer_class= ToDoTaskSerializer

    #Columns to be displayed in datatable
    columns = ['sr_no','name', 'is_completed', 'actions']
    #Columns By which we can order data
    order_columns = ['id','name','is_completed']

    def get_initial_queryset(self):
        qs = TodoTask.objects.filter().order_by("-updated_at")
        return qs

    # This function is used to manually change the columns
    def render_column(self, row, column):
        if column == 'sr_no':
            return ''
        elif column == 'name':
            return (row.name).upper()
        elif column == 'is_completed':
            print("row.is_completed",row.is_completed)
            if(row.is_completed == True):
                return "YES"
            else:
                return "NO"
        elif column == 'actions':
            if(row.is_completed == True):
                return '<div class="list-icons text-center"><div class="dropdown"><a href="#" class="list-icons-item" data-toggle="dropdown"><i class="icon-menu9"></i></a><div class="dropdown-menu dropdown-menu-right"><a class="dropdown-item updatetask"  data-id="' + str(row.id) + '/updatetask/"><i class="icon-pencil"></i>Edit</a><a href="#" class="dropdown-item markaspending" data-id="' + str(
                    row.id) + '/markaspending/"><i class="icon-trash"></i>Mark as Pending</a></div></div></div>'
            else:
                return '<div class="list-icons text-center"><div class="dropdown"><a href="#" class="list-icons-item" data-toggle="dropdown"><i class="icon-menu9"></i></a><div class="dropdown-menu dropdown-menu-right"><a class="dropdown-item updatetask"  data-id="' + str(row.id) + '/updatetask/"><i class="icon-pencil"></i>Edit</a><a href="#" class="dropdown-item markasdone" data-id="' + str(row.id) + '/markasdone/"><i class="icon-trash"></i>Mark as Done</a></div></div></div>'
        else:
            return super(GetAllTasks, self).render_column(row, column)


    def filter_queryset(self, qs):
        search = self.request.GET.get(u'search[value]', None)
        print("Search", search)
        if search:
            qs = qs.filter(Q(name__icontains=search) | Q(is_completed__icontains=search))
            print("Query Set 0", qs)
        return qs




#This class is to Mark ask as Done
class MarkAsDone(generic.UpdateView):
    template_name= 'myproject/myapp/task_update.html'
    model = TodoTask
    fields = ['is_completed']
    status = "Mark as Done"

    def form_valid(self, form):

        print("This is Update")
        # This will make only is_completed field to be changed when update modal form is submitted
        model = form.save(commit=False)
        model.is_completed=True
        model.save()
        return HttpResponseRedirect(reverse('homepage'))

#This class is to put task in Pending State
class MarkAsPending(generic.UpdateView):
    template_name= 'myproject/myapp/task_update.html'
    model = TodoTask
    fields = ['is_completed']
    status = "Mark as Pending"

    def form_valid(self, form):

        print("This is Update")
        # This will make only is_delete field to be changed when update modal form is submitted
        model = form.save(commit=False)
        model.is_completed=False
        model.save()
        return HttpResponseRedirect(reverse('homepage'))


#This class is used to Update the Task (name)
class UpdateTask(generic.UpdateView):
    template_name= 'myproject/myapp/task_update_details.html'
    model = TodoTask
    form_class = TodoTaskForm
    success_message="Task Updated Successfully"
    success_url = reverse_lazy('homepage')


