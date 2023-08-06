def text_input(label: str, name: str):
	return f'''
		<div class="flex flex-col">
			<label for="{name}" class="text-xs font-text mb-1 text-textColor">{label}</label>
			<input name="{name}" type=text class="border border-gray-200 text-xs p-2 rounded outline-none focus:border-gray-400" />
		</div>
	'''