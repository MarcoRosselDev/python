def comon_pattern(*items):
    for i in items:
        # we can use any string methods tho match results
        # count(), endwith(), find(), rfind(),
        if i.find('land') != -1:
            return True
        else:
            return False
