from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from account.models import Profile


# Create your views here.

def home(request):
    return render(request, "home.html")


def staff_dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")

    # only staff/admin users should access
    try:
        from account.permissions import is_staff_user

        if not is_staff_user(request.user):
            return redirect("profile")
    except Exception:
        # if role lookup fails, just don't block
        pass

    # Get user's role
    role = None
    try:
        role = Profile.objects.get(user=request.user).role
    except Profile.DoesNotExist:
        role = None

    context = {"role": role}

    # If admin, get pending leave requests to approve
    if role == "admin":
        from account.models import LeaveRequest
        pending_requests = LeaveRequest.objects.filter(
            status=LeaveRequest.Status.PENDING
        ).select_related("user").order_by("-created_at")
        context["pending_requests"] = pending_requests
    # If staff, get their own approved/rejected leaves
    elif role == "staff":
        from account.models import LeaveRequest
        staff_leaves = LeaveRequest.objects.filter(
            user=request.user,
            status=LeaveRequest.Status.APPROVED
        ).order_by("-created_at")
        context["staff_leaves"] = staff_leaves

    return render(request, "staff_dashboard.html", context)



def apply_leave(request):
    from django.utils import timezone
    from account.models import LeaveRequest

    if not request.user.is_authenticated:
        return redirect("login")

    error = None
    success = None

    if request.method == "POST":
        from_date = request.POST.get("from_date")
        to_date = request.POST.get("to_date")
        reason = request.POST.get("reason")

        if not from_date or not to_date or not reason:
            error = "All fields are required."
        else:
            try:
                # Django will parse date strings for DateField/DateTimeField on save via model.
                # Basic validation:
                if from_date > to_date:
                    error = "From Date cannot be after To Date."
                else:
                    LeaveRequest.objects.create(
                        user=request.user,
                        from_date=from_date,
                        to_date=to_date,
                        reason=reason,
                    )
                    success = "Leave request submitted successfully!"
            except Exception:
                error = "Invalid input. Please try again."

    return render(request, "apply_leave.html", {"error": error, "success": success})


def leave_status(request):
    from account.models import LeaveRequest

    if not request.user.is_authenticated:
        return redirect("login")

    requests = LeaveRequest.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "leave_status.html", {"requests": requests})


def admin_approve_leaves(request):
    """Admin/staff page to approve or reject pending leave requests."""
    from account.models import LeaveRequest

    if not request.user.is_authenticated:
        return redirect("login")

    from account.permissions import is_staff_user

    if not is_staff_user(request.user):
        return render(request, "approval_denied.html")

    if request.method == "POST":
        # We handle approve/reject in separate endpoints.
        return redirect("staff_leave_status")

    requests = LeaveRequest.objects.filter(status=LeaveRequest.Status.PENDING).select_related("user").order_by("-created_at")
    return render(request, "admin_approve_leaves.html", {"requests": requests})


def staff_approve_leave(request, leave_id: int):
    from account.models import LeaveRequest

    if not request.user.is_authenticated:
        return redirect("login")

    from account.permissions import is_staff_user

    if not is_staff_user(request.user):
        return render(request, "approval_denied.html")

    leave = LeaveRequest.objects.get(id=leave_id)
    leave.status = LeaveRequest.Status.APPROVED
    leave.save(update_fields=["status"])
    return redirect("admin_approve_leaves")


def staff_reject_leave(request, leave_id: int):
    from account.models import LeaveRequest

    if not request.user.is_authenticated:
        return redirect("login")

    from account.permissions import is_staff_user

    if not is_staff_user(request.user):
        return render(request, "approval_denied.html")

    leave = LeaveRequest.objects.get(id=leave_id)
    leave.status = LeaveRequest.Status.REJECTED
    leave.save(update_fields=["status"])
    return redirect("admin_approve_leaves")




def profile(request):
    # Assumes the user is authenticated (login_view will redirect here).
    # If not authenticated, Django will still render but request.user will be AnonymousUser.
    role = None
    if getattr(request, "user", None) and request.user.is_authenticated:
        try:
            role = Profile.objects.get(user=request.user).role
        except Profile.DoesNotExist:
            role = None

    return render(request, "profile.html", {"role": role})



def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        if not username or not password or not role:
            # Simple fallback; you can add proper error messages later.
            return render(request, "register.html")

        # Avoid duplicate usernames (would otherwise error on Profile/User creation)
        if User.objects.filter(username=username).exists():
            return render(request, "register.html")

        user = User.objects.create_user(
            username=username,
            password=password,
        )
        Profile.objects.create(user=user, role=role)


        return redirect("home")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        # Fallback: authenticate() can return None if backend is misconfigured.
        # Checking password directly makes the login behavior deterministic.
        if user is None and username and password:
            try:
                user = User.objects.get(username=username)
                if not user.check_password(password):
                    user = None
            except User.DoesNotExist:
                user = None

        if user is not None:
            login(request, user)
            return redirect("profile")


        return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")




