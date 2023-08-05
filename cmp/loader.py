from const.dom import BIG_LOADER_ID

def loader_sm():
    return f'<div class="h-10 w-10 hidden rounded-full border-4 animate-spin border border-gray-200 border-t-main"></div>'

def big_loader():
    return f'''
        <div id={BIG_LOADER_ID} class="flex justify-center hidden">
            <div class="flex h-full w-full opacity-50 bg-black absolute"></div>
            <div class="flex items-center mt-20 border-gray-200 absolute border-t-main border-4 animate-spin rounded-full h-24 w-24"></div>
        </div>
    '''