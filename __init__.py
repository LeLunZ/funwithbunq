import argparse
import time

from bunq.sdk.context import ApiContext, ApiEnvironmentType
from bunq.sdk.context import BunqContext
from bunq.sdk.exception import BunqException
from bunq.sdk.model.generated import endpoint
from bunq.sdk.model.generated.object_ import Amount, Pointer

OPTION_API_KEY = '--api-key'

# Error constants.
ERROR_OPTION_MISSING_API_KEY = 'Missing mandatory option "--api-key [API key]"'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(OPTION_API_KEY)
    all_option = parser.parse_args()

    if all_option.api_key is None:
        raise BunqException(ERROR_OPTION_MISSING_API_KEY)

    api_context = ApiContext(ApiEnvironmentType.PRODUCTION, all_option.api_key, '*')
    BunqContext.load_api_context(api_context)
    end = 50
    for i in range(0, end):
        endpoint.Payment.create(amount=Amount('0.01', 'EUR'),
                                counterparty_alias=Pointer('IBAN', '', ''),
                                description=str(round(i / end * 100, 2)) + " Prozent von deinem Geld",
                                monetary_account_id=)
        time.sleep(0.33333)


if __name__ == '__main__':
    main()
