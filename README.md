# Sprint_5

Данный проект содержит набор автоматизированных UI-тестов для учебного сервиса объявлений. Тесты написаны на **Python** c применением **Pytest** и **Selenium**:

### Регистрация пользователя (test_registration.py):
1. test_register_new_user_success - позитивный кейс создания нового аккаунта.
2. test_register_user_email_invalid_shows_error - проверка ошибки при некорректном формате email.
3. test_register_duplicate_user_shows_error - проверка уникальности: запрет регистрации на уже занятый email.

### Вход в систему (test_login.py):
4. test_login_user_success - успешный вход существующим пользователем.

### Выход из системы (test_logout.py):
5. test_logout_user_success - выход из системы.

### Создание объявления (test_create_notice.py):
6. test_create_notice_unauthorized_user_redirects_to_login - проверка прав доступа: редирект гостя на страницу входа.
7. test_create_notice_adds_to_profile - создание объявления и проверка его отображения в профиле пользователя.