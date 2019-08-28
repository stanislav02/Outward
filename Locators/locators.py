class Locators():

    #Home page objects
    email_campaign_popup = "stickyOverlayWidget emailCampaignStickyOverlay"
    close_email_campaign_popup = "stickyOverlayMinimizeButton"
    search_bar = "search-field"
    store_locator_button = "//span[contains(text(),'Stores')]"

    #Product page objects
    product_page_url = "https://www.westelm.com/products/build-your-own-andes-sectional-extra-deep-h2517/?words=2613243&pkey=k2613243&sku=2613243#"
    product_image_url = "https://www.westelm.com/weimgs/ab/images/wcm/products/201932/0002/img28c.jpg"
    item_image = "hero"

    #Search page objects
    invalid_search_result_page_url = 'https://www.westelm.com/search/results.html?words=123456'
    unrecognized_query_message = "//li[@class='message']"

    #Store locator page objects
    store_locator_dropdown = "#state-list-selector"
    view_all_stores_button = "//a[@class='c-store-locator__map-search-toggle-link js-toggle-store-map-list']"
    store_count = "js-store-counter"