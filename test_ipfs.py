import ipfshttpclient
# import multiaddr
import store


ipfs = None


def main():
    print("create ipfs api ...")
    ipfs = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
    s = store.Store()
    s.init(ipfs)
    print("store file ... ")
    ret = s.store_1('test', recursive=True)
    # ret = ipfs.add('test', recursive=True)
    print(ret)
    print(ret[len(ret) - 1]['Hash'])

    print("id() ...")
    print(ipfs.id())

    print("pin ls() ...")
    print(ipfs.pin.ls(ret[len(ret) - 1]['Hash']))

    print("ls() ...")
    lsobj = ipfs.ls(ret[len(ret) - 1]['Hash'])
    print(lsobj)

    print("cat() ...")
    print(ipfs.cat(lsobj['Objects'][0]['Links'][0]['Hash']))


if __name__ == "__main__":
    main()
