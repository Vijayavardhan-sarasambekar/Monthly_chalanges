from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# declaring variable
monthly_challenges={
    "january":"walk 20 min Every day",
    "february":"learn Django for 20min every day",
    "march":"practice communication Skill",
    "april":"do meditation for 10 min for Every morning",
    "may":"walk 20 min Every day",
    "june":"practice communication Skill",
    "july":"walk 20 min Every day",
    "august":"learn Django for 20min every day",
    "october":"",
    "november":"",
    "December":"Have Fun"
}

def index(request):
    # response_data="""
    #     <ul>
    #     <li><a href="/challenges/january">January</a></li>
    #     <li><a href="/challenges/february">february</a></li>
    #     </ul>
    #     """
    # return HttpResponse(response_data)
    list_items=""
    months=list(monthly_challenges.keys())

    for month in months:
        capitalize_month=month.capitalize()
        path=reverse("month_challenge",args=[month])
        list_items += f"<li><a href=\"{path}\">{capitalize_month}</a></li>"  #<li>...</li><li>.....</li>
        final_response=f"<ul>{list_items}</ul>"

    return HttpResponse(final_response)



# for number
def monthly_challenge_number(request,month):
    # use key() in dict
    months=list(monthly_challenges.keys())

    if month > len(months):
      return HttpResponseNotFound("Invalid Month")
    
    redirect_month=months[month - 1]
    redirect_path=reverse("month_challenge",args=[redirect_month])#/challenge/january
    # return HttpResponseRedirect("/challenges/"+redirect_month)   redicting without using reverse method
    
    return HttpResponseRedirect(redirect_path)
    

# for string
def monthly_challenge(request,month):
    try:
        challenge_text=monthly_challenges[month]
        # Returning HTML
        response_data=f"<h1>{challenge_text}</h1>" #f -> f-string
        return HttpResponse(response_data)
    except:
        HttpResponse("This month not found")
    