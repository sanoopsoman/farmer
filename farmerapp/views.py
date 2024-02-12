
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, 'index.html')


def farmerregister(request):
    if request.POST:
        name = request.POST['Uname']
        email = request.POST['email']
        gender = request.POST['gender']
        mob = request.POST['mob']
        password = request.POST['password']
        address = request.POST['address']
        img = request.FILES['img']
        if Farmer.objects.filter(email=email).exists():
            messages.info(request, "email already exists")
        else:
            farmer = Login.objects.create_user(
                username=email, password=password, usertype='farmer', ViewPassword=password, is_active=1)
            farmer.save()
            register = Farmer.objects.create(
                name=name, email=email, img=img, mob=mob, farmer=farmer, gender=gender, address=address)
            register.save()
            messages.info(request, "registration successfull")
            return redirect("/login")

    return render(request, 'farmer/farmerregister.html')


def farmtechregister(request):
    if request.POST:
        name = request.POST['Uname']
        email = request.POST['email']
        gender = request.POST['gender']
        mob = request.POST['mob']
        password = request.POST['password']
        img = request.FILES['img']
        if Farmer.objects.filter(email=email).exists():
            messages.info(request, "email already exists")
        else:
            farm = Login.objects.create_user(
                username=email, password=password, usertype='farmtech', ViewPassword=password, is_active=1)
            farm.save()
            register = Farmtech.objects.create(
                name=name, email=email, img=img, mob=mob, farm=farm, gender=gender)
            register.save()
            messages.info(request, "registration successfull")
            return redirect("/login")
    return render(request, 'farmtech/farmtechregister.html')


def login(request):

    # print("test")
    if request.POST:

        email = request.POST["email"]
        password = request.POST["password"]
        # print(email, password,"test")
        user = authenticate(username=email, password=password)
        # print("trxdetxtrx",user)
        if user is not None:
            if user.usertype == "admin":
                messages.info(request, "welocme to  page admin")
                return redirect('/admin1')

            elif user.usertype == "farmer":
                print(user.usertype)
                request.session['uid'] = user.id
                messages.info(request, "welcome to farmer page")
                return redirect('/farmer')

            elif user.usertype == "farmtech":
                request.session['uid'] = user.id
                messages.info(request, "welcome to farmtech page")
                print(user.usertype)
                return redirect('/farmtech')
            else:
                messages.info(request, "invalid login")
        else:
            # messages.info(request, "User Not Approved")
            print("Type Not Get")

    return render(request, 'login.html')


def farmer(request):
    return render(request, 'farmer/farmer.html')


def farmtech(request):
    return render(request, 'farmtech/farmtech.html')



def admin1(request):
    return render(request, 'admin/admin.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def addproducts(request):
    cid=request.GET.get('cid')
    Cid=Category.objects.get(id=cid)
    
    uid=request.session['uid']
    farmer=Farmer.objects.filter(farmer=uid)
    id=Farmer.objects.get(farmer=uid)
    category=Category.objects.all()
    if request.POST:
        name=request.POST['name']
        quantity=request.POST['quantity']
        img=request.FILES['img']
        price=request.POST['price']
        product=Products.objects.create(name=name, quantity=quantity, price=price, category=Cid, fid=id, img=img)
        product.save()
        return redirect('/viewcategory')
    return render(request, 'farmer/addproducts.html',{'category':category, 'farmer':farmer})

def applyloan(request):
    id=request.GET.get('id')
    tid=Farmtech.objects.get(farm__id=id)
    print("ekjc",tid.farm_id)
    tech=Farmtech.objects.filter(farm=id)
    uid=request.session['uid']
    fam=Farmer.objects.filter(farmer=uid)
    fid=Farmer.objects.get(farmer=uid)
    if request.POST:
       
        purpose=request.POST['purpose']
        amount=request.POST['amount']
      
        loan=Loan.objects.create(techid=tid, amount=amount, purpose=purpose, fid=fid)
        loan.save()
        
    
    return render(request,'farmer/applyloan.html',{'fam':fam,'tech':tech})

def addcategory(request):
    uid=request.session['uid']
    fam=Farmer.objects.filter(farmer=uid)
    id=Farmer.objects.get(farmer=uid)
    if request.POST:
        categoryname=request.POST['cname']
        img=request.FILES['img']
        category=Category.objects.create(name=categoryname,img=img,farmername=id)
        category.save()
        return redirect('/viewcategory')
    return render(request, 'farmer/addcategory.html',{'fam':fam})

def viewcategory(request):
    category=Category.objects.all()
    return render(request, 'farmer/viewcategory.html',{'category':category})


def deleteproducts(request):
    cid=request.GET.get('cid')
    product=Products.objects.filter(id=cid)
    product.delete()
    messages.info(request,"product deleted")
    return redirect('/farmtechviewloan')
    
def viewproducts(request):
    cid=request.GET['cid']
    product=Products.objects.filter(category=cid)
    return render(request, 'farmer/viewproducts.html',{'product':product})

def deletecategory(request):
    cid=request.GET['cid']
    category=Category.objects.filter(id=cid)
    category.delete()
    messages.info(request,"category deleted")
    return redirect('/viewvehiclerent')
    
def updateproducts(request):
    
    id = request.GET['id']
    update = Products.objects.filter(id=id)
    if request.POST:
        if 'img' in request.FILES:
            img=request.FILES['img']
        else:
            img=update[0].img
        name = request.POST.get("name")
        img = request.FILES["img"]
        quantity=request.POST.get("quantity")
        price=request.POST.get("price")

        updatedata = Products.objects.get(id=id)
        updatedata.img = img
        updatedata.price=price
        updatedata.quantity=quantity
        updatedata.name=name
        update.save()
        messages.info(request,"product updated successfuly")
        return redirect('/')
    return render(request,'farmer/updateproducts.html',{'update':update})

def farmtechviewcategory(request):
    category=Category.objects.all()
    return render(request,'farmtech/viewcategory.html',{'category':category})

def farmtechviewproducts(request):
    cid=request.GET.get('cid')
    products=Products.objects.filter(category=cid)
    return render(request,'farmtech/viewproducts.html',{'products':products})


def actionproducts(request):
    status=request.GET['status']
    id=request.GET['id']
    product=Products.objects.get(id=id)
    product.status=int(status)
    product.save()
    if status == "1":
        messages.info(request,"approved sell")
    else:
        messages.info(request,"rejected your sell")
    return redirect('/farmtechviewcategory')


def adminviewfarmer(request):
    farmer=Farmer.objects.all()
    return render(request,'admin/viewfarmer.html',{'farmer':farmer})
    
def admindeletefarmer(request):
    id=request.GET['id']
    farmer=Farmer.objects.filter(id=id)
    farmer.delete()
    messages.info(request,"farmer deleted")
    return redirect('/adminviewfarmer')


def adminviewfarmtech(request):
    farmtech=Farmtech.objects.all()
    return render(request,'admin/viewfarmtech.html',{'farmtech':farmtech})

def admindeletefarmtech(request):
    id=request.GET['id']
    farm=Farmtech.objects.filter(id=id)
    farm.delete()
    messages.info(request,"farmtech deleted")
    return redirect('/adminviewfarmtech')


def feedback(request):
    uid=request.session['uid']
    farmer=Farmer.objects.filter(farmer=uid)
    id=Farmer.objects.get(farmer=uid)
    if request.POST:
        content=request.POST['content']
        rating=request.POST['rate']
        feedback=Feedback.objects.create(fid=id, content=content, rating=rating)
        feedback.save()
        messages.info(request,"thankyou for feedback")
        return redirect('/farmer')
    return render(request,'farmer/feedback.html',{'farmer':farmer})

def admin_feedback(request):
    feed=Feedback.objects.all()
    return render(request,'admin/feedback.html',{'feed':feed})

def farmerviewfarmtech(request):
    farm=Farmtech.objects.all()
    return render(request,'farmer/viewfarmtech.html',{'farm':farm})

def farmtechviewloan(request):
    uid=request.session['uid']
    Uid=Farmtech.objects.get(farm=uid)
    # print(uid)
    id=Farmtech.objects.filter(farm_id=uid)
    farm=Loan.objects.filter(techid=Uid)   
    # print(farm) 
    return render(request,'farmtech/viewloans.html',{'farm':farm})

def addrent(request):
    return render(request,'farmtech/rent.html')
def addvehicle(request):
    uid=request.session['uid']
    # print(uid)
    fam=Farmtech.objects.filter(farm=uid)
    farm=Farmtech.objects.get(farm__id=uid)
    print(farm,"djhgasddsdjk")
    if request.POST:
        type=request.POST['vname']
        amount=request.POST['amount']
        img=request.FILES['img']
        duration=request.POST['duration']
        vehicle=Vehicle.objects.create(type=type, amount=amount, img=img, duration=duration, techid=farm)
        vehicle.save()
        messages.info(request,"added succesfully")
        return redirect('/addrent')
        
        
    return render(request,'farmtech/addvehicle.html',{'fam':fam})

def addland(request):
    uid=request.session['uid']
    print(uid)
    fam=Farmtech.objects.filter(farm=uid)
    farm=Farmtech.objects.get(farm=uid)
    if request.POST:
        area=request.POST['area']
        amount=request.POST['amount']
        img=request.FILES['img']
        duration=request.POST['duration']
        land=Lands.objects.create(area=area, amount=amount, img=img, duration=duration, techid=farm)
        land.save()
        messages.info(request,"added succesfully")
        return redirect('/addrent')
    return render(request,'farmtech/addland.html',{'fam':fam})

def viewvehiclerent(request):
    uid=request.session['uid']
    Uid=Farmtech.objects.get(farm=uid)
    farm=Vehicle.objects.filter(techid=Uid) 
    print(uid)
    vehicle=Vehicle.objects.filter(techid=uid)
    return render(request,'farmtech/viewvehiclerent.html',{'farm':farm})


def actionloans(request):
    status=request.GET['status']
    id=request.GET['id']
    loan=Loan.objects.get(id=id)
    loan.status=int(status)
    loan.save()
    if status == "1":
        messages.info(request,"approved approved")
    else:
        messages.info(request,"rejected your loan")
    return redirect('/farmtechviewloan')


def deleteloans(request):
    lid=request.GET.get('lid')
    loan=Loan.objects.filter(id=lid)
    loan.delete()
    messages.info(request,"deleted")
    return redirect('/farmtechviewloan')

def deletevehicle(request):
    vid=request.GET.get('vid')
    vehicle=Vehicle.objects.filter(id=vid)
    vehicle.delete()
    messages.info(request,"vehicle deleted successfully")
    return redirect('/viewvehiclerent')

def updatevehicle(request):
    uid=request.session['uid']
    Uid=Farmtech.objects.get(farm=uid)
    farm=Vehicle.objects.filter(techid=Uid) 
    vid = request.GET['vid']
    update = Vehicle.objects.filter(id=vid)
    if request.POST:
        if 'img' in request.FILES:
            img=request.FILES['img']
        else:
            img=update[0].img
        name = request.POST.get("vname")
        img = request.FILES["img"]
        duration=request.POST.get("duration")
        amount=request.POST.get("amount") 

        updatedata = Vehicle.objects.get(id=vid)
        updatedata.img = img
      
        updatedata.duration=duration
        updatedata.type=name
        updatedata.amount=amount
        update.save()
        messages.info(request," update vehicle successfuly")
        return redirect('/')
    return render(request,'farmtech/updatevehicle.html',{'update':update})

    
def viewlandrent(request):
    uid=request.session['uid']
    Uid=Farmtech.objects.get(farm=uid)
    farm=Lands.objects.filter(techid=Uid) 
    print(uid)
    vehicle=Lands.objects.filter(techid=uid)
    return render(request,'farmtech/viewland.html',{'farm':farm})
    
def deleteland(request):
    lid=request.GET.get('lid')
    land=Lands.objects.filter(id=lid)
    land.delete()
    messages.info(request,"land deleted successfully")
    return redirect('/viewlandrent')


def updateland(request):
    uid=request.session['uid']
    Uid=Farmtech.objects.get(farm=uid)
    farm=Lands.objects.filter(techid=Uid) 
    lid = request.GET['lid']
    update = Lands.objects.filter(id=lid)
    if request.POST:
        if 'img' in request.FILES:
            img=request.FILES['img']
        else:
            img=update[0].img
        area = request.POST.get("area")
        img = request.FILES["img"]
        duration=request.POST.get("duration")
        amount=request.POST.get("amount")

        updatedata = Lands.objects.get(id=lid)
        updatedata.img = img
      
        updatedata.duration=duration
        updatedata.area=area
        updatedata.amount=amount
        update.save()
        messages.info(request," update land successfuly")
        return redirect('/viewlandrent')
    return render(request,'farmtech/updateland.html',{'update':update})

def rent(request):
    farm=Farmtech.objects.all()
    return render(request,'farmer/rent.html',{'farm':farm})

def farmerviewvehicle(request):
    id=request.GET.get('id')
    uid=request.session['uid']
    Uid=Farmtech.objects.get(farm=id)
    farm=Vehicle.objects.filter(techid=Uid,status=0) 
    book=Bookvehiclerent.objects.filter(techid=uid)
    vehicle=Vehicle.objects.filter(techid=uid)
    return render(request,'farmer/viewvehicle.html',{'farm':farm,'book':book})

def bookrent(request):
    fid=request.GET.get('fid')
    vid=request.GET.get('vid')
    
    tid=Vehicle.objects.get(id=vid)
    print(tid.id)
    
    Uid=Farmtech.objects.get(id=fid)
    farm=Vehicle.objects.filter(techid=Uid) 
    # tec=Vehicle.objects.get(techid=Uid)
    # print(tec,"trdyug")
    vehicle=Vehicle.objects.filter(id=vid)
    # Vid=Vehicle.objects.get(id=vid)

    uid=request.session['uid']
    fam=Farmer.objects.get(farmer=uid)
    update = Vehicle.objects.filter(id=vid)
    
    if request.POST:
        
        startdate=request.POST['startdate']
        enddate=request.POST['enddate']
        amount=request.POST['amount']
        
        startdate = datetime.strptime(startdate, '%Y-%m-%d')
        enddate = datetime.strptime(enddate, '%Y-%m-%d')
        date = (enddate - startdate).days
        
        # date = enddate - startdate
        print(date)

        price=int(date) * int(amount)
        print(price)
        rent=Bookvehiclerent.objects.create(totalamount=price,startingdate=startdate,endingdate=enddate,techid=Uid,fid=fam, vid=tid)
        rent.save()
        data=Vehicle.objects.filter(id=vid).update(status="1")
        
        messages.info(request,"welcome to payment page")
        
        return redirect(f'/vehiclepayment?rid={rent.id}')
        
    
    
    return render(request,'farmer/bookrent.html',{'vehicle':vehicle})




def farmerviewland(request):
    id=request.GET.get('id')
    uid=request.session['uid']
    Uid=Farmtech.objects.get(farm=id)
    farm=Lands.objects.filter(techid=Uid,status=0) 
    vehicle=Lands.objects.filter(techid=uid)
    return render(request,'farmer/viewland.html',{'farm':farm})

def actionland(request):
    status=request.GET['status']
    id=request.GET['id']
    land=Lands.objects.get(id=id)
    land.status=int(status)
    land.save()
    if status == "1":
        messages.info(request,"successfully take rent")
    else:
        messages.info(request,"not take rent")
    return redirect('farmer/viewland.html')

def actionvehicle(request):
    status=request.GET['status']
    id=request.GET['id']
    vehicle=Vehicle.objects.get(id=id)
    vehicle.status=int(status)
    vehicle.save()
    if status == "1":
        messages.info(request,"successfully take rent")
    else:
        messages.info(request,"not take rent")
    return redirect('farmer/viewvehicle.html')



def booklandrent(request):
    fid=request.GET.get('fid')
    lid=request.GET.get('lid')
    tid=Lands.objects.get(id=lid)
    Uid=Farmtech.objects.get(id=fid)
    farm=Lands.objects.filter(techid=Uid) 
    vehicle=Lands.objects.filter(id=lid)

    uid=request.session['uid']
    fam=Farmer.objects.get(farmer=uid)
    
    
    if request.POST:
        startdate=request.POST['startdate']
        enddate=request.POST['enddate']
        amount=request.POST['amount']
        startdate = datetime.strptime(startdate, '%Y-%m-%d')
        enddate = datetime.strptime(enddate, '%Y-%m-%d')
        date = (enddate - startdate).days
        
        # date = enddate - startdate
        print(date)

        price=int(date) * int(amount)
        rent=Booklandrent.objects.create(totalamount=price,startingdate=startdate,endingdate=enddate,techid=Uid,fid=fam, lid=tid)
        rent.save()
        data=Lands.objects.filter(id=lid).update(status="1")
  
        messages.info(request,"book land rent successfully")
        return redirect(f'/landpayment?lid={rent.id}')
        
    
    
    return render(request,'farmer/booklandrent.html',{'vehicle':vehicle})

def bookedrent(request):
    uid=request.session['uid']
    Uid=Farmer.objects.get(farmer=uid)
    vehicle=Bookvehiclerent.objects.filter(fid=Uid)
    land=Booklandrent.objects.filter(fid=Uid)
      
    return render(request,'farmer/bookedrent.html',{'vehicle':vehicle,'land':land})

def deletevehicle(request):
    vid=request.GET.get('vid')
    if request.GET:
        data=Vehicle.objects.filter(id=vid).update(status=0)
        messages.info(request,"vehicle deleted successfully")
        return redirect('/bookedrent')

def deleteland(request):
    lid=request.GET.get('lid')
    Lid=Lands.objects.get(id=lid)
    if request.GET:
        # land=Booklandrent.objects.filter(id=lid)
        # land.delete()
        data=Lands.objects.filter(id=lid).update(status=0)
        messages.info(request,"land deleted successfully")
        
        return redirect('/bookedrent')

def delete(request):
    
    a=Vehicle.objects.all()
    a.delete()
    b=Lands.objects.all()
    b.delete()
    
def landpayment(request):
    lid=request.GET.get('lid')
    land=Booklandrent.objects.filter(id=lid)
    if request.POST:   
        
        return redirect('/bookedrent')
    return render(request, 'farmer/landpayment.html',{'land':land})

def vehiclepayment(request):
    vid=request.GET.get('rid')
    vehicle=Bookvehiclerent.objects.filter(id=vid)
    if request.POST:
        messages.info(request,"payment successfull")
        return redirect('/bookedrent')
    return render(request,'farmer/vehiclepayment.html',{'vehicle':vehicle})





# from django.db import transaction


# @transaction.atomic
# def deleteland(request, lid):
#     lid=request.GET.get('lid')
#     try:
#         # Delete data from YourModel1
#         Booklandrent.objects.filter(id=lid).delete()

#         # Update the status of YourModel2
#         Lands.objects.filter(id=lid).update(status="0")

#         messages.success(request, "Data deleted successfully.")
#     except Exception as e:
#         messages.error(request, f"An error occurred: {str(e)}")

#     return redirect('/rent')
