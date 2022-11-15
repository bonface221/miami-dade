from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserForm
from django.contrib import messages
from . models import OfficialSearch, Parties, Dockets, Case
from datetime import date


# from .scrapper import scrapper
# from .selenium import selenium_func
# Create your views here.


def registerPage(request):
    # check if user is authenticated if yes redirect the user to homepage
    if request.user.is_authenticated:
        return redirect('home')

    # check for post requests and authenticate the user and redirect to login
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username.lower()
            user.save()
            return redirect('login')

        messages.error(request, form.errors)

    context = dict()
    return render(request, 'base/registration/register.html', context)


def loginPage(request):
    # check if user is authenticated if yes redirect to home
    if request.user.is_authenticated:
        return redirect('home')

    # check for post requests and authenticate the user
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username').lower()
            password = request.POST.get('password')

            try:
                user = User.objects.get(username)

            except:
                messages.error(request, "User does not exist.")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            messages.error(request, "Invalid username or password.")
        messages.error(request, 'Invalid username or password')

    context = dict()
    return render(request, 'base/registration/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def homePage(request):
    '''
    this is the homepage section
    '''
    context = dict()
    return render(request, 'base/home.html', context)


@csrf_exempt
def showCases(request):
    '''
    check if there is a post request from our scrapper and tackle the rest of the work
    '''

    if request.method == 'POST':

        uncleaned_data = request.POST
        data = uncleaned_data.dict()
        if type(data) is dict:

            # format the date in a format that is consistent with the db
            splitted_date = data['Rec Date'].split('/')
            date_obj = date(int(splitted_date[2]),
                            int(splitted_date[1]), int(splitted_date[0]))

            # splitting the first party code and second to make them in a format that lets them be saved in the db
            splitted_parties = data['First Party (Code)  Second Party (Code)'].split(
                '  ')

            # check if the object already exist if yes do nothing if there is an exeption like the case is not found then the 
            # case is new => create it
            try:
                OfficialSearch.objects.get(Clerks_File_No=data["Clerk's File No"], First_Party_Code=splitted_date[0],
                                           Second_Party_Code=splitted_date[1], Rec_Book_or_Page=data['Rec Book/Page'], Misc_Ref=data['Misc Ref'])

            except ObjectDoesNotExist:
                OfficialSearch.objects.create(
                    Clerks_File_No=data["Clerk's File No"], Doc_Type=data["Doc Type"], Rec_Date=date_obj, Rec_Book_or_Page=data['Rec Book/Page'], Plat_Book_or_Page=data['Plat Book/Page'], Blk=data['Blk'], Legal=data['Legal'], Misc_Ref=data['Misc Ref'], First_Party_Code=splitted_parties[0], Second_Party_Code=splitted_parties[1])

    # pull data from db and order by the recorded date
    data_from_db = OfficialSearch.objects.all().order_by('-Rec_Date').distinct()

    # count the number of items availble
    total_count=''
    if data_from_db:
        total_count = data_from_db.count()
    context = dict(data=data_from_db, total_count=total_count)

    return render(request, 'base/showCases.html', context)


@csrf_exempt
def advancedSearch(request):

    # check whether the incoming request is post
    if request.method == "POST":
        uncleaned_data = request.POST
        # use the dict function to get the dictionary representation
        data = uncleaned_data.dict()
        # print(data)
        if type(data) is dict:
            # check if case number is available
            # if yes create it because there is only one case number

            if 'case_number' in data:
                Case.objects.create(
                    local_case_number=data['case_number'], state_number=data['state_number'], case_type=data['case_type'])

            # check for parties 
            if 'Party Description' in data:
                # print('parties', data)
                try:
                    # check if the parties are already saved to avoid duplicates
                    Parties.objects.get(
                        party_description=data['Party Description'], party_name=data['Party Name'], attorney_information=data['Attorney Information'])
                    # if does not exist create it
                except ObjectDoesNotExist:
                    Parties.objects.create(
                        party_description=data['Party Description'], party_name=data[
                            'Party Name'], attorney_information=data['Attorney Information'], attorney_name='',local_case_number = data['local_case_number']
                    )
                    

            # check for the dockets
            if 'Docket Entry' in data:
                # print('dockets', data)
                # check if docket is saved
                try:
                    Dockets.objects.get(
                        event_date=data['Date'], book_page=data['Book/Page'], docket_entry=data['Docket Entry'], event_type=data['Event Type'], comments='Comments'
                    )
                # if docket does not exist create it
                except ObjectDoesNotExist:
                    Dockets.objects.create(
                        event_date=data['Date'], docket_number=float(data['Number']), book_page=data[
                            'Book/Page'], docket_entry=data['Docket Entry'], event_type=data['Event Type'], comments=data['Comments']
                    )
                    
            
            
    
    # get all the parties
    parties = Parties.objects.all()

    # get all the dockets
    dockets = Dockets.objects.all()

    # use of context to create a dictionary to be sent to the template
    context = dict(parties=parties,dockets=dockets)

    return render(request, 'base/advanced_records.html', context)
