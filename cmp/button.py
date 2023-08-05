from cmp.loader import loader_sm

def submit_button(value: str):
    hs_event = '_="on click toggle .hidden on me then toggle .hidden on the next <div/>"'
    return f'''
		<div class="w-full flex justify-center">
			<input {hs_event} type='submit' value='{value}' class="bg-main w-full text-white px-6 py-2 font-button text-sm rounded">
            {loader_sm()}
        </div>
	'''