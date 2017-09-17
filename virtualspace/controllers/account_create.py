from virtualspace.models import Account


class AccountCreateController:
    model = Account

    @classmethod
    def create_account(cls, sa_session, username, password, email):
        account = cls.model(username=username, password=password, email=email)
        # TODO: Validate
        sa_session.add(account)
        sa_session.commit()
