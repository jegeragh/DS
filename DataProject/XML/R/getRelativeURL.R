getRelativeURL =
  #
  #  takes the name of a file/URL and a baseURL and 
  # figures out the URL for the new file given by u.
  # This handles the case where the file/URL is relative to the
  # the baseURL or if it is a fully qualified file or URL.

  #
  #  getRelativeURL("/foo", "http://www.omegahat.org")
  #  getRelativeURL("/foo", "http://www.omegahat.org/")
  #  getRelativeURL("foo", "http://www.omegahat.org/")
  #  getRelativeURL("http://www.foo.org", "http://www.omegahat.org/")
  #
  # XXX test - baseURL with /path/ and u as /other/path. Looks okay. See
  # ParsingStrategies example for kaggle.
  #   getRelativeURL("../foo/xyz/bar.html", "http://www.omegahat.org/a/b.html")
  # getRelativeURL("./foo/xyz/bar.html", "http://www.omegahat.org/a/b.html")
  #  getRelativeURL("../foo/xyz/bar.html", "http://www.omegahat.org/a/b.html")
  #
  #
  #  BROKEN
  #   getRelativeURL("foo", ".")   yields :///foo
  #
  #
  # [Fixed] not working for ../...
  #  fails
  #    getRelativeURL("../foo", "http://www.omegahat.org/a/b.html")
  # should be http://www.omegahat.org/foo
  # or at least http://www.omegahat.org/a/../foo
function(u, baseURL, sep = "/", addBase = TRUE)  
{
   if(length(u) > 1)
     return(sapply(u, getRelativeURL, baseURL, sep))
   
   pu = parseURI(u)
   #XXX Need to strip the path in baseURL if pu$path starts with /
   if(pu$scheme == "" && addBase) {
      b = parseURI(baseURL)
      b$query = ""
      if(grepl("^/", pu$path)) {
        b$path = u
        return(as(b, "character"))
      }

      b$path = sprintf("%s%s%s", dirname(b$path), sep, u)
        # handle .. in the path and try to collapse these.
      if(grepl("..", b$path, fixed = TRUE)) {
        els = strsplit(b$path, sep)[[1]]
        i = which(els == "..")
        els = els[-c(i, i-1)]
        b$path = paste(els, collapse = sep)
      }
      return(as(b, "character"))         
#      b = as(b, "character")
#      sprintf("%s%s%s", b, "" else sep, u)
   } else
      u
}
