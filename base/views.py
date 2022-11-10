from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib import messages



# from .scrapper import scrapper
# from .selenium import selenium_func
# Create your views here.


def registerPage(request):
    if request.method =='POST':
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
        messages.error(request,'Invalid username or password')

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
    return render(request,'base/home.html',context)




@csrf_exempt
def showCases(request):
    
    '''
    check if there is a post request from our scrapper and tackle the rest of the work
    '''
    sample_data = [
        {
            "Clerk_File_No": "2022 R 831976",
            "Doc_Type": "LIS",
            "Rec_Date": "11/1/2022",
            "Rec_Book_or_Page": "33447 / 92",
            "Plat_Book_or_Page": "149/220",
            'Blk': '5.0',
            'Legal': "LOT 2A",
            "Misc_Ref": "2022-020673-CA-01 LISPCV",
            "First_Party_Code": 'HSBC BANK USA NA (D)',
            "Second_Party_Code": "LARGAESPADA SILVIA"

        },
        {
            "Clerk_File_No": "2022 R 831976",
            "Doc_Type": "LIS",
            "Rec_Date": "11/1/2022",
            "Rec_Book_or_Page": "33447 / 92",
            "Plat_Book_or_Page": "149/220",
            'Blk': '5.0',
            'Legal': "LOT 2A",
            "Misc_Ref": "2022-020673-CA-01 LISPCV",
            "First_Party_Code": 'HSBC BANK USA NA (D)',
            "Second_Party_Code": "LARGAESPADA SILVIA"

        },
        {
            "Clerk_File_No": "2022 R 831976",
            "Doc_Type": "LIS",
            "Rec_Date": "11/1/2022",
            "Rec_Book_or_Page": "33447 / 92",
            "Plat_Book_or_Page": "149/220",
            'Blk': '5.0',
            'Legal': "LOT 2A",
            "Misc_Ref": "2022-020673-CA-01 LISPCV",
            "First_Party_Code": 'HSBC BANK USA NA (D)',
            "Second_Party_Code": "LARGAESPADA SILVIA"

        },
        {
            "Clerk_File_No": "2022 R 831976",
            "Doc_Type": "LIS",
            "Rec_Date": "11/1/2022",
            "Rec_Book_or_Page": "33447 / 92",
            "Plat_Book_or_Page": "149/220",
            'Blk': '5.0',
            'Legal': "LOT 2A",
            "Misc_Ref": "2022-020673-CA-01 LISPCV",
            "First_Party_Code": 'KENDALE LAKES NORTH SECTION NINE HOMEOWNERS ASSN INC (R)',
            "Second_Party_Code": "HSBC BANK USA NA"

        },
        {
            "Clerk_File_No": "2022 R 831976",
            "Doc_Type": "LIS",
            "Rec_Date": "11/1/2022",
            "Rec_Book_or_Page": "33447 / 92",
            "Plat_Book_or_Page": "149/220",
            'Blk': '5.0',
            'Legal': "LOT 2A",
            "Misc_Ref": "2022-020673-CA-01 LISPCV",
            "First_Party_Code": 'LARGAESPADA SILVIA (R)',
            "Second_Party_Code": "HSBC BANK USA NA"
        },
        {
            "Clerk_File_No": "2022 R 831982",
            "Doc_Type": "LIS",
            "Rec_Date": "11/1/2022",
            "Rec_Book_or_Page": "33447 / 101",
            "Plat_Book_or_Page": "96/110",
            'Blk': '17.0',
            'Legal': "LOT 2",
            "Misc_Ref": "2022-020677-CA-01 LISPCV",
            "First_Party_Code": 'LARGAESPADA SILVIA (R)',
            "Second_Party_Code": "HSBC BANK USA NA"
        },
        {
            "Clerk_File_No": "2022 R 831982",
            "Doc_Type": "LIS",
            "Rec_Date": "11/1/2022",
            "Rec_Book_or_Page": "33447 / 101",
            "Plat_Book_or_Page": "96/110",
            'Blk': '17.0',
            'Legal': "LOT 2",
            "Misc_Ref": "2022-020677-CA-01 LISPCV",
            "First_Party_Code": 'LARGAESPADA SILVIA (R)',
            "Second_Party_Code": "HSBC BANK USA NA"
        },
        {
            "Clerk_File_No": "2022 R 832023",
            "Doc_Type": "LIS",
            "Rec_Date": "11/1/2022",
            "Rec_Book_or_Page": "33447 / 207",
            "Plat_Book_or_Page": "89/100",
            'Blk': '2.0',
            'Legal': "LOT 2",
            "Misc_Ref": "2022-020681-CA-01 LISPCV",
            "First_Party_Code": 'LARGAESPADA SILVIA (R)',
            "Second_Party_Code": "HSBC BANK USA NA"
        },
        {
            "Clerk_File_No": "2022 R 832023",
            "Doc_Type": "LIS",
            "Rec_Date": "11/1/2022",
            "Rec_Book_or_Page": "33447 / 207",
            "Plat_Book_or_Page": "89/100",
            'Blk': '2.0',
            'Legal': "LOT 2",
            "Misc_Ref": "2022-020681-CA-01 LISPCV",
            "First_Party_Code": 'LARGAESPADA SILVIA (R)',
            "Second_Party_Code": "HSBC BANK USA NA"
        },
        {
            "Clerk_File_No": "2022 R 833199",
            "Doc_Type": "LIS",
            "Rec_Date": "11/1/2022",
            "Rec_Book_or_Page": "33447 / 3271",
            "Plat_Book_or_Page": "118/180",
            'Blk': '75.0',
            'Legal': "LOT 10",
            "Misc_Ref": "2022-020662-CA-01 LISPCV",
            "First_Party_Code": 'LARGAESPADA SILVIA (R)',
            "Second_Party_Code": "HSBC BANK USA NA"
        },
        {
            "Clerk_File_No": "2022 R 833199",
            "Doc_Type": "LIS",
            "Rec_Date": "11/1/2022",
            "Rec_Book_or_Page": "33447 / 3271",
            "Plat_Book_or_Page": "118/180",
            'Blk': '75.0',
            'Legal': "LOT 10",
            "Misc_Ref": "2022-020662-CA-01 LISPCV",
            "First_Party_Code": 'LARGAESPADA SILVIA (R)',
            "Second_Party_Code": "HSBC BANK USA NA"
        },
    ]


    if request.method == 'POST':
        data= request.POST
       
    context= dict(data=sample_data)

    return render(request,'base/showCases.html',context)