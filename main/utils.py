from datetime import datetime


def get_last_login(request):
    # Cookie 'last_login' hanya ada di browser session, sedangkan session Django bertahan 2 minggu.
    # Jangan sampai halaman error 500 hanya karena cookie-nya sudah hilang.
    last_login = request.COOKIES.get('last_login')
    if last_login:
        try:
            parsed_date_time = datetime.strptime(last_login, '%Y-%m-%d %H:%M:%S.%f')
            return parsed_date_time.strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
            pass

    if request.user.is_authenticated and request.user.last_login:
        return request.user.last_login.strftime('%Y-%m-%d %H:%M:%S')
    return ""
