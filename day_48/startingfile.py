from selenium import webdriver
from selenium.webdriver.common.by import By
URL = "https://www.amazon.in/NORTHWIND-Turtle-Cotton-T-Shirt-White/dp/B0CSFR6KLM/ref=sr_1_18?crid=X8XMOGI3TG3C&dib=eyJ2IjoiMSJ9.YwELi1CF4kinsJIaD67_f-bi5_tGxUr5h8BQ38_wDOkn308brNN3p93Ghzpq3e48po0p2uGYHje9rtBTxTRja-9PHtyCncSPaYC2bg3yIMH1aeqZn15T9beHcBtYxhgyIClBZ1m3yRuWuj_W28HB1H6sTGKl0godznulU6hni88S1JIANMXlElJU8gCSdoCidNpVPPn-QUxId0vzj2s7TxRIAn_EUkeeDa-1qmnchFSxnqCPY0pPaLMQdcA4lRQFmQ6EOxxl0OHUJHlD6lsNHvNxzbiQHU1EhSnoqLvXskk.cKrBxmv2ZOLN7mzCNde7-TekzPD6dFSWwPzsRjbZvdw&dib_tag=se&keywords=t%2Bshirt%2Bfor%2Bman&qid=1765808967&refinements=p_36%3A60000-80000%2Cp_n_pt_nav_size_men_international_size%3A1975395031&rnid=1974882031&sprefix=t%2B%2Caps%2C322&sr=8-18&th=1&psc=1"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
price = driver.find_element(By.XPATH,value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]').text
print(f"The shirts price today is {price}")
driver.quit()