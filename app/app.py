import json
import os

from playwright.sync_api import sync_playwright

url = os.environ.get('URL', None) 
account = os.environ.get('ACCOUNT', None)
birthday_year = os.environ.get('BIRTHDAY_YEAR', None)
birthday_month = os.environ.get('BIRTHDAY_MONTH', None)
birthday_day = os.environ.get('BIRTHDAY_DAY', None)
tpoint_no = os.environ.get('TPOINT_NO', None)
email = os.environ.get('EMAIL', None)

def run(playwright):

    browser = playwright.chromium.launch(headless=True, args=[
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '-–disable-dev-shm-usage',
        '--disable-gpu',
        '--no-first-run',
        '--no-zygote',
        '--single-process',
    ])
    context = browser.new_context()

    page = context.new_page()

    # ---------------------
    page.goto(url)

    page.wait_for_timeout(5 * 1000)

    page.fill('input[name="singleAnswer(ANSWER42)"]', account)

    page.fill('input[name="singleAnswer(ANSWER43-1)"]', birthday_year)
    page.fill('input[name="singleAnswer(ANSWER43-2)"]', birthday_month)
    page.fill('input[name="singleAnswer(ANSWER43-3)"]', birthday_day)

    page.fill('input[name="singleAnswer(ANSWER31)"]', tpoint_no)
    page.fill('input[name="singleAnswer(ANSWER34)"]', email)

    page.check('//*[@id="policy_agree"]/div/label')

    page.click('input[type="submit"]')

    page.wait_for_timeout(3 * 1000)

    page.click('input[type="submit"]')

    page.wait_for_timeout(3 * 1000)

    # ---------------------
    context.close()
    browser.close()


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    Output : dict

    """

#    print(os.environ)

    if account is None:
        raise ValueError('Value Error')

    with sync_playwright() as playwright:
        run(playwright)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world",
            }
        ),
    }
