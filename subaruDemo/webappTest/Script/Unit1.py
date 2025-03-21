def contactUsForm():
    #Launches the specified browser and opens the specified URL in it.
    Browsers.Item[btEdge].Run("https://bearstore-testsite.smartbear.com/")
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    Project.Variables.contactUsData.Reset()
    RecordIdx = 1
    while RecordIdx <= 3:
        #Clicks the 'linkContactUs' link.
        Aliases.browser.pageShop.header.navUsd.navContactUs.linkContactUs.Click()
        #Waits until the browser loads the page and is ready to accept user input.
        Aliases.browser.pageContactus.Wait()
        #Clicks the 'textboxYourName' control.
        Aliases.browser.pageContactus.sectionContent.formYourName.textboxYourName.Click()
        #Sets the text KeywordTests.contactUsForm.Variables.contactUsData["Name"] in the 'textboxYourName' text editor.
        Aliases.browser.pageContactus.sectionContent.formYourName.textboxYourName.SetText(Project.Variables.contactUsData.Value["Name"])
        #Enters '[Tab]' in the 'textboxYourName' object.
        Aliases.browser.pageContactus.sectionContent.formYourName.textboxYourName.Keys("[Tab]")
        #Sets the text KeywordTests.contactUsForm.Variables.contactUsData["Email"] in the 'emailinputYourEmail' text editor.
        Aliases.browser.pageContactus.sectionContent.formYourName.emailinputYourEmail.SetText(Project.Variables.contactUsData.Value["Email"])
        #Enters '[Tab]' in the 'emailinputYourEmail' object.
        Aliases.browser.pageContactus.sectionContent.formYourName.emailinputYourEmail.Keys("[Tab]")
        #Enters KeywordTests.contactUsForm.Variables.contactUsData["Enquiry"] in the 'textareaEnquiry' object.
        Aliases.browser.pageContactus.sectionContent.formYourName.textareaEnquiry.Keys(Project.Variables.contactUsData.Value["Enquiry"])
        #Clicks the 'buttonSendEmail' button.
        Aliases.browser.pageContactus.sectionContent.formYourName.buttonSendEmail.ClickButton()
        #Checks whether the 'contentText' property of the Aliases.browser.pageContactus.sectionContent.panelYourEnquiryHasBeen object equals 'Your enquiry has been successfully sent to the store owner.'.
        aqObject.CheckProperty(Aliases.browser.pageContactus.sectionContent.panelYourEnquiryHasBeen, "contentText", cmpEqual, "Your enquiry has been successfully sent to the store owner.", True)
        Project.Variables.contactUsData.Next()
        RecordIdx = RecordIdx + 1
    #Simulates a left-button single click in a window or control as specified (relative position, shift keys).
    #Aliases.browser.pageContactus.header.link.imageSmartstore.Click()
