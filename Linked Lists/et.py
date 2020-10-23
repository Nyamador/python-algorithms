def namelist(names):
    # get the last item
    final = ''
    last_two = ''
    for dict in names:
        if dict == names[-2]:
            last_two += dict['name']
            names.pop(-2)
        if dict == names[-1]:
            # last_two += ' & '
            amper = "&"
            last_two += f' {amper} {dict["name"]}'
            names.pop(-1)
        print("as", last_two)

        final += dict['name']
        final += ' '
        last_two += final
        # print(last_two)
    print(final)

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])