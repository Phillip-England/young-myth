from cmp.text import header_xxl, text_form_error
from cmp.button import submit_button
from cmp.input import text_input

CLASS_FORM_CONTAINER = (
    "p-4 m-2 rounded border border-t-2 border-l-2 border-gray-200 flex flex-col gap-4"
)


def login_form(err: str = '', email: str = '', password: str = ''):
    error_component = text_form_error(err) if err else ""
    return f"""
		<form hx-boost="true" id="login-form" class="{CLASS_FORM_CONTAINER}" method="POST" action="/login">
			{header_xxl(text='Login')}
			{error_component}
			{text_input(label="Email", name="email", value=email)}
			{text_input(label="Password", name="password", input_type='password', value=password)}
			{submit_button(value="Login")}
		</form>
	"""


def signup_form(err: str = "", email: str = "", password: str = ""):
    error_component = text_form_error(err) if err else ""
    return f"""
		<form hx-boost="true" id="signup-form" class="{CLASS_FORM_CONTAINER}" method="POST" action="/signup">
			{header_xxl(text='Signup')}
			{error_component}
			{text_input(label="Email", name="email", value=email)}
			{text_input(label="Password", name='password', input_type='password', value=password)}
			{submit_button(value="Signup")}
		</form>
	"""
