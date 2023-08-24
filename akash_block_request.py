from base64 import b64decode
from typing import Any

from requests import Response, get
from requests.exceptions import RequestException


def get_transaction_by_akash_block(block_height) -> str | list[bytes]:
    """Get transaction by the Akash block by the specified height."""
    url: str = f'https://akash-api.polkachu.com/blocks/{block_height}'
    try:
        response: Response = get(url)
        response.raise_for_status
        data: dict[str, Any] = response.json()
        if 'error' in data:
            return data['error']
        transactions: list[str] = data['block']['data']['txs']
        if transactions:
            return [b64decode(transaction) for transaction in transactions]
        return 'There are no transactions in this block.'
    except RequestException as error:
        return f'Request error: {error}.'
    except KeyError as error:
        return f'Key error: The "{error}" key is missing in data.'
    except Exception as error:
        return f'Error: {error}'
