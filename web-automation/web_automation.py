import webbrowser  # Import webbrowser library


def web_automation():  # Creating a function
    urls = ("stackoverflow.com", "github.com", "neuralnine.com")  # URLs we want to reach
    for url in urls:  # Creating a for-loop in order to open any URL at once.
        webbrowser.open("https://" + url)  # As we do not use a specific directory of Chrome, for example, we add
        # 'https://' to the URL to open it on default browser.


web_automation()    # Call the function
