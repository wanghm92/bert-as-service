import sys
import time

from service.client import BertClient

if __name__ == '__main__':
    bc = BertClient()#ip='localhost', port=int(sys.argv[1]))
    # encode a list of strings
    # with open('README.md') as fp:
    #     data = [v for v in fp if v.strip()]

    data = ['Bitar pulled off fine saves whenever they did .', 'then do it\'s right',
            'pope michael iii of alexandria ( also known as khail iii ) was the coptic pope of alexandria and patriarch of the see of st. mark ( 880 -- 907 ) .']

    # for j in range(1, 20000, 10):
    start_t = time.time()
    # tmp = data * j
    result, mask = bc.encode(data)
    # TODO: numpy array processing here
    for d, r, m in zip(data, result, mask):
        print("{}:\n {}".format(d, r))
        print(m)
        print("\n")
    time_t = time.time() - start_t
    print('encoding %d strs in %.2fs, speed: %d/s' %
          (len(data), time_t, int(len(data) / time_t)))
