def text_input(label: str):
	return f'''
		<div class="flex flex-col">
			<label class="text-xs font-text mb-1">{label}</label>
			<input type=text class="border border-gray-200 text-xs p-2 rounded" />
		</div>
	'''