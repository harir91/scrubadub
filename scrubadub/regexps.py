"""regular expressions go here to prevent the code from becoming a gigantic
scary regular expression that is difficult to understand.
"""

import re

# there may be better solutions than this out there and this certainly
# doesn't do that great of a job with people that spell out the
# hyphenation of their email address, but its a pretty solid start.
#
# adapted from http://stackoverflow.com/a/719543/564709
EMAIL_REGEXS = (
    re.compile(r'\b[\w\.\+\-]+@[\w\-]+\.[\w\-\.]+\b'),
    re.compile(r'\b[\w\.\+\-]+ at [\w\-]+\.[\w\-\.]+\b'),
    re.compile(r'\b[\w\.\+\-]+ AT [\w\-]+\.[\w\-\.]+\b'),
)

# this regular expression is convenient for captures the domain name
# and the path separately, which is useful for keeping the domain name
# but sanitizing the path altogether
URL_REGEX = re.compile(r'''
    (?P<domain_name>
        (https?:\/\/(www\.)?|www\.)          # protocol http://, https://, www.
        [\-\w@:%\.\+~\#=]{2,256}\.[a-z]{2,6} # domain name
    )(?P<path>
        [\-\w@:%\+\.~\#?&//=]*               # rest of path, query, and hash
    )
''', re.VERBOSE)
