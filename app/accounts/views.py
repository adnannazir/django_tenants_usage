from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from tenant_users.tenants.models import ExistsError
from tenant_users.tenants.tasks import provision_tenant

from .forms import CustomerForm, LoginForm, TenantForm
from .models import Customer, User, Domain


# Create your views here.

def get_rag_status_counts():
    green_count = 2
    yellow_count = 4
    red_count = 5
    return green_count, yellow_count, red_count


@login_required
def home(request):
    customers = Customer.objects.all()
    green_count, yellow_count, red_count = get_rag_status_counts()
    print(Domain.objects.all())
    context = {
        'user_obs': '',
        'customers': customers,
        'green_count': green_count,
        'yellow_count': yellow_count,
        'red_count': red_count,

        'parent': '',
        'segment': 'dashboard'
    }
    return render(request, 'home.html', context)


# Create your views here.

@login_required
def customers_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers_list.html', {'customers': customers, 'segment': 'accounts:customers_list'})


@login_required
def create_customer(request):
    try:
        if request.method == 'POST':
            form = TenantForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                # Create user
                user = User.objects.create_user(email=data['user_email'], password=data['password'], is_staff=True)
                # Provision tenant
                provision_tenant(data['name'], data['code'], data['user_email'], tenant_extra_data={"code": data['code']})
                # Redirect or render success page
                return redirect('accounts:customers_list')
        else:
            form = TenantForm()
    except ExistsError as e:
        # Handle the specific ExistsError exception
        messages.error(request, 'User already exists. Please use a different email address.')

    except Exception as e:
        # Log the exception for debugging purposes
        print(f"An error occurred: {str(e)}")
        # Display a generic error message
        messages.error(request, 'An error occurred while processing your request. Please try again later.')

    return render(request, 'customer_form.html', {'form': form})


@login_required
def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('accounts:customers_list')  # Redirect to customers list
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer_form.html', {'form': form, 'customer': customer})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:home')  # Redirect to home or any desired URL after login
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout_view(request):
    logout(request)
    return redirect('accounts:login')
