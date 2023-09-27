import Amazon.gifts as gifts
import dataProcess.dataProcess as dp
import time
import excel.excelFormat as ef

def crawl_forAmazon_withTagging(link, excel_path, toCollect):
    gifts.get_gifts(link, excel_path, toCollect)
    max_retries = 5
    retry_delay = 3

    for i in range(max_retries):
        try:
            dp.tagging(excel_path)
            dp.translate(excel_path)
            break
        except Exception as e:
            print(f"An error occurred: {e}. Retrying.s..")
            time.sleep(retry_delay)
    else:
        print("Max retries reached. Exiting.")

    ef.excelFormat(excel_path)
    
def crawl_forAmazon_withoutTagging(link, excel_path, toCollect):
    gifts.get_gifts(link, excel_path, toCollect)
    max_retries = 5
    retry_delay = 3

    ef.excelFormat(excel_path)