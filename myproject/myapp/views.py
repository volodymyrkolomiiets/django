from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from .models import Person
from .forms import PersonForm

def my_view(request):
    accurate_search = False  # Default to partial search

    form = PersonForm()

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            for k, v in form.cleaned_data.items():
                print(f"{k}: {v}")
            
            accurate_search = form.cleaned_data.pop('accurate_search')
            filter_data = {}

            for field in form.fields:
                value = form.cleaned_data.get(field)

                if value is not None:
                    if isinstance(value, str):
                        if field == 'ClientContact':
                            filter_data[field + '__icontains'] = value
                        elif field in ['FirstName', 'LastName']:
                            filter_data[field + ('__iexact' if accurate_search else '__icontains')] = value
                        else:
                            filter_data[field + '__iexact'] = value
                    else:
                        filter_data[field] = value
            filter_data.pop("ClientOwner__iexact")
            
            print(filter_data, "----------------------")

            q_objects = Q()
            for key, value in filter_data.items():
                q_objects &= Q(**{key: value})

            persons = Person.objects.filter(q_objects)
        else:
            persons = Person.objects.all()
    else:
        persons = Person.objects.all()

    items_per_page = 100
    paginator = Paginator(persons, items_per_page)

    page = request.GET.get('page', 1)

    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)

    context = {"form": form, "current_page": current_page, "accurate_search": accurate_search}
    return render(request, "personlist.html", context)

# # views.py

# from django.shortcuts import render
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.db.models import Q  # Import Q for complex queries
# from .models import Person
# from .forms import PersonForm


# # Add a flag to determine if the search should be accurate
# def my_view(request):
#     accurate_search = False  # Default to partial search

#     form = PersonForm()

#     if request.method == 'POST':
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             for k, v in form.cleaned_data.items():
#                 print(f"{k}: {v}")
#             accurate_search = form.cleaned_data.pop('accurate_search')
#             # Filter persons based on the provided form data
#             filter_data = {}
#             for field in form.fields:
#                 value = form.cleaned_data.get(field)
                
                
#                 if value is not None:
#                     # Use case-insensitive filters for string fields
#                     if isinstance(value, str):
#                         if field == 'ClientContact':
#                             # Use icontains for partial matching on ClientContact
#                             filter_data[field + '__icontains'] = value
#                         elif field in ['FirstName', 'LastName']:
#                             # Use icontains for partial matching or iexact for accurate matching
#                             filter_data[field + ('__iexact' if accurate_search else '__icontains')] = value
#                             print(filter_data, "!!!!!!!!!!!!")

#                         else:
#                             # Use case-insensitive exact match for other string fields
#                             filter_data[field + '__iexact'] = value
#                     else:
#                         filter_data[field] = value
#             print(filter_data)
#             # Use Q objects for OR queries
#             q_objects = Q()
#             for key, value in filter_data.items():
#                 q_objects |= Q(**{key: value})

#             persons = Person.objects.filter(q_objects)
#         else:
#             persons = Person.objects.all()
#     else:
#         persons = Person.objects.all()

#     # Configure the number of items per page
#     items_per_page = 100
#     paginator = Paginator(persons, items_per_page)

#     page = request.GET.get('page', 1)

#     try:
#         current_page = paginator.page(page)
#     except PageNotAnInteger:
#         current_page = paginator.page(1)
#     except EmptyPage:
#         current_page = paginator.page(paginator.num_pages)

#     context = {"form": form, "current_page": current_page, "accurate_search": accurate_search}
#     return render(request, "personlist.html", context)



# # def my_view(request):
# #     form = PersonForm()

# #     if request.method == 'POST':
# #         form = PersonForm(request.POST)
# #         if form.is_valid():
# #             # Filter persons based on the provided form data
# #             filter_data = {}
# #             for field in form.fields:
# #                 value = form.cleaned_data.get(field)
# #                 if value is not None:
# #                     # Use case-insensitive filters for string fields
# #                     if isinstance(value, str):
# #                         if field == 'ClientContact':
# #                             # Use icontains for partial matching on ClientContact
# #                             filter_data[field + '__icontains'] = value
# #                         elif field in ['FirstName', 'LastName']:
# #                             # Use icontains for partial matching on FirstName and LastName
# #                             filter_data[field + '__icontains'] = value
# #                         else:
# #                             # Use case-insensitive exact match for other string fields
# #                             filter_data[field + '__iexact'] = value
# #                     else:
# #                         filter_data[field] = value

# #             # Use Q objects for OR queries
# #             q_objects = Q()
# #             for key, value in filter_data.items():
# #                 q_objects |= Q(**{key: value})

# #             persons = Person.objects.filter(q_objects)
# #         else:
# #             persons = Person.objects.all()
# #     else:
# #         persons = Person.objects.all()

# #     # Configure the number of items per page
# #     items_per_page = 100
# #     paginator = Paginator(persons, items_per_page)

# #     page = request.GET.get('page', 1)

# #     try:
# #         current_page = paginator.page(page)
# #     except PageNotAnInteger:
# #         current_page = paginator.page(1)
# #     except EmptyPage:
# #         current_page = paginator.page(paginator.num_pages)

# #     context = {"form": form, "current_page": current_page}
# #     return render(request, "personlist.html", context)