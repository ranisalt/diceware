#!/usr/bin/env python3
import argparse
import random

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--delimiter', '-d', default='', metavar='DELIM',
            help='use DELIM as the output delimiter (default: none)')
    parser.add_argument('--length', '-l', default=16, metavar='N', type=int,
            help='force at least N characters for password (default: 16)')
    parser.add_argument('--words', '-w', metavar='N', type=int,
            help='use exactly N words for password')
    parser.add_argument('wordlist', nargs=1)
    args = parser.parse_args()

    # wordlist parsing. the wordlist MUST be in the following pattern:
    # 11111 wordfirst
    # 11112 wordsecond
    # ...
    # 66666 wordlast
    # separator doesn't matter as long as it is a single character (e.g. tab)
    # there must be only one word per line
    with open(args.wordlist[0]) as wordlist:
        wordmap = {int(splot[0:5]): splot[6:-1] for splot in wordlist}

    def gen_word():
        # generate 5 random integers from 1 to 6 (inclusive)
        rands = (random.randint(1, 6) for _ in range(5))

        _sum = 0
        for rand in rands:
            _sum = _sum * 10 + rand

        return wordmap[_sum]

    password = []

    # generate words until word count accomplished (if -w is provided) or
    # until minimum length is reached (if nothing or -l is provided)
    while len(password) < args.words if args.words else \
        sum(map(len, password)) < args.length:
        password.append(gen_word())

    print(args.delimiter.join(password))
