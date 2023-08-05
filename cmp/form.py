
from cmp.text import header_xxl
from cmp.button import submit_button
from cmp.input import text_input

CLASS_FORM_CONTAINER='class="p-4 m-2 rounded border border-gray-200 flex flex-col gap-4"'


def login_form():
	return f'''
		<form id="login-form" {CLASS_FORM_CONTAINER}>
			{header_xxl(text='Login')}
			{text_input(label="Email")}
			{text_input(label="Password")}
			{submit_button(value="Login")}
		</form>
	'''

def signup_form():
	return f'''
		<form id="signup-form" {CLASS_FORM_CONTAINER}>
			{header_xxl(text='Signup')}
			{text_input(label="Email")}
			{text_input(label="Password")}
			{submit_button(value="Signup")}
		</form>
	'''