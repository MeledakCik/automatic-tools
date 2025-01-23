url_share_data = '/api/v1/web/data/shared_data/' + headers + cookie + data
url_one_tap = '/api/v1/web/accounts/one_tap_web_login/'+ headers + body + cookie
url_send_email = '/api/v1/web/accounts/send_account_recovery_email_ajax/' + query + header
url_login = '/api/v1/web/accounts/login/ajax/' +data + headers + body
url_create = "/api/v1/web/accounts/web_create_ajax/attempt/" / "/api/v1/web/accounts/web_create_ajax/" + dataa + headers
url_verif = '/api/v1/accounts/send_verify_email/' + header + query
url_code_confirm ='/api/v1/accounts/check_confirmation_code/' + data + header


dataa_body_create = {
    'captcha': 'captcha',
    'day': 'day',
    'email': 'f',
    'failed_birthday_year_count': 'failedBirthdayYearCount',
    'first_name': 'fullNameFirst',
    'month': 'month',
    'phone_number': 'phoneNumber',
    'subno_key': 'subnoKey',
    'username': 'username',
    'year': 'year'
}
data_create = 'smsCode','clientId','seamlessLoginEnabled','gdpr_s','tosVersion','phoneId','optIntoOneTap','fbToken','emailSignupCode','failedBirthdayYearCount'
body_one_tap = {
    'login_nonce': 'b',
    'queryParams': 'c',
    'trustedDeviceRecords': 'e',
    'user_id': 'a',
}
data_login = {
    'caaF2DebugGroup': 'j',
    'loginAttemptSubmissionCount': 'i',
    'optIntoOneTap': 'f',
    'queryParams': 'e',
    'stopDeletionNonce': 'g',
    'trustedDeviceRecords': 'h',
    'username': 'a'
}