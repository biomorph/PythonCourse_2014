import sys
from subprocess import Popen, PIPE
import os


passed = True

if sys.version_info.major != 2 and sys.version_info.minor != 7:
    print "Wrong version of Python! Your version string is: ", sys.version
    print "We were expecting something starting with 2.7"
    passed = False

try:
    import numpy
    assert numpy.__version__ == '1.6.1'
except:
    print "Failed importing numpy, or wrong version"
    print "You have", numpy.__version__
    print "We were expecting '1.6.1'"
    passed = False

try:
    if 'darwin' in sys.platform:
        chimera = Popen(['/Applications/Chimera.app/Contents/MacOS/chimera',
                         '--version'], stdout=PIPE)
    else:
        chimera = Popen(['chimera', '--version'], stdout=PIPE)
    assert 'version 1.9' in chimera.communicate()[0]

except:
    print "Chimera not installed, or wrong version"
    print "We were expecting version 1.8"
    passed = False

try:
    git = Popen(['git', '--version'], stdout = PIPE)
    assert 'git version 1.8' in git.communicate()[0]
except:
    print "Git not installed, or wrong version"
    passed = False

try:
    Popen(["/bin/bash","-i","-c","aquamacs"])
except:
    print "Aquamacs not installed properly!"
    passed = False

if passed:
    print "Installation successful! Good job, now go enjoy your Sunday!"
else:
    print """Something went wrong. Look at the messages above, fix 'em, and then
    re-run this program"""



'''
try:
    import IPython
    import os
    ip = IPython.InteractiveShell()
    ip.editor = os.environ["EDITOR"]
    ip.magic("edit helper.py")
    assert "Failure" not in open('helper.py').read()
except:
    print "Aquamacs or emacs not installed properly"
    print "Did you change the line in the file like we told you?"
    passed = False

'''
