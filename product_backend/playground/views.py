from django.shortcuts import render
from django.http import HttpResponse
from . import test_api
# Create your views here.
# view func takes a req and gives a response
# a basic request handler

def my_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        
        # Process the user input with Python code here
        output_GPT = test_api.output_response(user_input)
        # Return the result as a string
        result = "Result: " + output_GPT
        
        # Render the result back to the user
        return render(request, 'result.html', {'result': result})
    else:
        return render(request, 'input.html')