import authentication._views.system_admin as system_admin_views
import authentication._views.driver as driver_views
import authentication._views.passenger as passenger_views
import authentication._views.fleet_manager as fleet_manager_views
import authentication._views.account_views as account_views


# Create your views here.


# Account Views
SendVerificationLinkView = account_views.SendVerificationLinkView
VerifyEmailView = account_views.VerifyEmailView
UserLoginView = account_views.UserLoginView
PasswordResetView = account_views.PasswordResetView
PasswordResetConfirmView = account_views.PasswordResetConfirmView
