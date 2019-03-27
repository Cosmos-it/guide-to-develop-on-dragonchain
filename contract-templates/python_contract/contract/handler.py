import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main(payload):
    eprint('Hello Code Fellows today')
    sys.stdout.write('Testing;')
    return {
        'invoker_transaction_type': payload['header']['txn_type'],
    }
