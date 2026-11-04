class EmailValidator:

    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain: str) -> bool:
        return domain in self.domains

    def validate(self,email: str):
        user_name, data = email.split('@')
        mail_name, domain_name = data.split('.')
        valid_name = self.__is_name_valid(user_name)
        valid_mail = self.__is_mail_valid(mail_name)
        valid_domain = self.__is_domain_valid(domain_name)

        if valid_name and valid_mail and valid_domain:
            return True
        else:
            return False

mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))


