
from cmp.text import header_xxl
from cmp.button import submit_button
from cmp.input import text_input

CLASS_FORM_CONTAINER='p-4 m-2 rounded border border-t-2 border-l-2 border-gray-200 flex flex-col gap-4'


def login_form():
	return f'''
		<form hx-boost="true" id="login-form" class="{CLASS_FORM_CONTAINER}" method="POST" action="/login">
			{header_xxl(text='Login')}
			{text_input(label="Email", name="email")}
			{text_input(label="Password", name="password")}
			{submit_button(value="Login")}
		</form>
	'''

def signup_form():
	return f'''
		<form hx-boost="true" id="signup-form" class="{CLASS_FORM_CONTAINER}" method="POST" action="/signup">
			{header_xxl(text='Signup')}
			{text_input(label="Email", name="email")}
			{text_input(label="Password", name='password')}
			{submit_button(value="Signup")}
		</form>
	'''