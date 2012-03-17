from django.conf import settings
from django.db.models import signals
from django.utils.translation import ugettext_noop as _


if "notification" in settings.INSTALLED_APPS:
    from notification import models as notification

    def create_notice_types(app, created_models, verbosity, **kwargs):
        notification.create_notice_type("friends_invite", _("Invitation Received"), _("you have received an invitation"), default=1)
        notification.create_notice_type("friends_invite_sent", _("Invitation Sent"), _("you have sent an invitation"), default=1)
        notification.create_notice_type("friends_accept", _("Acceptance Received"), _("an invitation you sent has been accepted"), default=1)
        notification.create_notice_type("friends_accept_sent", _("Acceptance Sent"), _("you have accepted an invitation you received"), default=1)
        # TODO: create notifiaction about friend having new friend

    signals.post_syncdb.connect(create_notice_types, sender=notification)
else:
    print "Skipping creation of NoticeTypes as notification app not found"
