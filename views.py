from django.shortcuts import render,redirect

from django.contrib.auth.models import User,auth


from django.contrib import messages


from django import forms
# Create your views here.	
def address(request):
    if request.method == 'POST':
        state = request.POST['state']
        street = request.POST['street']
        pincode = request.POST['pincode']
        phoneno = request.POST['phoneno']
        country = request.POST['country']
        

    return render(request,'address.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
      
        user = auth.authenticate(request,username = username,password = password)
        
        
        if user is not None :
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'invalid credentials')
            return redirect('signin')

    else:
        return render(request,'signin.html')


def register(request):
    
   
    if request.method == 'POST':
       
        username = request.POST.get('username')
        
        password = request.POST.get('password')
        
        
         
      

        
        if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')

      
        else:
           
            user = User.objects.create_user(username=username,password=password)
            user.save();
            print('user created')
            return redirect('signin')
          
    else:
        
        return render(request,'register.html')
        


        

   
 
    





