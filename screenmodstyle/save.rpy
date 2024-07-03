init python:
    def pages_serie():
        page = int(persistent._file_page)
        
        if page % 10 == 0:
            return (page // 10) - 1
        else:
            return page // 10

    if persistent.pages_serie is None:
        if unicode(persistent._file_page).isnumeric():
            persistent.pages_serie = pages_serie()
        else:
            persistent.pages_serie = 0
