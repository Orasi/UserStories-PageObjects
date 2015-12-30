from time import sleep
import webium
from hotdog.Config import GetConfig

from Helpers.BaseTest import BaseTest
from Pages.Common import CommonPage
from Pages.ContentDetailPage import ContentDetailPage
from Pages.ShowDetailsPage import ShowDetailsPage
from Pages.ShowsPage import ShowsPage

class ContentDetailsTest(BaseTest):

    def test_contentDetailsElements(self):

        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()
        common.navigateToSection('SHOWS')

        #Navigate to all shows and select show
        shows = ShowsPage(driver=self.driver)
        shows.sync()
        isMobile = shows.isMobile
        showTitle = shows.clickOnShow(random=True)

        #Navigate to Content Detail
        sleep(1)
        showDetail = ShowDetailsPage(driver=self.driver)
        showDetail.sync(showTitle)
        showDetail.clickOnEpisode(random=True)

        #Validate Content Detail Elements
        contentDetail = ContentDetailPage(driver=self.driver)
        contentDetail.assert_element_present('txtBreadcrumbs')
        contentDetail.assert_element_present('btnPlay')
        if not isMobile:
            contentDetail.assert_element_present('imgAd')
        contentDetail.assert_element_present('txtEpisodeNumber')
        contentDetail.assert_element_present('txtDuration')
        contentDetail.assert_element_present('txtEpisodeTitle')
        contentDetail.assert_element_present('txtDescription')
        contentDetail.assert_element_present('txtCredits')

    def test_navigateBreadcrumb(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()
        common.navigateToSection('SHOWS')

        #Navigate to all shows and select show
        sleep(1)
        shows = ShowsPage(driver=self.driver)
        showTitle = shows.clickOnShow(random=True)

        #Navigate to Content Detail
        sleep(1)
        showDetail = ShowDetailsPage(driver=self.driver)
        showDetail.clickOnEpisode(random=True)

        #Navigate Back via breadcrumb
        contentDetail = ContentDetailPage(driver=self.driver)
        contentDetail.sync()
        contentDetail.assert_element_present('txtBreadcrumbs')
        breadcrumb = contentDetail.txtBreadcrumbs.text
        self.assertEqual(breadcrumb.lower(), showTitle.lower(), 'Breadcrumb does not match expected show title. Expected [%s].  Actual [%s]' % (breadcrumb, showTitle))
        contentDetail.txtBreadcrumbs.click()

        #Validate Navigated back to correct Show Detail page
        sleep(1)
        showDetail = ShowDetailsPage(driver=self.driver)
        showDetail.sync(showTitle)
        self.assertEqual(breadcrumb.lower(), showDetail.txtSeriesTitle.text.lower(),
                         'Failed to navigate back to correct page via breadcrumb.  Expected [%s].  Actual [%s]' % (breadcrumb, showDetail.txtSeriesTitle.text))

