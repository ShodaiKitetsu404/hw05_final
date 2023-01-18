from django.shortcuts import render
from http import HTTPStatus


def csrf_failure(request, reason=""):
    return render(
        request,
        template_name="core/403csrf.html"
    )


def page_not_found(request, exception):
    return render(
        request,
        template_name="core/404.html",
        context={"path": request.path},
        status=HTTPStatus.NOT_FOUND,
    )


def permission_denied(request, reason=""):
    return render(
        request,
        template_name="core/403.html",
        status=HTTPStatus.FORBIDDEN
    )


def server_error(request):
    return render(
        request,
        "core/500.html",
        status=HTTPStatus.INTERNAL_SERVER_ERROR
    )
