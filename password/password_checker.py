import hashlib
import requests
import sys


def request_api(query_char):
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching:{res.status_code}, check the api and try again!')
    return res


def get_leaked_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('UTF-8')).hexdigest().upper()
    first5_char, tail_char = sha1password[0:5], sha1password[5:]
    response = request_api(first5_char)
    return get_leaked_count(response, tail_char)


def main(argv):
    for password in argv:
        count = pwned_api_check(password)
        if count:
            print(
                f'{password} was found {count} times. You should change your password.')
        else:
            print(f'{password} ws NOT found. Carry on!')
    return 'Done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))