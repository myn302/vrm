from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from .models import Item,Buyer,Delivery, Payment,Seller
import json
from datetime import date

def index(request):
    product=Item.objects.all()
    noOfProducts=len(product)
    params={'product':product, 'range': range (noOfProducts)}
    return render (request,'index.html',params)

def singleProductPage(request, id):
    product=Item.objects.filter(id=id)
    print(product)
    return  render (request,'productpage.html', {'product':product[0]})

def searchMatch(query,item):
     if query!="":
        Query=query[0].upper()+query[1:]  
        if query in str(item.productName ).lower() or  query in str(item.productType).lower() or query in str(item.description).lower() \
        or query in str(item.productName ).upper() or  query in str(item.productType).upper() or query in str(item.description).upper()\
            or Query in str(item.productName ) or  Query in str(item.productType) or Query in str(item.description):
            return True
        else:
            return False

def search(request):
    query=request.GET.get('search')
    prod=Item.objects.all()
    msg=''
    product=[item for item in prod if searchMatch(query,item) ]
    noOfProducts=len(product)
    if noOfProducts==0 or query=="":
        product=Item.objects.all()
        msg='Please make sure to enter relevant search query'
    params={'product':product, 'range': range (noOfProducts),'msg':msg}

    return render (request,'search.html',params)




def refundRequest(request):
     return render (request,'refundRequest.html')

def handleLogin(request):
    admin=Seller.objects.all()
   
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        for item in admin:
            print(item.username,"==")
            print(item.password,"==")
            if item.username == loginusername and item.password== loginpassword:
                return redirect("/admin")             

        user=authenticate(request, username= loginusername, password= loginpassword)
        print(user)
        print(user is not None)
        if user is not None:
            login(request, user)
            print(loginusername)
            print(loginpassword)
            messages.success(request, "Successfully Logged In")
            return redirect("MyShop")
        else:
            print(loginpassword)
            messages.warning(request, "Invalid credentials! Please try again")
            return redirect("MyShop")

    return HttpResponse("404- Not found")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('MyShop')


def handleSignUp(request):
    if request.method=="POST":

        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        phone=request.POST['phonesignup']
        address=request.POST['addresssignup']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if not username.isalnum():
            messages.warning(request, " User name should only contain letters and numbers")
            return redirect('MyShop')
        if (pass1!= pass2):
             messages.warning(request, " Passwords do not match")
             return redirect('MyShop')
        buyer = Buyer(itemsJson='', name=fname+lname, username=username, email=email, address=address, phone=phone, payment='0', password=pass1)
        buyer.save()
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name=lname
        myuser.email= email
        myuser.username= username
        myuser.set_password(pass1)
       
        myuser.save()
        
        messages.success(request, " Your account has been successfully created")
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")


def checkout(request):
    product=Item.objects.all()
    buyers=Buyer.objects.all()
    print( request.method)
    if request.method=="POST":
        itemsJson=request.POST.get('itemsJson', '')
        name = request.POST.get('firstName', '')+' '+ request.POST.get('lastName', '')
        username = request.POST.get('checkoutusername', '')
        email = request.POST.get('checkoutemail', '')
        address = request.POST.get('address', '') + " " + request.POST.get('address2', '')+ " " + request.POST.get('country', '')+ " " + request.POST.get('city', '')+ " " + request.POST.get('zip', '')
        phone = request.POST.get('phone', '')
        cardnumber = request.POST.get('cc-number', '')
        
        data  = json.loads(itemsJson)
        
        price=0
        for item in data:
            price+=data[item][2]

        for buyer in buyers:
            print(buyer.username,"==")
            print(buyer.password,"==")
            if buyer.username == username and buyer.email== email and buyer.phone== phone:
                buyer.payment+=price
            else:   
                buyer = Buyer(itemsJson=itemsJson, name=name, username=username, email=email, address=address, phone=phone, payment=price, password='2')
        id=buyer.buyerID
        today = date.today()
        delivery=Delivery(buyerID=id,name=name,date=today,address=address)
        delivery.save()
        
        did=delivery.deliveryID
        payment=Payment(deliveryID=did, cardNumber=cardnumber, amount=price  )
        payment.save()


        buyer.save()
        thank=True
        return render(request, 'checkout.html', {'thank':thank, 'id':id})
    
    return render (request,'checkout.html',{'product':product})

def orderSuccess(request):
    return render (request,'orderPlaced.html')