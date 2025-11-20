from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def home_redirect(request):
    if request.user.role == "admin":
        return redirect("/api/users/")
    else:
        return redirect("/api/user-dashboard/")  # dashboard for agents/customers
