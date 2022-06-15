from django.shortcuts import render,HttpResponse,redirect
from .models.product import Product
from .models.catagory import Catagory
from .models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
# Create your views here.
def index(request):

    cat=Catagory.get_all_cata()
    pr =None
    cata_id=request.GET.get('catagory')
    if cata_id:
        pr = Product.get_all_by_categoryid(cata_id)
    else:
        pr=Product.get_all()
    d1={}
    d1['Prod']= pr
    d1['cata']= cat
    print(request.session.get('email'))
    return render(request,'home.html',d1)





        
def feedback(request):
    return render(request,'feedback.html')

class Login(View):
    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        email = request.POST.get('email_login')
        password = request.POST.get('password_login')
        er_mess = None
        
        customer = Customer.get_email_check(email)
        if customer:
            flag = check_password(password, customer.Password)

            if flag:
                request.session['customer_id']=customer.id
                request.session['email']=customer.email_Adress
                return redirect('home')
            else:

                er_mess = 'Password INVALID'

        else:

            er_mess = 'check email'
        return render(request, 'login.html', {'error': er_mess})


class Signup(View):
    def get(self,request):
        return render(request, 'signup.html')
    def post(self,request):

        p = request.POST
        first_name = p.get('f_name')
        last_name = p.get('l_name')
        phone_number = p.get('Phone')
        email_Adress = p.get('email_Adress')
        Password = p.get('pass')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'email_Adress': email_Adress
        }

        customer = Customer(first_name=first_name, last_name=last_name, phone_number=phone_number,
                                email_Adress=email_Adress, Password=Password)
        er_mes = self.Validation(customer)

        if (not er_mes):
            customer.Password = make_password(customer.Password)
            customer.save()
            return redirect("home")




        else:
            da = {
                'error': er_mes,
                'values': value
            }
            return render(request, 'signup.html', da)

    def Validation(self,customer):
        er_mes = None

        if (not customer.first_name):
            er_mes = 'First Name Required'

        elif (not customer.last_name):
            er_mes = 'Last Name Required'


        elif (not customer.phone_number):
            er_mes = 'Phone Number Required'
        elif (len(customer.phone_number) < 10):
            er_mes = 'Please Enter Valid Phone Number'
        elif (not customer.email_Adress):
            er_mes = 'Email Required'
        elif (not customer.Password):
            er_mes = 'Password Required'
        elif customer.isExits():
            er_mes = 'Account already created by this email id'

        return er_mes
