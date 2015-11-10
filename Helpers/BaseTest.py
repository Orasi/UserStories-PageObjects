import os
import builtins
import threading
from appium_selector.DeviceSelector import DeviceSelector
from Helpers.FilePath import get_full_path


os.environ['PROJECTFOLDER'] = get_full_path('')

from hotdog.BaseTest import HotDogBaseTest

class BaseTest(HotDogBaseTest):

    @classmethod
    def setUpClass(cls):
        if not hasattr(builtins, 'threadlocal'):
            builtins.threadlocal = threading.local()
            builtins.threadlocal.config = DeviceSelector(platform='desktop').getDevice()[0]
    pass