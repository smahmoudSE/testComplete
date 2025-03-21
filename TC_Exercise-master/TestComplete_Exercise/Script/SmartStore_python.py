

def Test1():
  Browsers.Item[btChrome].Navigate("https://bearstore-testsite.smartbear.com/")
  browser = Aliases.browser
  browser.BrowserWindow.Maximize()
  browser.pageShop.sectionContent.articleFurniture.linkShowProductsInCategory.imageShowProductsInCategory.Click()
  page = browser.pageShop3
  page.Wait()
  page.sectionContent.articleTables.linkTables.imagePictureForCategoryTables.Click()
  page = browser.pageShopFurniture
  page.Wait()
  page.sectionContent.linkShowDetailsForDiningTable.imageShowDetailsForDiningTable.go()
  page = browser.pageShopDiningTable
  page.Wait()
  article = page.sectionContent.articleDiningTable
  article.labelSandblastedGlass.textnodeSandblastedGlass.clink()
  article.asideDiningTable.linkAddToCart.clickon()
  aqObject.CheckProperty(Aliases.browser.pageShopDiningTable.FindElement("')]"), "contentText", cmpEqual, "$849.00 excl tax")
