function scriptWork()
{
  //Opens the specified URL in a running instance of the specified browser.
  Browsers.Item(btEdge).Navigate("https://bearstore-testsite.smartbear.com/");
  //Maximizes the specified Window object.
  Aliases.browser.BrowserWindow.Maximize();
  //Clicks the 'linkContactUs' link.
  Aliases.browser.pageShop.header.navUsd.navContactUs.linkContactUs.Click();
  //Waits until the browser loads the page and is ready to accept user input.
  Aliases.browser.pageShop2.Wait();
  //Clicks the 'textboxYourName' control.
  Aliases.browser.pageShop2.sectionContent.formYourName.textboxYourName.Click();
  //Sets the text 'testUser' in the 'textboxYourName' text editor.
  Aliases.browser.pageShop2.sectionContent.formYourName.textboxYourName.SetText("testUser");
  //Enters '[Tab]' in the 'textboxYourName' object.
  Aliases.browser.pageShop2.sectionContent.formYourName.textboxYourName.Keys("[Tab]");
  //Sets the text 'test' in the 'emailinputYourEmail' text editor.
  Aliases.browser.pageShop2.sectionContent.formYourName.emailinputYourEmail.SetText("test");
  //Sets the text 'test@sb.com' in the 'emailinputYourEmail' text editor.
  Aliases.browser.pageShop2.sectionContent.formYourName.emailinputYourEmail.SetText("test@sb.com");
  //Enters '[Tab]' in the 'emailinputYourEmail' object.
  Aliases.browser.pageShop2.sectionContent.formYourName.emailinputYourEmail.Keys("[Tab]");
  //Enters 'what is my order n[Tab]?' in the 'textareaEnquiry' object.
  Aliases.browser.pageShop2.sectionContent.formYourName.textareaEnquiry.Keys("what is my order n[Tab]?");
  //Clicks the 'buttonSendEmail' button.
  Aliases.browser.pageShop2.sectionContent.formYourName.buttonSendEmail.ClickButton();
  //checking the error page popped up since the form is currently out of service
  //Checks whether the 'contentText' property of the Aliases.browser.pageShop2.textnodeOops object equals 'Oops!'.
 // aqObject.CheckProperty(Aliases.browser.pageShop2.textnodeOops, "contentText", cmpEqual, "Oops!");
  
 } 
/*  
function addNumbers(a, b) {
    return a + b;  // Returns the sum of a and b
}

let result = addNumbers(5, 10);
console.log(`Result: ${result}`);
}*/

function hoverOnScreenAction(Param1)
{
  //Launches the specified browser and opens the specified URL in it.
  Browsers.Item(btEdge).Run("https://bearstore-testsite.smartbear.com/");
  //Clicks the 'BrowserWindow' object.
  //Aliases.browser.BrowserWindow.Click(217, 93);
  Aliases.browser.BrowserWindow.Maximize();
  //Sets the specified position and size for the specific BrowserWindow object.
  //Aliases.browser.BrowserWindow.Position(784, 87, 1051, 893);
  //Place mouse pointer over the specified control (relative position).
  Aliases.browser.pageShop.header.navBooks.linkGaming.textnodeGaming.HoverMouse();
  //Clicks the 'textnodeGamingAccessories' control.
  Aliases.browser.pageShop.header.navBooks.linkGamingAccessories.textnodeGamingAccessories.Click();
}
