def domain_name(url):
    strings_to_remove = ["www.", "http://", "https://",".com"]
    for string in strings_to_remove:
        url = url.replace(string, "") 
    if url.find(".") < 0:
        if url.find("/") < 0:
            return url
        else:
            return url[0:url.find("/")]
    else:
        return url[0:url.find(".")]

#def domain_name(url):
#    return url.split("//")[-1].split("www.")[-1].split(".")[0]

domain_name("https://youtube.com")