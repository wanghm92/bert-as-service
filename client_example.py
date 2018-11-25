import sys
import time

from service.client import BertClient

if __name__ == '__main__':
    bc = BertClient()#ip='localhost', port=int(sys.argv[1]))
    # encode a list of strings
    # with open('README.md') as fp:
    #     data = [v for v in fp if v.strip()]

    # for j in range(1, 200, 10):
    start_t = time.time()
    # tmp = data * j
    data = ['First do it', 'then do it\'s right', 'then do it better']
    result = bc.encode(data)
    # TODO: numpy array processing here
    for d, r in zip(data, result):
        print("{}: {}\n".format(d, r))
    time_t = time.time() - start_t
    print('encoding %d strs in %.2fs, speed: %d/s' %
          (len(data), time_t, int(len(data) / time_t)))
