from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# view func takes a req and gives a response
# a basic request handler

def my_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        
        # Process the user input with Python code here
        
        # Return the result as a string
        result = "Result: " + user_input.upper()
        
        # Render the result back to the user
        return render(request, 'result.html', {'result': result})
    else:
        return render(request, 'input.html')