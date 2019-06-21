add_one = lambda x: x + 1
result = add_one(2)
print(("simple result: ").format(result))

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
result2 = full_name('chad', 'duffey')
print(result2)