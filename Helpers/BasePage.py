from hotdog.BasePage import HotDogBasePage

class BasePage(HotDogBasePage):

    def __init__(self, *args, **kwargs):
        """

        :rtype:
        """
        super().__init__(*args, **kwargs)

    def elemenent_exists(self, element):
        try:
            displayed = element.is_displayed()
            return True if displayed else False
        except:
            return False