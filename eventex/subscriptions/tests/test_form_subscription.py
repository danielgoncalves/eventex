from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must accept only digits."""
        form = self.make_validated_form(cpf='1A3B5C78901')
        self.assertFormErrorCode(form, 'cpf', 'cpf_wrong_content')

    def test_cpf_has_11_digits(self):
        """A valid CPF number must contains exactly 11 digits."""
        form = self.make_validated_form(cpf='1234567')
        self.assertFormErrorCode(form, 'cpf', 'cpf_wrong_length')

    def test_name_must_be_capitalized(self):
        """Name must be capitalized."""
        form = self.make_validated_form(name='JOHN programmer')
        self.assertEqual('John Programmer', form.cleaned_data['name'])

    def test_email_is_optional(self):
        """E-mail is optional."""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """Phone is optional."""
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        """E-mail and phone are optional, but one must be informed."""
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))

    def make_validated_form(self, **kwargs):
        data = dict(
                name='John Programmer',
                cpf='12345678901',
                email='john@example.com',
                phone='55-5555-5551')
        data.update(**kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        self.assertIn(field, errors)

        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)
